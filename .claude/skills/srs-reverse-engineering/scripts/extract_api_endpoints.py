#!/usr/bin/env python3
"""
API端点提取脚本
用于从项目源码中提取API接口信息
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any

class APIEndpointExtractor:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.api_endpoints = {
            "rest_apis": [],
            "graphql_schemas": [],
            "websocket_endpoints": [],
            "external_apis": []
        }

    def extract(self) -> Dict[str, Any]:
        """提取所有API端点信息"""
        self._scan_source_files()
        self._extract_rest_apis()
        self._extract_graphql_schemas()
        self._extract_websocket_endpoints()
        self._extract_external_api_calls()

        return self.api_endpoints

    def _scan_source_files(self):
        """扫描源码文件"""
        self.source_files = []

        # 常见的源码文件扩展名
        source_extensions = ['.js', '.jsx', '.ts', '.tsx', '.py', '.java', '.go', '.php', '.rb']

        for root, dirs, files in os.walk(self.project_path):
            # 忽略不需要的目录
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'target', 'build', 'dist']]

            for file in files:
                if any(file.endswith(ext) for ext in source_extensions):
                    self.source_files.append(Path(root) / file)

    def _extract_rest_apis(self):
        """提取REST API端点"""
        # Express.js路由模式
        express_patterns = [
            r'app\.(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'router\.(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'@([A-Z]+)\s*\(\s*[\'"]([^\'"]+)[\'"]'  # Spring Boot注解
        ]

        # FastAPI路由模式
        fastapi_patterns = [
            r'@(app\.)?(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'@router\.(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]'
        ]

        # Django URL模式
        django_patterns = [
            r'path\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'url\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r're_path\s*\(\s[r\'"]([^\'"]+)[r\'"]'
        ]

        for file_path in self.source_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    # 检测框架类型并应用相应模式
                    if self._is_express_file(content):
                        self._parse_patterns(content, express_patterns, file_path, "Express")
                    elif self._is_fastapi_file(content):
                        self._parse_patterns(content, fastapi_patterns, file_path, "FastAPI")
                    elif self._is_django_file(content):
                        self._parse_patterns(content, django_patterns, file_path, "Django")
                    else:
                        # 通用模式匹配
                        all_patterns = express_patterns + fastapi_patterns + django_patterns
                        self._parse_patterns(content, all_patterns, file_path, "Unknown")

            except Exception as e:
                print(f"读取文件失败 {file_path}: {e}")

    def _extract_graphql_schemas(self):
        """提取GraphQL模式"""
        graphql_patterns = [
            r'type\s+(\w+)\s*\{',
            r'(?:input|type|interface|union|enum)\s+(\w+)',
            r'(?:query|mutation|subscription)\s*\(\s*\$?(\w+)'
        ]

        for file_path in self.source_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    if 'graphql' in content.lower() or 'gql' in content.lower():
                        schema_info = {
                            "file": str(file_path.relative_to(self.project_path)),
                            "types": [],
                            "queries": [],
                            "mutations": []
                        }

                        for pattern in graphql_patterns:
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            for match in matches:
                                if isinstance(match, tuple):
                                    match = match[0] if match[0] else match[1]

                                if 'type' in pattern.lower() or 'input' in pattern.lower():
                                    schema_info["types"].append(match)
                                elif 'query' in pattern.lower():
                                    schema_info["queries"].append(match)
                                elif 'mutation' in pattern.lower():
                                    schema_info["mutations"].append(match)

                        if schema_info["types"] or schema_info["queries"] or schema_info["mutations"]:
                            self.api_endpoints["graphql_schemas"].append(schema_info)

            except Exception as e:
                print(f"读取GraphQL文件失败 {file_path}: {e}")

    def _extract_websocket_endpoints(self):
        """提取WebSocket端点"""
        websocket_patterns = [
            r'io\.on\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'websocket\.on\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'new\s+WebSocket\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'ws\://([^/]+)(/[^\'"]*)'
        ]

        for file_path in self.source_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    if 'websocket' in content.lower() or 'socket.io' in content.lower():
                        endpoints = []
                        for pattern in websocket_patterns:
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            for match in matches:
                                if isinstance(match, tuple):
                                    endpoint = match[1] if len(match) > 1 else match[0]
                                else:
                                    endpoint = match
                                endpoints.append(endpoint)

                        if endpoints:
                            self.api_endpoints["websocket_endpoints"].append({
                                "file": str(file_path.relative_to(self.project_path)),
                                "endpoints": list(set(endpoints))  # 去重
                            })

            except Exception as e:
                print(f"读取WebSocket文件失败 {file_path}: {e}")

    def _extract_external_api_calls(self):
        """提取外部API调用"""
        external_api_patterns = [
            r'fetch\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'axios\.(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'requests\.(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'httpclient\.(get|post|put|delete)\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'@GetMapping\s*\(\s*[\'"]([^\'"]+)[\'"]',
            r'@PostMapping\s*\(\s*[\'"]([^\'"]+)[\'"]'
        ]

        external_domains = set()

        for file_path in self.source_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    for pattern in external_api_patterns:
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        for match in matches:
                            if isinstance(match, tuple):
                                url = match[1] if len(match) > 1 else match[0]
                            else:
                                url = match

                            # 检查是否为外部URL
                            if url.startswith(('http://', 'https://')):
                                domain = url.split('/')[2]  # 提取域名
                                external_domains.add(domain)

            except Exception as e:
                print(f"读取外部API文件失败 {file_path}: {e}")

        if external_domains:
            self.api_endpoints["external_apis"] = list(external_domains)

    def _is_express_file(self, content: str) -> bool:
        """检测是否为Express文件"""
        return any(keyword in content for keyword in ['require(\'express\')', 'import express', 'app.get', 'app.post', 'router.'])

    def _is_fastapi_file(self, content: str) -> bool:
        """检测是否为FastAPI文件"""
        return any(keyword in content for keyword in ['from fastapi import', 'FastAPI()', '@app.', '@router.'])

    def _is_django_file(self, content: str) -> bool:
        """检测是否为Django文件"""
        return any(keyword in content for keyword in ['from django', 'urlpatterns', 'path(', 'url('])

    def _parse_patterns(self, content: str, patterns: List[str], file_path: Path, framework: str):
        """解析模式并提取API信息"""
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    method = match[0].upper() if match[0] else 'GET'
                    endpoint = match[1] if len(match) > 1 else match[0]
                else:
                    method = 'GET'
                    endpoint = match

                # 清理端点路径
                endpoint = endpoint.strip()

                # 跳过非API路径
                if not self._is_api_endpoint(endpoint):
                    continue

                api_info = {
                    "method": method,
                    "path": endpoint,
                    "file": str(file_path.relative_to(self.project_path)),
                    "framework": framework,
                    "line_number": self._find_line_number(content, endpoint)
                }

                # 避免重复
                if not any(api['path'] == endpoint and api['method'] == method for api in self.api_endpoints["rest_apis"]):
                    self.api_endpoints["rest_apis"].append(api_info)

    def _is_api_endpoint(self, path: str) -> bool:
        """判断是否为API端点"""
        # 常见的API路径前缀
        api_prefixes = ['/api/', '/v1/', '/v2/', '/rest/', '/graphql', '/ws/', '/socket.io/']

        # 检查是否包含API前缀
        for prefix in api_prefixes:
            if path.startswith(prefix):
                return True

        # 检查是否包含常见的HTTP动词
        http_verbs = ['login', 'logout', 'register', 'auth', 'users', 'posts', 'comments', 'products', 'orders']
        for verb in http_verbs:
            if f'/{verb}' in path:
                return True

        return False

    def _find_line_number(self, content: str, search_text: str) -> int:
        """查找文本在文件中的行号"""
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if search_text in line:
                return i
        return 0

def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description="提取API端点")
    parser.add_argument("project_path", help="项目路径")
    parser.add_argument("--output", "-o", help="输出JSON文件路径")

    args = parser.parse_args()

    extractor = APIEndpointExtractor(args.project_path)
    result = extractor.extract()

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"API端点已保存到: {args.output}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()