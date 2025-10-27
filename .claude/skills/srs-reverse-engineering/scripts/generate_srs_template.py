#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SRS模板生成脚本
基于分析结果生成标准化的软件需求规格说明书
"""

import os
import json
import sys
from typing import Dict, List, Optional
from datetime import datetime

# 设置标准输出编码为UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
from pathlib import Path

class SRSTemplateGenerator:
    def __init__(self):
        self.srs_data = {
            "project_info": {},
            "database_analysis": {},
            "api_analysis": {},
            "code_analysis": {},
            "business_rules": []
        }

    def load_analysis_results(self, analysis_dir: str) -> None:
        """加载分析结果"""
        analysis_path = Path(analysis_dir)

        # 加载数据库分析结果
        db_file = analysis_path / "database_analysis.json"
        if db_file.exists():
            with open(db_file, 'r', encoding='utf-8') as f:
                self.srs_data["database_analysis"] = json.load(f)

        # 加载API分析结果
        api_file = analysis_path / "api_analysis.json"
        if api_file.exists():
            with open(api_file, 'r', encoding='utf-8') as f:
                self.srs_data["api_analysis"] = json.load(f)

        # 加载代码分析结果
        code_file = analysis_path / "code_analysis.json"
        if code_file.exists():
            with open(code_file, 'r', encoding='utf-8') as f:
                self.srs_data["code_analysis"] = json.load(f)

        # 提取项目信息
        if "project_info" in self.srs_data["code_analysis"]:
            self.srs_data["project_info"] = self.srs_data["code_analysis"]["project_info"]

        # 提取业务规则
        if "business_rules" in self.srs_data["code_analysis"]:
            self.srs_data["business_rules"] = self.srs_data["code_analysis"]["business_rules"]

    def generate_srs_document(self, output_path: str) -> None:
        """生成SRS文档"""
        srs_content = self._build_srs_content()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(srs_content)

    def _build_srs_content(self) -> str:
        """构建SRS内容"""
        project_name = self.srs_data["project_info"].get("name", "Unknown Project")
        current_date = datetime.now().strftime("%Y年%m月%d日")

        srs_lines = [
            f"# {project_name} - 软件需求规格说明书 (SRS)",
            "",
            f"**生成日期**: {current_date}",
            "**文档类型**: 逆向工程生成文档",
            "**分析方法**: 自动化代码分析与推断",
            "",
            "---",
            "",
            "## 1. 引言",
            "",
            "### 1.1 目的",
            "本文档通过逆向工程分析现有代码库，系统地提取和记录系统的功能需求、接口需求和非功能需求。",
            "由于是通过代码分析推导得出，本文档主要反映系统当前实现的功能，可能存在遗漏或需要进一步确认的内容。",
            "",
            "### 1.2 项目范围",
            self._generate_project_scope(),
            "",
            "### 1.3 定义、首字母缩写词和缩略语",
            self._generate_definitions(),
            "",
            "## 2. 总体描述",
            "",
            "### 2.1 产品功能",
            self._generate_product_functions(),
            "",
            "### 2.2 用户特征",
            self._generate_user_characteristics(),
            "",
            "### 2.3 运行环境",
            self._generate_operating_environment(),
            "",
            "### 2.4 设计和实现约束",
            self._generate_design_constraints(),
            "",
            "## 3. 功能需求",
            "",
            self._generate_functional_requirements(),
            "",
            "## 4. 外部接口需求",
            "",
            "### 4.1 用户界面",
            self._generate_ui_requirements(),
            "",
            "### 4.2 软件接口",
            self._generate_software_interfaces(),
            "",
            "### 4.3 硬件接口",
            "暂无相关信息",
            "",
            "## 5. 非功能需求",
            "",
            "### 5.1 性能需求",
            self._generate_performance_requirements(),
            "",
            "### 5.2 安全性需求",
            self._generate_security_requirements(),
            "",
            "### 5.3 可靠性需求",
            self._generate_reliability_requirements(),
            "",
            "### 5.4 可维护性需求",
            self._generate_maintainability_requirements(),
            "",
            "## 6. 数据需求",
            "",
            self._generate_data_requirements(),
            "",
            "## 7. 附录",
            "",
            "### 7.1 分析方法说明",
            "本文档通过以下自动化分析工具生成：",
            "- 数据库逆向工程分析",
            "- API接口自动发现",
            "- 代码结构静态分析",
            "- 业务规则提取",
            "",
            "### 7.2 局限性说明",
            "1. **信息不完整性**: 部分需求可能未在代码中明确体现",
            "2. **推断性质**: 某些需求和规则是基于代码模式推断得出",
            "3. **需要验证**: 建议与项目相关人员确认分析结果的准确性",
            "4. **动态行为**: 文档主要基于静态代码分析，可能遗漏运行时行为",
            "",
            f"---",
            f"*本文档由SRS逆向工程工具自动生成于 {current_date}*"
        ]

        return "\n".join(srs_lines)

    def _generate_project_scope(self) -> str:
        """生成项目范围描述"""
        project_info = self.srs_data["project_info"]
        frameworks = project_info.get("frameworks", [])
        language = project_info.get("language", "Unknown")

        scope = f"本项目是一个基于 {language} 开发的软件系统"
        if frameworks:
            scope += f"，使用了 {', '.join(frameworks)} 框架"

        # 根据发现的API端点推断功能范围
        api_data = self.srs_data["api_analysis"]
        total_endpoints = api_data.get("total_endpoints", 0)
        if total_endpoints > 0:
            scope += f"，提供了 {total_endpoints} 个API接口"

        # 根据数据库表推断数据管理范围
        db_data = self.srs_data["database_analysis"]
        if db_data:
            table_count = len(db_data.keys())
            scope += f"，管理 {table_count} 个数据表"

        scope += "。"

        return scope

    def _generate_definitions(self) -> str:
        """生成术语定义"""
        definitions = []

        project_info = self.srs_data["project_info"]
        language = project_info.get("language", "").lower()
        frameworks = project_info.get("frameworks", [])

        # 根据技术栈添加相关术语
        if language == "python":
            definitions.extend([
                "**Python**: 项目使用的编程语言",
            ])
        elif language in ["javascript", "typescript"]:
            definitions.extend([
                f"**{language.title()}**: 项目使用的编程语言",
            ])

        for framework in frameworks:
            if "Express" in framework:
                definitions.append("**Express.js**: Node.js Web应用框架")
            elif "Django" in framework:
                definitions.append("**Django**: Python Web应用框架")
            elif "Spring" in framework:
                definitions.append("**Spring Boot**: Java企业级应用框架")

        # 添加通用术语
        definitions.extend([
            "**API**: 应用程序编程接口",
            "**SRS**: 软件需求规格说明书",
            "**ERD**: 实体关系图",
        ])

        if not definitions:
            return "暂无特殊术语定义"

        return "\n".join(definitions)

    def _generate_product_functions(self) -> str:
        """生成产品功能描述"""
        functions = []

        # 基于API模块分析功能
        api_data = self.srs_data["api_analysis"]
        endpoints = api_data.get("endpoints", [])

        if endpoints:
            # 按路径分组
            modules = {}
            for endpoint in endpoints:
                path = endpoint.get("path", "")
                module_name = path.split("/")[1] if "/" in path and len(path.split("/")) > 1 else "root"
                if module_name not in modules:
                    modules[module_name] = []
                modules[module_name].append(endpoint)

            for module, module_endpoints in modules.items():
                functions.append(f"- **{module.title()}模块**: 提供 {len(module_endpoints)} 个API接口")

        # 基于数据库表分析数据管理功能
        db_data = self.srs_data["database_analysis"]
        if db_data:
            functions.append(f"- **数据管理**: 管理核心业务数据，包含 {len(db_data)} 个数据表")

        # 基于业务规则分析业务逻辑
        business_rules = self.srs_data["business_rules"]
        if business_rules:
            rule_types = set(rule["rule_type"] for rule in business_rules)
            for rule_type in rule_types:
                count = len([r for r in business_rules if r["rule_type"] == rule_type])
                functions.append(f"- **{rule_type.title()}逻辑**: 包含 {count} 个业务规则")

        if not functions:
            return "基于代码分析，系统主要提供基础的数据处理和接口服务功能。"

        return "\n".join(functions)

    def _generate_user_characteristics(self) -> str:
        """生成用户特征描述"""
        characteristics = [
            "基于系统架构分析，主要用户群体包括：",
            "",
            "1. **系统用户**: 使用系统核心功能的终端用户",
            "2. **API用户**: 通过API接口与系统交互的第三方系统或应用",
            "3. **管理员**: 负责系统维护和管理的用户",
            "",
            "具体用户权限和角色请参考相关业务规则部分。"
        ]

        return "\n".join(characteristics)

    def _generate_operating_environment(self) -> str:
        """生成运行环境描述"""
        project_info = self.srs_data["project_info"]
        language = project_info.get("language", "")
        frameworks = project_info.get("frameworks", [])

        environment = [
            "**技术环境要求：**",
            f"- 编程语言: {language}",
        ]

        if frameworks:
            environment.append(f"- 主要框架: {', '.join(frameworks)}")

        # 基于常见配置推断环境要求
        if "Node.js" in language or any("Express" in f for f in frameworks):
            environment.extend([
                "- 运行时: Node.js",
                "- 包管理: npm/yarn"
            ])
        elif language == "Python":
            environment.extend([
                "- 运行时: Python 3.x",
                "- 包管理: pip"
            ])
        elif language == "Java":
            environment.extend([
                "- 运行时: Java Runtime Environment",
                "- 构建工具: Maven/Gradle"
            ])

        environment.extend([
            "",
            "**部署环境：**",
            "- 支持容器化部署",
            "- 需要数据库环境支持",
            "- 需要网络连接支持"
        ])

        return "\n".join(environment)

    def _generate_design_constraints(self) -> str:
        """生成设计和实现约束"""
        constraints = [
            "基于代码分析，系统遵循以下约束：",
            "",
            "1. **技术约束**: 必须使用当前检测到的技术栈和框架",
            "2. **数据约束**: 必须兼容现有数据库结构和数据格式",
            "3. **接口约束**: 必须保持现有API接口的兼容性",
            "4. **性能约束**: 需要满足现有系统的性能要求",
            "5. **安全约束**: 必须遵循现有的安全机制和认证方式"
        ]

        return "\n".join(constraints)

    def _generate_functional_requirements(self) -> str:
        """生成功能需求"""
        requirements = []

        # 基于API端点生成功能需求
        api_data = self.srs_data["api_analysis"]
        endpoints = api_data.get("endpoints", [])

        if endpoints:
            # 按模块分组
            modules = {}
            for endpoint in endpoints:
                path = endpoint.get("path", "")
                module_name = path.split("/")[1] if "/" in path and len(path.split("/")) > 1 else "root"
                if module_name not in modules:
                    modules[module_name] = []
                modules[module_name].append(endpoint)

            req_counter = 1
            for module, module_endpoints in modules.items():
                requirements.append(f"### {req_counter}. {module.title()}模块功能需求")
                requirements.append("")

                # 为主要API端点生成需求
                for i, endpoint in enumerate(module_endpoints[:5]):  # 限制每个模块最多5个需求
                    method = endpoint.get("method", "")
                    path = endpoint.get("path", "")
                    description = endpoint.get("description", "")

                    req_id = f"FR-{module.upper():.3}-{i+1:03d}"
                    requirements.append(f"**{req_id}: {method} {path}**")
                    requirements.append(f"- **描述**: {description or f'提供{method}操作处理{path}请求'}")
                    requirements.append(f"- **触发器**: 客户端发送{method}请求到{path}端点")
                    requirements.append(f"- **前置条件**: 系统正常运行，相关服务可用")
                    requirements.append(f"- **后置条件**: 返回相应的处理结果和数据")
                    requirements.append("")

                req_counter += 1

        # 基于业务规则生成功能需求
        business_rules = self.srs_data["business_rules"]
        if business_rules:
            requirements.append(f"### {req_counter}. 业务规则需求")
            requirements.append("")

            rule_types = {}
            for rule in business_rules:
                rule_type = rule["rule_type"]
                if rule_type not in rule_types:
                    rule_types[rule_type] = []
                rule_types[rule_type].append(rule)

            for rule_type, rules in rule_types.items():
                for i, rule in enumerate(rules[:3]):  # 每种类型最多3个规则
                    req_id = f"FR-RULE-{rule_type.upper():.3}-{i+1:03d}"
                    requirements.append(f"**{req_id}: {rule['name']}**")
                    requirements.append(f"- **描述**: {rule['description'][:100]}...")
                    requirements.append(f"- **位置**: {rule['location']}")
                    requirements.append("")

        if not requirements:
            return "基于代码分析，系统主要提供数据处理和API接口功能。具体功能需求请参考API接口部分。"

        return "\n".join(requirements)

    def _generate_ui_requirements(self) -> str:
        """生成用户界面需求"""
        ui_requirements = [
            "基于代码分析，系统可能包含以下界面组件：",
            "",
            "1. **API接口界面**: 主要通过RESTful API提供服务",
            "2. **管理界面**: 可能包含系统管理和监控功能",
            "3. **响应式设计**: 支持不同设备和屏幕尺寸",
            "",
            "注意：具体的UI界面需要进一步分析前端代码或查看设计文档。"
        ]

        return "\n".join(ui_requirements)

    def _generate_software_interfaces(self) -> str:
        """生成软件接口需求"""
        interfaces = []

        # 内部API接口
        api_data = self.srs_data["api_analysis"]
        endpoints = api_data.get("endpoints", [])

        if endpoints:
            interfaces.append("#### 内部API接口")
            interfaces.append("")
            interfaces.append("| 模块 | 端点 | 方法 | 功能描述 |")
            interfaces.append("|------|------|------|----------|")

            # 按模块分组显示
            modules = {}
            for endpoint in endpoints:
                path = endpoint.get("path", "")
                module_name = path.split("/")[1] if "/" in path and len(path.split("/")) > 1 else "root"
                if module_name not in modules:
                    modules[module_name] = []
                modules[module_name].append(endpoint)

            for module, module_endpoints in modules.items():
                for endpoint in module_endpoints[:5]:  # 限制显示数量
                    path = endpoint.get("path", "")
                    method = endpoint.get("method", "")
                    description = endpoint.get("description", f"{method}操作")
                    interfaces.append(f"| {module} | `{path}` | {method} | {description} |")

            interfaces.append("")

        # 外部API依赖
        external_apis = api_data.get("external_apis", [])
        if external_apis:
            interfaces.append("#### 外部API依赖")
            interfaces.append("")
            interfaces.append("| 服务域名 | 基础URL | 用途 |")
            interfaces.append("|----------|---------|------|")

            for api in external_apis:
                domain = api.get("domain", "")
                base_url = api.get("base_url", "")
                purpose = api.get("purpose", "")
                interfaces.append(f"| {domain} | `{base_url}` | {purpose} |")

            interfaces.append("")

        if not interfaces:
            return "基于代码分析，系统主要通过API接口提供服务。详细接口信息请参考API分析结果。"

        return "\n".join(interfaces)

    def _generate_performance_requirements(self) -> str:
        """生成性能需求"""
        performance = [
            "基于代码分析和架构模式，系统可能需要满足以下性能要求：",
            "",
            "1. **响应时间**: API接口响应时间应在合理范围内",
            "2. **并发处理**: 支持多用户同时访问",
            "3. **数据处理**: 高效处理数据库查询和数据操作",
            "4. **资源使用**: 合理使用系统资源",
            "",
            "注意：具体的性能指标需要通过性能测试确定。"
        ]

        return "\n".join(performance)

    def _generate_security_requirements(self) -> str:
        """生成安全性需求"""
        security = [
            "基于代码分析，系统应满足以下安全要求：",
            "",
            "1. **身份认证**: 用户访问系统需要进行身份验证",
            "2. **权限控制**: 不同用户应具有不同的访问权限",
            "3. **数据保护**: 敏感数据需要加密存储和传输",
            "4. **输入验证**: 对用户输入进行有效性和安全性验证",
            "5. **日志审计**: 记录关键操作的审计日志",
            "",
            "注意：具体的安全机制需要根据代码实现进一步确认。"
        ]

        return "\n".join(security)

    def _generate_reliability_requirements(self) -> str:
        """生成可靠性需求"""
        reliability = [
            "系统应满足以下可靠性要求：",
            "",
            "1. **错误处理**: 具备完善的错误处理和恢复机制",
            "2. **数据一致性**: 保证数据操作的一致性和完整性",
            "3. **系统稳定性**: 在正常负载下稳定运行",
            "4. **故障恢复**: 具备故障检测和恢复能力",
            "5. **备份恢复**: 重要数据需要定期备份"
        ]

        return "\n".join(reliability)

    def _generate_maintainability_requirements(self) -> str:
        """生成可维护性需求"""
        maintainability = [
            "系统应满足以下可维护性要求：",
            "",
            "1. **代码规范**: 遵循良好的编码规范和约定",
            "2. **文档完整**: 提供完整的API文档和使用说明",
            "3. **模块化设计**: 采用模块化架构，便于维护和扩展",
            "4. **测试覆盖**: 具备充足的测试用例",
            "5. **监控日志**: 提供完善的监控和日志机制"
        ]

        return "\n".join(maintainability)

    def _generate_data_requirements(self) -> str:
        """生成数据需求"""
        data_requirements = []

        # 数据字典
        db_data = self.srs_data["database_analysis"]
        if db_data:
            data_requirements.append("### 6.1 数据字典")
            data_requirements.append("")

            for table_name, table_info in db_data.items():
                data_requirements.append(f"#### 表: {table_name}")
                data_requirements.append("")
                data_requirements.append("| 字段名 | 数据类型 | 可空 | 主键 | 外键 | 描述 |")
                data_requirements.append("|--------|----------|------|------|------|------|")

                columns = table_info.get("columns", [])
                for column in columns:
                    name = column.get("name", "")
                    data_type = column.get("data_type", "")
                    nullable = "是" if column.get("is_nullable", True) else "否"
                    primary_key = "是" if column.get("is_primary_key", False) else "否"
                    foreign_key = "是" if column.get("is_foreign_key", False) else "否"

                    data_requirements.append(f"| {name} | {data_type} | {nullable} | {primary_key} | {foreign_key} |  |")

                data_requirements.append("")

        if not db_data:
            data_requirements.append("基于代码分析，系统包含业务数据管理功能。具体的数据结构请参考数据库分析结果。")

        return "\n".join(data_requirements)

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="SRS模板生成工具")
    parser.add_argument("--analysis", "-a", required=True, help="分析结果目录")
    parser.add_argument("--output", "-o", default="./SRS_DOCUMENT.md", help="SRS文档输出路径")

    args = parser.parse_args()

    generator = SRSTemplateGenerator()
    generator.load_analysis_results(args.analysis)
    generator.generate_srs_document(args.output)

    print(f"SRS文档已生成: {args.output}")

if __name__ == "__main__":
    main()