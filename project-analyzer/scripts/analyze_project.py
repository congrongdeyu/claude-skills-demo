#!/usr/bin/env python3
"""
Project Analysis Script
Main analysis script for understanding project structure and characteristics
"""

import os
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

class ProjectAnalyzer:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.analysis_result = {}

    def detect_project_type(self) -> str:
        """Detect project type based on file structure"""
        indicators = {
            "frontend": ["package.json", "public/", "src/", "index.html", "webpack.config.js"],
            "backend": ["requirements.txt", "pom.xml", "build.gradle", "go.mod", "Cargo.toml"],
            "fullstack": ["package.json", "requirements.txt", "server/", "client/"],
            "mobile": ["ios/", "android/", "lib/", "pubspec.yaml", "package.json"],
            "desktop": ["CMakeLists.txt", ".pro", "Form1.cs", "MainWindow.java"]
        }

        for project_type, files in indicators.items():
            matches = sum(1 for f in files if (self.project_path / f).exists())
            if matches >= 2:
                return project_type

        return "unknown"

    def get_git_activity(self) -> Dict:
        """Analyze git activity if available"""
        git_dir = self.project_path / ".git"
        if not git_dir.exists():
            return {"status": "无git历史记录"}

        try:
            # Get last commit date
            result = subprocess.run(
                ["git", "log", "-1", "--format=%ci"],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode != 0:
                return {"status": "git命令错误"}

            last_commit = result.stdout.strip()

            # Get commit count in last year
            result = subprocess.run(
                ["git", "log", "--since='1 year ago'", "--oneline"],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=10
            )

            commit_count = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0

            return {
                "status": "成功",
                "last_commit": last_commit,
                "commits_last_year": commit_count
            }

        except Exception as e:
            return {"status": "错误", "message": str(e)}

    def analyze_directory_structure(self) -> Dict:
        """Analyze project directory structure"""
        structure = {}

        for item in self.project_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                structure[item.name] = {
                    "type": "directory",
                    "purpose": self._infer_directory_purpose(item.name)
                }
            elif item.is_file() and not item.name.startswith('.'):
                structure[item.name] = {
                    "type": "file",
                    "purpose": self._infer_file_purpose(item.name)
                }

        return structure

    def _infer_directory_purpose(self, dir_name: str) -> str:
        """Infer the purpose of a directory based on its name"""
        purposes = {
            "src": "源代码",
            "lib": "库代码",
            "docs": "项目文档",
            "tests": "测试文件",
            "test": "测试文件",
            "spec": "测试规范",
            "examples": "示例代码",
            "samples": "样本代码",
            "scripts": "构建/工具脚本",
            "tools": "开发工具",
            "config": "配置文件",
            "assets": "静态资源 (图片、字体)",
            "public": "公共静态文件",
            "build": "构建输出",
            "dist": "分发文件",
            "node_modules": "Node.js 依赖",
            "vendor": "第三方依赖"
        }
        return purposes.get(dir_name, f"目录: {dir_name}")

    def _infer_file_purpose(self, file_name: str) -> str:
        """Infer the purpose of a file based on its name"""
        purposes = {
            "README.md": "项目文档",
            "LICENSE": "许可证信息",
            "package.json": "Node.js 依赖",
            "requirements.txt": "Python 依赖",
            "Dockerfile": "Docker 配置",
            "docker-compose.yml": "Docker compose 配置",
            ".gitignore": "Git 忽略规则",
            ".env.example": "环境变量模板"
        }
        return purposes.get(file_name, f"文件: {file_name}")

    def generate_full_analysis(self) -> Dict:
        """Generate comprehensive project analysis"""
        return {
            "project_type": self.detect_project_type(),
            "git_activity": self.get_git_activity(),
            "directory_structure": self.analyze_directory_structure(),
            "project_path": str(self.project_path)
        }

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python analyze_project.py <project_path>")
        sys.exit(1)

    analyzer = ProjectAnalyzer(sys.argv[1])
    result = analyzer.generate_full_analysis()
    print(json.dumps(result, indent=2))