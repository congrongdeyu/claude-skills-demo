#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
代码结构分析脚本
分析项目架构、业务逻辑和功能模块
"""

import os
import re
import json
import sys
from typing import Dict, List, Optional, Set, Tuple

# 设置标准输出编码为UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
from dataclasses import dataclass, field
from pathlib import Path
from collections import defaultdict

@dataclass
class Function:
    name: str
    file_path: str
    line_number: int
    complexity: int = 1
    is_public: bool = True
    parameters: List[str] = field(default_factory=list)
    return_type: Optional[str] = None
    description: Optional[str] = None

@dataclass
class Class:
    name: str
    file_path: str
    line_number: int
    methods: List[Function] = field(default_factory=list)
    inheritance: List[str] = field(default_factory=list)
    attributes: List[str] = field(default_factory=list)
    is_service: bool = False
    is_controller: bool = False
    is_model: bool = False

@dataclass
class Module:
    name: str
    file_path: str
    functions: List[Function] = field(default_factory=list)
    classes: List[Class] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)

@dataclass
class BusinessRule:
    name: str
    description: str
    location: str
    rule_type: str  # validation, calculation, authorization, etc.
    conditions: List[str] = field(default_factory=list)

class CodeStructureAnalyzer:
    def __init__(self):
        self.modules: Dict[str, Module] = {}
        self.business_rules: List[BusinessRule] = []
        self.project_info: Dict = {}

    def analyze_project(self, project_path: str) -> None:
        """分析整个项目结构"""
        project_path = Path(project_path)

        # 分析项目基本信息
        self._analyze_project_info(project_path)

        # 扫描代码文件
        self._scan_code_files(project_path)

        # 分析业务规则
        self._extract_business_rules()

        # 分析依赖关系
        self._analyze_dependencies()

    def _analyze_project_info(self, project_path: Path) -> None:
        """分析项目基本信息"""
        self.project_info = {
            "name": project_path.name,
            "path": str(project_path),
            "language": self._detect_primary_language(project_path),
            "frameworks": self._detect_frameworks(project_path),
            "architecture": self._detect_architecture_pattern(project_path)
        }

    def _detect_primary_language(self, project_path: Path) -> str:
        """检测主要编程语言"""
        language_counts = {
            'javascript': len(list(project_path.rglob("*.js"))),
            'typescript': len(list(project_path.rglob("*.ts"))),
            'python': len(list(project_path.rglob("*.py"))),
            'java': len(list(project_path.rglob("*.java"))),
            'go': len(list(project_path.rglob("*.go"))),
            'csharp': len(list(project_path.rglob("*.cs"))),
            'php': len(list(project_path.rglob("*.php"))),
            'ruby': len(list(project_path.rglob("*.rb"))),
        }

        if not any(language_counts.values()):
            return "unknown"

        return max(language_counts, key=language_counts.get)

    def _detect_frameworks(self, project_path: Path) -> List[str]:
        """检测使用的框架"""
        frameworks = []

        # 检查 package.json (Node.js)
        package_json = project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json, 'r') as f:
                    deps = json.load(f).get('dependencies', {})
                    dev_deps = json.load(f).get('devDependencies', {})
                    all_deps = {**deps, **dev_deps}

                    if any(framework in all_deps for framework in ['express', 'express.js']):
                        frameworks.append('Express.js')
                    if any(framework in all_deps for framework in ['react', 'react.js']):
                        frameworks.append('React')
                    if any(framework in all_deps for framework in ['vue', 'vue.js']):
                        frameworks.append('Vue.js')
                    if any(framework in all_deps for framework in ['angular']):
                        frameworks.append('Angular')
                    if any(framework in all_deps for framework in ['fastify']):
                        frameworks.append('Fastify')
            except:
                pass

        # 检查 requirements.txt (Python)
        requirements_txt = project_path / "requirements.txt"
        if requirements_txt.exists():
            try:
                with open(requirements_txt, 'r') as f:
                    content = f.read()
                    if 'django' in content.lower():
                        frameworks.append('Django')
                    if 'flask' in content.lower():
                        frameworks.append('Flask')
                    if 'fastapi' in content.lower():
                        frameworks.append('FastAPI')
            except:
                pass

        # 检查 pom.xml (Java)
        pom_xml = project_path / "pom.xml"
        if pom_xml.exists():
            frameworks.append('Maven')
            try:
                with open(pom_xml, 'r') as f:
                    content = f.read()
                    if 'spring-boot' in content.lower():
                        frameworks.append('Spring Boot')
            except:
                pass

        return frameworks

    def _detect_architecture_pattern(self, project_path: Path) -> str:
        """检测架构模式"""
        directories = [d.name.lower() for d in project_path.iterdir() if d.is_dir()]

        if 'controllers' in directories or 'handlers' in directories:
            if 'services' in directories:
                if 'repositories' in directories or 'dao' in directories:
                    return "MVC/MVVM with Repository Pattern"
                return "MVC/MVVM"
            return "Controller-based"

        if 'services' in directories:
            return "Service-oriented"

        if 'components' in directories and 'pages' in directories:
            return "Component-based (likely frontend)"

        if 'src' in directories:
            return "Standard src layout"

        return "Unknown/Custom"

    def _scan_code_files(self, project_path: Path) -> None:
        """扫描代码文件"""
        # 根据主要语言选择文件扩展名
        lang = self.project_info.get('language', '')

        if lang in ['javascript', 'typescript']:
            code_files = list(project_path.rglob("*.js")) + list(project_path.rglob("*.ts"))
            self._scan_js_ts_files(code_files, project_path)
        elif lang == 'python':
            code_files = list(project_path.rglob("*.py"))
            self._scan_python_files(code_files, project_path)
        elif lang == 'java':
            code_files = list(project_path.rglob("*.java"))
            self._scan_java_files(code_files, project_path)
        elif lang == 'go':
            code_files = list(project_path.rglob("*.go"))
            self._scan_go_files(code_files, project_path)

    def _scan_js_ts_files(self, files: List[Path], project_path: Path) -> None:
        """扫描JavaScript/TypeScript文件"""
        for file_path in files:
            if any(skip in str(file_path) for skip in ['node_modules', 'dist', 'build', '.git']):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                module = Module(
                    name=str(file_path.relative_to(project_path)),
                    file_path=str(file_path)
                )

                # 分析导入
                import_pattern = r'import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]'
                module.imports = re.findall(import_pattern, content)

                # 分析类
                class_pattern = r'(?:export\s+)?(?:abstract\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?'
                for match in re.finditer(class_pattern, content):
                    class_name = match.group(1)
                    parent_class = match.group(2)

                    class_obj = Class(
                        name=class_name,
                        file_path=str(file_path),
                        line_number=content[:match.start()].count('\n') + 1,
                        inheritance=[parent_class] if parent_class else []
                    )

                    # 识别类类型
                    if 'Controller' in class_name:
                        class_obj.is_controller = True
                    elif 'Service' in class_name:
                        class_obj.is_service = True
                    elif 'Model' in class_name:
                        class_obj.is_model = True

                    module.classes.append(class_obj)

                # 分析函数
                function_pattern = r'(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\(([^)]*)\)'
                for match in re.finditer(function_pattern, content):
                    func_name = match.group(1)
                    params = [p.strip() for p in match.group(2).split(',') if p.strip()] if match.group(2) else []

                    func = Function(
                        name=func_name,
                        file_path=str(file_path),
                        line_number=content[:match.start()].count('\n') + 1,
                        parameters=params
                    )
                    module.functions.append(func)

                self.modules[module.name] = module

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    def _scan_python_files(self, files: List[Path], project_path: Path) -> None:
        """扫描Python文件"""
        for file_path in files:
            if any(skip in str(file_path) for skip in ['venv', '__pycache__', 'site-packages', '.git']):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                module = Module(
                    name=str(file_path.relative_to(project_path)),
                    file_path=str(file_path)
                )

                # 分析导入
                import_patterns = [
                    r'import\s+(\w+)',
                    r'from\s+(\w+)\s+import',
                ]
                for pattern in import_patterns:
                    module.imports.extend(re.findall(pattern, content))

                # 分析类
                class_pattern = r'class\s+(\w+)(?:\s*\(\s*([^)]+)\s*\))?'
                for match in re.finditer(class_pattern, content):
                    class_name = match.group(1)
                    parent_classes = match.group(2).split(',') if match.group(2) else []
                    parent_classes = [p.strip() for p in parent_classes if p.strip()]

                    class_obj = Class(
                        name=class_name,
                        file_path=str(file_path),
                        line_number=content[:match.start()].count('\n') + 1,
                        inheritance=parent_classes
                    )

                    # 识别类类型
                    if 'View' in class_name or 'Controller' in class_name:
                        class_obj.is_controller = True
                    elif 'Service' in class_name or 'Manager' in class_name:
                        class_obj.is_service = True
                    elif 'Model' in class_name:
                        class_obj.is_model = True

                    module.classes.append(class_obj)

                # 分析函数
                function_pattern = r'def\s+(\w+)\s*\(([^)]*)\):'
                for match in re.finditer(function_pattern, content):
                    func_name = match.group(1)
                    params = [p.strip() for p in match.group(2).split(',') if p.strip()] if match.group(2) else []

                    func = Function(
                        name=func_name,
                        file_path=str(file_path),
                        line_number=content[:match.start()].count('\n') + 1,
                        parameters=params,
                        is_public=not func_name.startswith('_')
                    )
                    module.functions.append(func)

                self.modules[module.name] = module

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    def _scan_java_files(self, files: List[Path], project_path: Path) -> None:
        """扫描Java文件"""
        for file_path in files:
            if any(skip in str(file_path) for skip in ['target', 'build', '.git']):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                module = Module(
                    name=str(file_path.relative_to(project_path)),
                    file_path=str(file_path)
                )

                # 分析导入
                import_pattern = r'import\s+([\w.]+);'
                module.imports = re.findall(import_pattern, content)

                # 分析类
                class_pattern = r'(?:public\s+)?(?:abstract\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?(?:\s+implements\s+([^{]+))?'
                for match in re.finditer(class_pattern, content):
                    class_name = match.group(1)
                    parent_class = match.group(2)
                    interfaces = match.group(3).split(',') if match.group(3) else []

                    class_obj = Class(
                        name=class_name,
                        file_path=str(file_path),
                        line_number=content[:match.start()].count('\n') + 1,
                        inheritance=([parent_class] if parent_class else []) + [i.strip() for i in interfaces if i.strip()]
                    )

                    # 识别类类型
                    if 'Controller' in class_name:
                        class_obj.is_controller = True
                    elif 'Service' in class_name:
                        class_obj.is_service = True
                    elif 'Entity' in class_name or 'Model' in class_name:
                        class_obj.is_model = True

                    module.classes.append(class_obj)

                # 分析方法
                method_pattern = r'(?:public|private|protected)?\s*(?:static\s+)?(?:final\s+)?(?:\w+\s+)?(\w+)\s*\(([^)]*)\)\s*(?:throws\s+[\w,\s]+)?\s*\{'
                for match in re.finditer(method_pattern, content):
                    method_name = match.group(1)
                    params = [p.strip() for p in match.group(2).split(',') if p.strip()] if match.group(2) else []

                    func = Function(
                        name=method_name,
                        file_path=str(file_path),
                        line_number=content[:match.start()].count('\n') + 1,
                        parameters=params,
                        is_public='public' in content[match.start()-20:match.start()]
                    )
                    module.functions.append(func)

                self.modules[module.name] = module

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    def _scan_go_files(self, files: List[Path], project_path: Path) -> None:
        """扫描Go文件"""
        for file_path in files:
            if any(skip in str(file_path) for skip in ['vendor', '.git']):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                module = Module(
                    name=str(file_path.relative_to(project_path)),
                    file_path=str(file_path)
                )

                # 分析导入
                import_pattern = r'"([^"]+)"'
                import_section = re.search(r'import\s*\((.*?)\)', content, re.DOTALL)
                if import_section:
                    module.imports = re.findall(import_pattern, import_section.group(1))
                else:
                    single_imports = re.findall(r'import\s+"([^"]+)"', content)
                    module.imports.extend(single_imports)

                # 分析结构体 (Go的类)
                struct_pattern = r'type\s+(\w+)\s+struct\s*\{([^}]*)\}'
                for match in re.finditer(struct_pattern, content, re.DOTALL):
                    struct_name = match.group(1)
                    struct_body = match.group(2)

                    class_obj = Class(
                        name=struct_name,
                        file_path=str(file_path),
                        line_number=content[:match.start()].count('\n') + 1
                    )

                    # 解析字段
                    field_lines = struct_body.strip().split('\n')
                    for line in field_lines:
                        line = line.strip()
                        if line and not line.startswith('//'):
                            parts = line.split()
                            if len(parts) >= 2:
                                class_obj.attributes.append(parts[0])

                    module.classes.append(class_obj)

                # 分析函数
                func_pattern = r'func\s+(?:\([^)]*\)\s*)?(\w+)\s*\(([^)]*)\)(?:\s*\([^)]*\))?'
                for match in re.finditer(func_pattern, content):
                    func_name = match.group(1)
                    params = [p.strip() for p in match.group(2).split(',') if p.strip()] if match.group(2) else []

                    func = Function(
                        name=func_name,
                        file_path=str(file_path),
                        line_number=content[:match.start()].count('\n') + 1,
                        parameters=params,
                        is_public=func_name[0].isupper() if func_name else True
                    )
                    module.functions.append(func)

                self.modules[module.name] = module

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    def _extract_business_rules(self) -> None:
        """提取业务规则"""
        rule_patterns = [
            # 验证规则
            (r'if\s+.*?(?:length|size|min|max|required|null|empty|email|password)', "validation"),
            # 计算规则
            (r'(?:total|sum|calculate|compute|discount|tax|price)', "calculation"),
            # 授权规则
            (r'(?:role|permission|auth|admin|user|access)', "authorization"),
            # 业务条件
            (r'if\s+.*?\{[^}]*return[^}]*\}', "business_logic"),
        ]

        for module_name, module in self.modules.items():
            try:
                with open(module.file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                for pattern, rule_type in rule_patterns:
                    matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
                    for match in matches:
                        # 获取上下文
                        start = max(0, match.start() - 50)
                        end = min(len(content), match.end() + 50)
                        context = content[start:end].strip()

                        rule = BusinessRule(
                            name=f"{rule_type.title()} Rule",
                            description=context,
                            location=f"{module_name}:{content[:match.start()].count('\n') + 1}",
                            rule_type=rule_type
                        )
                        self.business_rules.append(rule)

            except Exception as e:
                print(f"Error extracting rules from {module_name}: {e}")

    def _analyze_dependencies(self) -> None:
        """分析模块依赖关系"""
        for module_name, module in self.modules.items():
            dependencies = set()
            for import_name in module.imports:
                # 检查是否是项目内部依赖
                for other_module_name, other_module in self.modules.items():
                    if import_name in other_module_name or other_module_name in import_name:
                        dependencies.add(other_module_name)
            module.dependencies = list(dependencies)

    def generate_structure_report(self) -> str:
        """生成结构分析报告"""
        report_lines = ["# 代码结构分析报告\n"]

        # 项目概述
        report_lines.append("## 项目概述\n")
        report_lines.append(f"- **项目名称**: {self.project_info.get('name', 'Unknown')}")
        report_lines.append(f"- **主要语言**: {self.project_info.get('language', 'Unknown')}")
        report_lines.append(f"- **使用框架**: {', '.join(self.project_info.get('frameworks', [])) or 'None'}")
        report_lines.append(f"- **架构模式**: {self.project_info.get('architecture', 'Unknown')}")
        report_lines.append(f"- **模块数量**: {len(self.modules)}")
        report_lines.append("")

        # 功能模块分析
        controllers = []
        services = []
        models = []

        for module in self.modules.values():
            controllers.extend([c for c in module.classes if c.is_controller])
            services.extend([c for c in module.classes if c.is_service])
            models.extend([c for c in module.classes if c.is_model])

        if controllers or services or models:
            report_lines.append("## 架构组件\n")

            if controllers:
                report_lines.append(f"### 控制器 ({len(controllers)})")
                for controller in controllers[:10]:  # 限制显示数量
                    report_lines.append(f"- `{controller.name}` ({Path(controller.file_path).name})")
                report_lines.append("")

            if services:
                report_lines.append(f"### 服务层 ({len(services)})")
                for service in services[:10]:
                    report_lines.append(f"- `{service.name}` ({Path(service.file_path).name})")
                report_lines.append("")

            if models:
                report_lines.append(f"### 数据模型 ({len(models)})")
                for model in models[:10]:
                    report_lines.append(f"- `{model.name}` ({Path(model.file_path).name})")
                report_lines.append("")

        # 业务规则
        if self.business_rules:
            report_lines.append("## 业务规则分析\n")

            # 按类型分组
            rules_by_type = defaultdict(list)
            for rule in self.business_rules:
                rules_by_type[rule.rule_type].append(rule)

            for rule_type, rules in rules_by_type.items():
                report_lines.append(f"### {rule_type.title()} 规则 ({len(rules)})")
                for rule in rules[:5]:  # 限制显示数量
                    report_lines.append(f"- **{rule.name}**: {rule.description[:100]}...")
                    report_lines.append(f"  - 位置: `{rule.location}`")
                report_lines.append("")

        return "\n".join(report_lines)

    def export_analysis(self, output_dir: str) -> None:
        """导出分析结果"""
        os.makedirs(output_dir, exist_ok=True)

        # 生成结构报告
        report_content = self.generate_structure_report()
        with open(os.path.join(output_dir, "code_structure_analysis.md"), "w", encoding="utf-8") as f:
            f.write(report_content)

        # 生成JSON格式的详细分析
        json_data = {
            "project_info": self.project_info,
            "modules": {
                name: {
                    "file_path": module.file_path,
                    "functions": [
                        {
                            "name": func.name,
                            "line_number": func.line_number,
                            "parameters": func.parameters,
                            "is_public": func.is_public
                        }
                        for func in module.functions
                    ],
                    "classes": [
                        {
                            "name": cls.name,
                            "line_number": cls.line_number,
                            "inheritance": cls.inheritance,
                            "is_controller": cls.is_controller,
                            "is_service": cls.is_service,
                            "is_model": cls.is_model
                        }
                        for cls in module.classes
                    ],
                    "imports": module.imports,
                    "dependencies": module.dependencies
                }
                for name, module in self.modules.items()
            },
            "business_rules": [
                {
                    "name": rule.name,
                    "description": rule.description,
                    "location": rule.location,
                    "rule_type": rule.rule_type
                }
                for rule in self.business_rules
            ]
        }

        with open(os.path.join(output_dir, "code_analysis.json"), "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="代码结构分析工具")
    parser.add_argument("path", help="要分析的项目路径")
    parser.add_argument("--output", "-o", default="./srs_analysis", help="输出目录")

    args = parser.parse_args()

    analyzer = CodeStructureAnalyzer()
    analyzer.analyze_project(args.path)

    if not analyzer.modules:
        print("未发现可分析的代码文件")
        return

    # 导出分析结果
    analyzer.export_analysis(args.output)
    print(f"\n代码结构分析完成！结果已保存到: {args.output}")
    print(f"分析了 {len(analyzer.modules)} 个模块")
    print(f"发现 {len(analyzer.business_rules)} 个业务规则")

if __name__ == "__main__":
    main()