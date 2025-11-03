#!/usr/bin/env python3
"""
技能包裝和验证脚本
用于验证技能结构并打包成可分发的zip文件
"""

import os
import json
import zipfile
from pathlib import Path
from typing import Dict, List, Any
import argparse

# 简单的YAML解析器（避免依赖外部库）
def simple_yaml_load(content: str) -> Dict:
    """简单的YAML解析器，只处理基本的键值对"""
    result = {}
    for line in content.split('\n'):
        line = line.strip()
        if line and ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            # 移除引号
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            result[key] = value
    return result

class SkillPackageValidator:
    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)
        self.validation_result = {
            "valid": True,
            "errors": [],
            "warnings": [],
            "info": []
        }

    def validate_and_package(self, output_path: str = None) -> bool:
        """验证技能并打包"""
        print("开始验证技能结构...")

        # 执行所有验证
        self._validate_basic_structure()
        self._validate_skill_metadata()
        self._validate_skill_content()
        self._validate_file_organization()
        self._validate_references()
        self._validate_scripts()
        self._validate_assets()

        # 输出验证结果
        self._print_validation_results()

        if not self.validation_result["valid"]:
            print("❌ 技能验证失败，请修复错误后重试")
            return False

        print("✅ 技能验证通过！")

        # 打包技能
        if output_path:
            return self._package_skill(output_path)

        return True

    def _validate_basic_structure(self):
        """验证基础目录结构"""
        print("检查基础目录结构...")

        required_dirs = ["scripts", "references", "assets"]
        for dir_name in required_dirs:
            dir_path = self.skill_path / dir_name
            if not dir_path.exists():
                self._add_error(f"缺少必需目录: {dir_name}")
            elif not dir_path.is_dir():
                self._add_error(f"路径不是目录: {dir_name}")
            else:
                self._add_info(f"✅ 目录存在: {dir_name}")

    def _validate_skill_metadata(self):
        """验证技能元数据"""
        print("📋 检查技能元数据...")

        skill_md_path = self.skill_path / "SKILL.md"
        if not skill_md_path.exists():
            self._add_error("缺少 SKILL.md 文件")
            return

        try:
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 检查YAML前置内容
            if not content.startswith('---'):
                self._add_error("SKILL.md 必须以 YAML 前置内容开始")
                return

            # 提取YAML前置内容
            try:
                end_index = content.find('---', 3)
                if end_index == -1:
                    self._add_error("YAML 前置内容格式错误，缺少结束标记")
                    return

                yaml_content = content[3:end_index].strip()
                metadata = simple_yaml_load(yaml_content)

                # 验证必需字段
                required_fields = ["name", "description"]
                for field in required_fields:
                    if field not in metadata:
                        self._add_error(f"YAML 前置内容缺少必需字段: {field}")
                    elif not metadata[field]:
                        self._add_error(f"YAML 前置内容字段不能为空: {field}")

                # 验证字段内容质量
                if "name" in metadata:
                    name = metadata["name"]
                    if len(name) < 3:
                        self._add_warning("技能名称过短，建议至少3个字符")
                    if not name.replace('-', '').replace('_', '').isalnum():
                        self._add_warning("技能名称建议只使用字母、数字、连字符和下划线")

                if "description" in metadata:
                    description = metadata["description"]
                    if len(description) < 20:
                        self._add_warning("技能描述过短，建议至少20个字符")
                    if "should be used when" not in description.lower():
                        self._add_warning("建议在描述中说明何时使用此技能")

                self._add_info("✅ SKILL.md 元数据验证通过")

            except Exception as e:
                self._add_error(f"YAML 前置内容解析错误: {e}")

        except Exception as e:
            self._add_error(f"读取 SKILL.md 文件失败: {e}")

    def _validate_skill_content(self):
        """验证技能内容质量"""
        print("📖 检查技能内容质量...")

        skill_md_path = self.skill_path / "SKILL.md"
        try:
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 提取正文内容
            if '---' in content:
                end_index = content.find('---', 3)
                if end_index != -1:
                    body_content = content[end_index + 3:].strip()
                else:
                    body_content = content
            else:
                body_content = content

            # 检查内容长度
            if len(body_content) < 500:
                self._add_warning("技能内容过短，建议至少500字符")
            elif len(body_content) > 10000:
                self._add_warning("技能内容过长，建议控制在10000字符以内")

            # 检查标题结构
            if not body_content.startswith('#'):
                self._add_warning("建议以一级标题开始技能内容")

            # 检查是否包含关键信息
            key_sections = ["使用", "功能", "工作流程", "输出", "工具"]
            missing_sections = []
            for section in key_sections:
                if section not in body_content:
                    missing_sections.append(section)

            if missing_sections:
                self._add_warning(f"建议包含以下部分: {', '.join(missing_sections)}")

            # 检查是否有示例
            if "示例" not in body_content and "example" not in body_content.lower():
                self._add_warning("建议添加使用示例")

            self._add_info("✅ 技能内容质量检查完成")

        except Exception as e:
            self._add_error(f"分析技能内容失败: {e}")

    def _validate_file_organization(self):
        """验证文件组织结构"""
        print("📂 检查文件组织结构...")

        # 检查目录结构合理性
        for root, dirs, files in os.walk(self.skill_path):
            # 跳过隐藏目录
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for file in files:
                if file.startswith('.'):
                    continue  # 跳过隐藏文件

                file_path = Path(root) / file
                relative_path = file_path.relative_to(self.skill_path)

                # 检查文件大小
                if file_path.stat().st_size > 10 * 1024 * 1024:  # 10MB
                    self._add_warning(f"文件过大: {relative_path} (>10MB)")

                # 检查文件扩展名
                if file.endswith(('.tmp', '.bak', '.log')):
                    self._add_warning(f"包含临时文件: {relative_path}")

        self._add_info("✅ 文件组织结构检查完成")

    def _validate_references(self):
        """验证参考文档"""
        print("📚 检查参考文档...")

        refs_dir = self.skill_path / "references"
        if not refs_dir.exists():
            return

        ref_files = list(refs_dir.glob("*.md"))
        if not ref_files:
            self._add_warning("references 目录为空，建议添加参考文档")
            return

        for ref_file in ref_files:
            # 检查文件大小
            if ref_file.stat().st_size < 100:
                self._add_warning(f"参考文档过小: {ref_file.name}")
            elif ref_file.stat().st_size > 1024 * 1024:  # 1MB
                self._add_info(f"参考文档较大: {ref_file.name} (建议使用grep模式)")

        self._add_info(f"✅ 找到 {len(ref_files)} 个参考文档")

    def _validate_scripts(self):
        """验证脚本文件"""
        print("⚙️ 检查脚本文件...")

        scripts_dir = self.skill_path / "scripts"
        if not scripts_dir.exists():
            return

        script_files = []
        for pattern in ["*.py", "*.js", "*.sh", "*.bat"]:
            script_files.extend(scripts_dir.glob(pattern))

        if not script_files:
            self._add_warning("scripts 目录为空，建议添加工具脚本")
            return

        for script_file in script_files:
            # 检查文件权限
            if not os.access(script_file, os.R_OK):
                self._add_error(f"脚本文件不可读: {script_file.name}")

            # 检查shebang（适用于Unix脚本）
            if script_file.suffix in ['.sh', '.py']:
                try:
                    with open(script_file, 'r', encoding='utf-8') as f:
                        first_line = f.readline().strip()
                        if script_file.suffix == '.sh' and not first_line.startswith('#!'):
                            self._add_warning(f"Shell脚本建议添加shebang: {script_file.name}")
                except:
                    pass

        self._add_info(f"✅ 找到 {len(script_files)} 个脚本文件")

    def _validate_assets(self):
        """验证资源文件"""
        print("🎨 检查资源文件...")

        assets_dir = self.skill_path / "assets"
        if not assets_dir.exists():
            return

        asset_files = list(assets_dir.rglob("*"))
        asset_files = [f for f in asset_files if f.is_file()]

        if not asset_files:
            self._add_info("assets 目录为空")
            return

        # 统计文件类型
        file_types = {}
        total_size = 0
        for asset_file in asset_files:
            ext = asset_file.suffix.lower()
            file_types[ext] = file_types.get(ext, 0) + 1
            total_size += asset_file.stat().st_size

        self._add_info(f"✅ 找到 {len(asset_files)} 个资源文件")
        self._add_info(f"📊 资源文件类型分布: {dict(file_types)}")
        self._add_info(f"💾 资源文件总大小: {total_size / 1024:.1f} KB")

        # 检查是否有模板文件
        if not any(f.name.lower().startswith('template') for f in asset_files):
            self._add_warning("建议在assets中包含模板文件")

    def _package_skill(self, output_path: str) -> bool:
        """打包技能"""
        print(f"📦 开始打包技能到: {output_path}")

        try:
            skill_name = self.skill_path.name
            if not output_path.endswith('.zip'):
                output_path = f"{output_path}/{skill_name}.zip"

            # 确保输出目录存在
            output_dir = Path(output_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)

            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(self.skill_path):
                    # 跳过隐藏目录和文件
                    dirs[:] = [d for d in dirs if not d.startswith('.')]
                    files = [f for f in files if not f.startswith('.')]

                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(self.skill_path)
                        zipf.write(file_path, arcname)

            # 计算压缩信息
            original_size = sum(f.stat().st_size for f in self.skill_path.rglob('*') if f.is_file())
            compressed_size = Path(output_path).stat().st_size
            compression_ratio = (1 - compressed_size / original_size) * 100

            print(f"✅ 技能打包成功!")
            print(f"📁 原始大小: {original_size / 1024:.1f} KB")
            print(f"📦 压缩大小: {compressed_size / 1024:.1f} KB")
            print(f"📊 压缩率: {compression_ratio:.1f}%")
            print(f"📍 输出路径: {output_path}")

            return True

        except Exception as e:
            self._add_error(f"打包技能失败: {e}")
            return False

    def _add_error(self, message: str):
        """添加错误信息"""
        self.validation_result["errors"].append(message)
        self.validation_result["valid"] = False

    def _add_warning(self, message: str):
        """添加警告信息"""
        self.validation_result["warnings"].append(message)

    def _add_info(self, message: str):
        """添加信息"""
        self.validation_result["info"].append(message)

    def _print_validation_results(self):
        """打印验证结果"""
        print("\n" + "="*50)
        print("📋 验证结果报告")
        print("="*50)

        if self.validation_result["errors"]:
            print(f"\n❌ 错误 ({len(self.validation_result['errors'])}):")
            for error in self.validation_result["errors"]:
                print(f"   • {error}")

        if self.validation_result["warnings"]:
            print(f"\n⚠️ 警告 ({len(self.validation_result['warnings'])}):")
            for warning in self.validation_result["warnings"]:
                print(f"   • {warning}")

        if self.validation_result["info"]:
            print(f"\n✅ 信息 ({len(self.validation_result['info'])}):")
            for info in self.validation_result["info"]:
                print(f"   • {info}")

        print("\n" + "="*50)

def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(description="验证和打包技能")
    parser.add_argument("skill_path", help="技能目录路径")
    parser.add_argument("--output", "-o", help="输出目录路径")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")

    args = parser.parse_args()

    if not os.path.exists(args.skill_path):
        print(f"❌ 技能路径不存在: {args.skill_path}")
        return 1

    validator = SkillPackageValidator(args.skill_path)
    success = validator.validate_and_package(args.output)

    return 0 if success else 1

if __name__ == "__main__":
    exit(main())