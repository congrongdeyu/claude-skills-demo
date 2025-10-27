#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API接口自动发现脚本
扫描代码库，自动识别和文档化所有API端点
"""

import os
import re
import json
import sys
from typing import Dict, List, Optional, Tuple

# 设置标准输出编码为UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
from dataclasses import dataclass
from pathlib import Path
from enum import Enum

class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"

@dataclass
class APIEndpoint:
    path: str
    method: HTTPMethod
    description: Optional[str] = None
    controller: Optional[str] = None
    function: Optional[str] = None
    parameters: List[Dict] = None
    request_body: Optional[Dict] = None
    response: Optional[Dict] = None
    status_codes: List[str] = None
    middleware: List[str] = None

    def __post_init__(self):
        if self.parameters is None:
            self.parameters = []
        if self.status_codes is None:
            self.status_codes = []
        if self.middleware is None:
            self.middleware = []

class APIDiscoverer:
    def __init__(self):
        self.endpoints: List[APIEndpoint] = []
        self.external_apis: List[Dict] = []

    def discover_in_project(self, project_path: str) -> None:
        """在项目中发现API"""
        project_path = Path(project_path)

        # 扫描不同类型的文件
        self._scan_nodejs_files(project_path)
        self._scan_python_files(project_path)
        self._scan_java_files(project_path)
        self._scan_go_files(project_path)
        self._scan_openapi_files(project_path)
        self._scan_external_api_calls(project_path)

    def _scan_nodejs_files(self, project_path: Path) -> None:
        """扫描Node.js文件中的API定义"""
        js_ts_files = list(project_path.rglob("*.js")) + list(project_path.rglob("*.ts"))

        # Express.js 路由模式
        express_patterns = [
            # app.get('/path', handler)
            r'\.(get|post|put|delete|patch|use|all)\s*\(\s*[\'"`]([^\'"`]+)[\'"`]\s*,?\s*([^,\)]*)',
            # router.METHOD('/path', handler)
            r'(?:app|router)\.([a-zA-Z]+)\s*\(\s*[\'"`]([^\'"`]+)[\'"`]\s*,?\s*([^,\)]*)',
        ]

        for file_path in js_ts_files:
            if any(skip in str(file_path) for skip in ['node_modules', 'dist', 'build']):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                for pattern in express_patterns:
                    matches = re.finditer(pattern, content, re.MULTILINE)
                    for match in matches:
                        method_str = match.group(1).upper()
                        path = match.group(2)
                        handler = match.group(3).strip()

                        if method_str in [m.value for m in HTTPMethod]:
                            endpoint = APIEndpoint(
                                path=path,
                                method=HTTPMethod(method_str),
                                controller=str(file_path.relative_to(project_path)),
                                function=handler
                            )
                            self.endpoints.append(endpoint)

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    def _scan_python_files(self, project_path: Path) -> None:
        """扫描Python文件中的API定义"""
        py_files = list(project_path.rglob("*.py"))

        # Flask 路由模式
        flask_patterns = [
            # @app.route('/path', methods=['GET', 'POST'])
            r'@(\w+)\.route\s*\(\s*[\'"`]([^\'"`]+)[\'"`](?:\s*,\s*methods=\[([^\]]+)\])?',
            # @bp.route('/path', methods=['GET'])
            r'@(\w+)\.route\s*\(\s*[\'"`]([^\'"`]+)[\'"`](?:\s*,\s*methods=\[([^\]]+)\])?',
        ]

        # FastAPI 路由模式
        fastapi_patterns = [
            r'@(?:app|router)\.(get|post|put|delete|patch)\s*\(\s*[\'"`]([^\'"`]+)[\'"`]',
        ]

        for file_path in py_files:
            if any(skip in str(file_path) for skip in ['venv', '__pycache__', 'site-packages']):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 扫描Flask路由
                for pattern in flask_patterns:
                    matches = re.finditer(pattern, content, re.MULTILINE)
                    for match in matches:
                        path = match.group(2)
                        methods_str = match.group(3) or "['GET']"

                        # 解析methods列表
                        methods = re.findall(r'[\'"]([A-Z]+)[\'"]', methods_str)
                        for method_str in methods:
                            if method_str in [m.value for m in HTTPMethod]:
                                endpoint = APIEndpoint(
                                    path=path,
                                    method=HTTPMethod(method_str),
                                    controller=str(file_path.relative_to(project_path))
                                )
                                self.endpoints.append(endpoint)

                # 扫描FastAPI路由
                for pattern in fastapi_patterns:
                    matches = re.finditer(pattern, content, re.MULTILINE)
                    for match in matches:
                        method_str = match.group(1).upper()
                        path = match.group(2)

                        if method_str in [m.value for m in HTTPMethod]:
                            endpoint = APIEndpoint(
                                path=path,
                                method=HTTPMethod(method_str),
                                controller=str(file_path.relative_to(project_path))
                            )
                            self.endpoints.append(endpoint)

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    def _scan_java_files(self, project_path: Path) -> None:
        """扫描Java文件中的Spring Boot API定义"""
        java_files = list(project_path.rglob("*.java"))

        # Spring Boot 注解模式
        spring_patterns = [
            # @GetMapping("/path")
            r'@(Get|Post|Put|Delete|Patch)Mapping\s*\(\s*[\'"`]([^\'"`]+)[\'"`]',
            # @RequestMapping(path = "/path", method = RequestMethod.GET)
            r'@RequestMapping\s*\(\s*(?:path\s*=\s*)?[\'"`]([^\'"`]+)[\'"`](?:.*?method\s*=\s*RequestMethod\.(\w+))?',
        ]

        for file_path in java_files:
            if any(skip in str(file_path) for skip in ['target', 'build', '.git']):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                for pattern in spring_patterns:
                    matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
                    for match in matches:
                        if match.group(1):  # GetMapping等
                            method_str = match.group(1).upper()
                            path = match.group(2)
                        else:  # RequestMapping
                            method_str = match.group(3) or "GET"
                            path = match.group(1)

                        if method_str in [m.value for m in HTTPMethod]:
                            endpoint = APIEndpoint(
                                path=path,
                                method=HTTPMethod(method_str),
                                controller=str(file_path.relative_to(project_path))
                            )
                            self.endpoints.append(endpoint)

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    def _scan_go_files(self, project_path: Path) -> None:
        """扫描Go文件中的Gin/echo API定义"""
        go_files = list(project_path.rglob("*.go"))

        # Gin 框架模式
        gin_patterns = [
            # r.GET("/path", handler)
            r'\.(GET|POST|PUT|DELETE|PATCH)\s*\(\s*"([^"]+)"\s*,',
            # r.Handle("GET", "/path", handler)
            r'\.Handle\s*\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*,',
        ]

        for file_path in go_files:
            if any(skip in str(file_path) for skip in ['vendor', '.git']):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                for pattern in gin_patterns:
                    matches = re.finditer(pattern, content, re.MULTILINE)
                    for match in matches:
                        if len(match.groups()) == 2:
                            method_str = match.group(1).upper()
                            path = match.group(2)
                        else:
                            method_str = match.group(2).upper()
                            path = match.group(1)

                        if method_str in [m.value for m in HTTPMethod]:
                            endpoint = APIEndpoint(
                                path=path,
                                method=HTTPMethod(method_str),
                                controller=str(file_path.relative_to(project_path))
                            )
                            self.endpoints.append(endpoint)

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    def _scan_openapi_files(self, project_path: Path) -> None:
        """扫描OpenAPI/Swagger规范文件"""
        openapi_files = (
            list(project_path.rglob("openapi.yaml")) +
            list(project_path.rglob("openapi.yml")) +
            list(project_path.rglob("swagger.yaml")) +
            list(project_path.rglob("swagger.yml")) +
            list(project_path.rglob("api.json"))
        )

        for file_path in openapi_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if file_path.suffix == '.json':
                        spec = json.load(f)
                    else:
                        import yaml
                        spec = yaml.safe_load(f)

                self._parse_openapi_spec(spec, str(file_path.relative_to(project_path)))

            except Exception as e:
                print(f"Error processing OpenAPI file {file_path}: {e}")

    def _parse_openapi_spec(self, spec: Dict, source_file: str) -> None:
        """解析OpenAPI规范"""
        paths = spec.get('paths', {})

        for path, path_item in paths.items():
            for method, operation in path_item.items():
                if method.upper() in [m.value for m in HTTPMethod]:
                    endpoint = APIEndpoint(
                        path=path,
                        method=HTTPMethod(method.upper()),
                        description=operation.get('summary', ''),
                        controller=source_file,
                        function=operation.get('operationId', ''),
                        parameters=operation.get('parameters', []),
                        request_body=operation.get('requestBody', {}),
                        response=operation.get('responses', {}),
                    )
                    self.endpoints.append(endpoint)

    def _scan_external_api_calls(self, project_path: Path) -> None:
        """扫描外部API调用"""
        # 外部API调用模式
        external_patterns = [
            # fetch('https://api.example.com/...')
            r'fetch\s*\(\s*[\'"](https?://[^\'"]+)[\'"]',
            # axios.get('https://api.example.com/...')
            r'axios\.(get|post|put|delete|patch)\s*\(\s*[\'"](https?://[^\'"]+)[\'"]',
            # requests.get('https://api.example.com/...')
            r'requests\.(get|post|put|delete|patch)\s*\(\s*[\'"](https?://[^\'"]+)[\'"]',
            # http.Client.get('https://api.example.com/...')
            r'(?:http|HttpClient)\.(get|post|put|delete|patch)\s*\(\s*[\'"](https?://[^\'"]+)[\'"]',
        ]

        code_files = []
        for ext in ['*.js', '*.ts', '*.jsx', '*.tsx', '*.py', '*.java', '*.go', '*.cs']:
            code_files.extend(list(project_path.rglob(ext)))

        for file_path in code_files:
            if any(skip in str(file_path) for skip in ['node_modules', 'vendor', 'venv', 'target', 'build', '.git']):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                for pattern in external_patterns:
                    matches = re.finditer(pattern, content, re.MULTILINE)
                    for match in matches:
                        url = match.group(2) if len(match.groups()) >= 2 else match.group(1)
                        method = match.group(1) if len(match.groups()) >= 2 else 'GET'

                        # 提取域名
                        from urllib.parse import urlparse
                        parsed = urlparse(url)
                        domain = parsed.netloc

                        if domain and domain not in [api.get('domain') for api in self.external_apis]:
                            self.external_apis.append({
                                'domain': domain,
                                'base_url': f"{parsed.scheme}://{domain}",
                                'purpose': f"外部API调用 ({method})",
                                'source_file': str(file_path.relative_to(project_path))
                            })

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    def generate_api_documentation(self) -> str:
        """生成API文档"""
        if not self.endpoints:
            return "# API接口文档\n\n未发现API端点。\n"

        # 按路径分组API
        grouped_apis = {}
        for endpoint in self.endpoints:
            base_path = '/' + endpoint.path.split('/')[1] if '/' in endpoint.path else 'root'
            if base_path not in grouped_apis:
                grouped_apis[base_path] = []
            grouped_apis[base_path].append(endpoint)

        doc_lines = ["# API接口文档\n"]
        doc_lines.append(f"共发现 {len(self.endpoints)} 个API端点\n")

        # 按模块组织
        for module, apis in sorted(grouped_apis.items()):
            doc_lines.append(f"## 模块: {module}\n")

            # API表格
            doc_lines.append("| 方法 | 端点 | 描述 | 控制器 |")
            doc_lines.append("|------|------|------|--------|")

            for api in apis:
                description = api.description or ""
                controller = api.controller.split('/')[-1] if api.controller else ""
                doc_lines.append(f"| {api.method.value} | `{api.path}` | {description} | {controller} |")

            doc_lines.append("")

        # 外部API依赖
        if self.external_apis:
            doc_lines.append("## 外部API依赖\n")
            doc_lines.append("| 域名 | 基础URL | 用途 | 源文件 |")
            doc_lines.append("|------|---------|------|--------|")

            for external_api in self.external_apis:
                doc_lines.append(f"| {external_api['domain']} | `{external_api['base_url']}` | {external_api['purpose']} | {external_api['source_file']} |")

            doc_lines.append("")

        return "\n".join(doc_lines)

    def export_analysis(self, output_dir: str) -> None:
        """导出分析结果"""
        os.makedirs(output_dir, exist_ok=True)

        # 生成API文档
        doc_content = self.generate_api_documentation()
        with open(os.path.join(output_dir, "api_documentation.md"), "w", encoding="utf-8") as f:
            f.write(doc_content)

        # 生成JSON格式的分析结果
        json_data = {
            "total_endpoints": len(self.endpoints),
            "endpoints": [
                {
                    "path": endpoint.path,
                    "method": endpoint.method.value,
                    "description": endpoint.description,
                    "controller": endpoint.controller,
                    "function": endpoint.function,
                    "parameters": endpoint.parameters,
                    "request_body": endpoint.request_body,
                    "response": endpoint.response
                }
                for endpoint in self.endpoints
            ],
            "external_apis": self.external_apis
        }

        with open(os.path.join(output_dir, "api_analysis.json"), "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="API接口自动发现工具")
    parser.add_argument("path", help="要分析的项目路径")
    parser.add_argument("--output", "-o", default="./srs_analysis", help="输出目录")

    args = parser.parse_args()

    discoverer = APIDiscoverer()
    discoverer.discover_in_project(args.path)

    if not discoverer.endpoints and not discoverer.external_apis:
        print("未发现API相关文件")
        return

    # 导出分析结果
    discoverer.export_analysis(args.output)
    print(f"\nAPI分析完成！结果已保存到: {args.output}")
    print(f"发现 {len(discoverer.endpoints)} 个API端点")
    print(f"发现 {len(discoverer.external_apis)} 个外部API依赖")

if __name__ == "__main__":
    main()