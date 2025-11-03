#!/usr/bin/env python3
"""
项目结构分析脚本
用于分析GitHub项目或本地项目的结构，提取技术栈信息
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Any

class ProjectStructureAnalyzer:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.analysis_result = {
            "project_info": {},
            "tech_stack": {},
            "directory_structure": {},
            "key_files": [],
            "dependencies": {},
            "build_config": {}
        }

    def analyze(self) -> Dict[str, Any]:
        """执行完整的项目结构分析"""
        if not self.project_path.exists():
            raise FileNotFoundError(f"项目路径不存在: {self.project_path}")

        self._extract_project_info()
        self._detect_tech_stack()
        self._analyze_directory_structure()
        self._identify_key_files()
        self._extract_dependencies()
        self._analyze_build_config()

        return self.analysis_result

    def _extract_project_info(self):
        """提取项目基本信息"""
        # 尝试从package.json读取项目信息
        package_json = self.project_path / "package.json"
        if package_json.exists():
            with open(package_json, 'r', encoding='utf-8') as f:
                package_data = json.load(f)
                self.analysis_result["project_info"] = {
                    "name": package_data.get("name", "Unknown"),
                    "version": package_data.get("version", "0.0.0"),
                    "description": package_data.get("description", ""),
                    "author": package_data.get("author", ""),
                    "license": package_data.get("license", "")
                }

        # 尝试从其他配置文件读取信息
        self._try_read_project_metadata()

    def _detect_tech_stack(self):
        """检测技术栈"""
        tech_stack = {
            "frontend": [],
            "backend": [],
            "database": [],
            "testing": [],
            "build_tools": [],
            "deployment": []
        }

        # 检测前端框架
        frontend_indicators = {
            "react": ["package.json", "src/App.jsx", "src/App.tsx", "public/index.html"],
            "vue": ["package.json", "src/App.vue", "src/main.js", "vue.config.js"],
            "angular": ["package.json", "src/app/app.module.ts", "angular.json"],
            "svelte": ["package.json", "src/App.svelte", "svelte.config.js"]
        }

        for framework, files in frontend_indicators.items():
            for file in files:
                if (self.project_path / file).exists():
                    tech_stack["frontend"].append(framework)
                    break

        # 检测后端框架
        backend_indicators = {
            "express": ["package.json", "server.js", "app.js"],
            "fastapi": ["requirements.txt", "main.py", "app.py"],
            "django": ["requirements.txt", "manage.py", "settings.py"],
            "spring-boot": ["pom.xml", "build.gradle", "src/main/java"],
            "flask": ["requirements.txt", "app.py", "run.py"]
        }

        for framework, files in backend_indicators.items():
            for file in files:
                if (self.project_path / file).exists():
                    tech_stack["backend"].append(framework)
                    break

        # 检测数据库
        db_indicators = {
            "mysql": ["requirements.txt", "package.json", "docker-compose.yml"],
            "postgresql": ["requirements.txt", "package.json", "docker-compose.yml"],
            "mongodb": ["requirements.txt", "package.json", "docker-compose.yml"],
            "sqlite": ["requirements.txt", "*.db", "*.sqlite"]
        }

        for db, files in db_indicators.items():
            for file in files:
                if (self.project_path / file).exists():
                    tech_stack["database"].append(db)
                    break

        self.analysis_result["tech_stack"] = tech_stack

    def _analyze_directory_structure(self):
        """分析目录结构"""
        structure = {}

        for root, dirs, files in os.walk(self.project_path):
            # 忽略隐藏目录和常见的不重要目录
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'target', 'build']]

            rel_path = os.path.relpath(root, self.project_path)
            if rel_path == '.':
                rel_path = 'root'

            structure[rel_path] = {
                "subdirectories": dirs,
                "files": [f for f in files if not f.startswith('.')],
                "file_count": len([f for f in files if not f.startswith('.')]),
                "directory_count": len(dirs)
            }

        self.analysis_result["directory_structure"] = structure

    def _identify_key_files(self):
        """识别关键文件"""
        key_files = []

        # 配置文件
        config_patterns = [
            "package.json", "requirements.txt", "pom.xml", "build.gradle",
            "docker-compose.yml", "Dockerfile", ".env.example", ".gitignore",
            "tsconfig.json", "webpack.config.js", "vite.config.js", "babel.config.js"
        ]

        # 主要源码文件
        source_patterns = [
            "src/index.js", "src/App.jsx", "src/App.tsx", "src/main.js",
            "app.js", "server.js", "main.py", "app.py", "index.js", "index.html"
        ]

        # 测试文件
        test_patterns = [
            "jest.config.js", "pytest.ini", "test.js", "tests/", "__tests__/"
        ]

        all_patterns = config_patterns + source_patterns + test_patterns

        for pattern in all_patterns:
            if pattern.endswith('/'):
                # 目录模式
                dir_name = pattern.rstrip('/')
                dir_path = self.project_path / dir_name
                if dir_path.exists() and dir_path.is_dir():
                    key_files.append({
                        "type": "directory",
                        "path": pattern,
                        "description": self._get_directory_description(dir_name)
                    })
            else:
                # 文件模式
                file_path = self.project_path / pattern
                if file_path.exists():
                    key_files.append({
                        "type": "file",
                        "path": pattern,
                        "description": self._get_file_description(pattern)
                    })

        self.analysis_result["key_files"] = key_files

    def _extract_dependencies(self):
        """提取依赖信息"""
        dependencies = {}

        # 从package.json提取依赖
        package_json = self.project_path / "package.json"
        if package_json.exists():
            with open(package_json, 'r', encoding='utf-8') as f:
                package_data = json.load(f)
                dependencies["npm"] = {
                    "dependencies": package_data.get("dependencies", {}),
                    "devDependencies": package_data.get("devDependencies", {})
                }

        # 从requirements.txt提取依赖
        requirements_txt = self.project_path / "requirements.txt"
        if requirements_txt.exists():
            with open(requirements_txt, 'r', encoding='utf-8') as f:
                pip_deps = []
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        pip_deps.append(line)
                dependencies["pip"] = {"requirements": pip_deps}

        self.analysis_result["dependencies"] = dependencies

    def _analyze_build_config(self):
        """分析构建配置"""
        build_config = {}

        # Docker配置
        docker_compose = self.project_path / "docker-compose.yml"
        if docker_compose.exists():
            build_config["docker"] = "Docker Compose配置存在"

        dockerfile = self.project_path / "Dockerfile"
        if dockerfile.exists():
            build_config["dockerfile"] = "Dockerfile存在"

        # CI/CD配置
        ci_files = [".github/workflows", ".gitlab-ci.yml", "Jenkinsfile"]
        for ci_file in ci_files:
            if (self.project_path / ci_file).exists():
                build_config["ci_cd"] = f"CI/CD配置存在: {ci_file}"

        self.analysis_result["build_config"] = build_config

    def _try_read_project_metadata(self):
        """尝试从各种配置文件读取项目元数据"""
        # 这里可以扩展读取更多配置文件
        pass

    def _get_file_description(self, filename: str) -> str:
        """获取文件描述"""
        descriptions = {
            "package.json": "Node.js项目配置文件",
            "requirements.txt": "Python依赖列表",
            "pom.xml": "Maven项目配置",
            "build.gradle": "Gradle构建配置",
            "docker-compose.yml": "Docker Compose配置",
            "Dockerfile": "Docker镜像构建文件",
            "tsconfig.json": "TypeScript配置",
            "webpack.config.js": "Webpack打包配置",
            "vite.config.js": "Vite构建配置",
            ".gitignore": "Git忽略文件配置",
            ".env.example": "环境变量示例"
        }
        return descriptions.get(filename, "项目文件")

    def _get_directory_description(self, dirname: str) -> str:
        """获取目录描述"""
        descriptions = {
            "src": "源代码目录",
            "public": "静态资源目录",
            "tests": "测试文件目录",
            "__tests__": "测试文件目录",
            "docs": "文档目录",
            "build": "构建输出目录",
            "dist": "分发目录"
        }
        return descriptions.get(dirname, "项目目录")

def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description="分析项目结构")
    parser.add_argument("project_path", help="项目路径")
    parser.add_argument("--output", "-o", help="输出JSON文件路径")

    args = parser.parse_args()

    analyzer = ProjectStructureAnalyzer(args.project_path)
    result = analyzer.analyze()

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"分析结果已保存到: {args.output}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()