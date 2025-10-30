#!/usr/bin/env python3
"""
GitHub项目分析器
支持分析GitHub项目的README、文件结构、依赖等信息
"""

import os
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, Optional

class GitHubAnalyzer:
    def __init__(self):
        self.temp_dir = None

    def clone_or_extract_github_project(self, github_url: str, temp_dir: str = None) -> str:
        """克隆或提取GitHub项目到临时目录"""
        try:
            # 标准化GitHub URL
            github_url = self._normalize_github_url(github_url)

            # 设置临时目录
            if temp_dir is None:
                import tempfile
                self.temp_dir = Path(tempfile.mkdtemp(prefix="github_analysis_"))
            else:
                self.temp_dir = Path(temp_dir)
                self.temp_dir.mkdir(exist_ok=True)

            # 提取项目名称
            project_name = self._extract_project_name(github_url)
            project_path = self.temp_dir / project_name

            # 尝试克隆仓库
            if self._is_valid_github_url(github_url):
                print(f"正在克隆GitHub项目: {github_url}")
                result = subprocess.run(
                    ["git", "clone", "--depth", "1", github_url, str(project_path)],
                    capture_output=True,
                    text=True,
                    timeout=60
                )

                if result.returncode != 0:
                    print(f"克隆失败，尝试下载主文件...")
                    return self._download_github_files(github_url, project_path)

                return str(project_path)
            else:
                raise ValueError("无效的GitHub URL")

        except Exception as e:
            print(f"GitHub项目处理失败: {str(e)}")
            raise

    def _normalize_github_url(self, url: str) -> str:
        """标准化GitHub URL"""
        url = url.strip()

        # 如果已经是很完整的URL，直接返回
        if url.startswith("https://github.com/"):
            return url

        # 如果是用户名/仓库名格式
        if "/" in url and not url.startswith("http"):
            return f"https://github.com/{url}"

        # 其他情况尝试添加GitHub前缀
        return f"https://github.com/{url}"

    def _is_valid_github_url(self, url: str) -> bool:
        """验证是否是有效的GitHub URL"""
        github_pattern = r"https?://github\.com/[\w\-\.]+/[\w\-\.]+/?$"
        return bool(re.match(github_pattern, url))

    def _extract_project_name(self, github_url: str) -> str:
        """从GitHub URL提取项目名称"""
        # 移除末尾的斜杠
        url = github_url.rstrip('/')
        # 提取最后一部分作为项目名
        return url.split('/')[-1]

    def _download_github_files(self, github_url: str, project_path: Path) -> str:
        """下载GitHub项目的主要文件（当克隆失败时）"""
        import requests
        from bs4 import BeautifulSoup

        try:
            # 解析GitHub仓库信息
            owner, repo = github_url.strip('/').split('/')[-2:]

            # 下载README
            readme_content = self._fetch_github_file(owner, repo, "README.md")
            if readme_content:
                (project_path / "README.md").write_text(readme_content, encoding='utf-8')

            # 尝试下载package.json或requirements.txt
            package_json = self._fetch_github_file(owner, repo, "package.json")
            if package_json:
                (project_path / "package.json").write_text(package_json, encoding='utf-8')

            requirements_txt = self._fetch_github_file(owner, repo, "requirements.txt")
            if requirements_txt:
                (project_path / "requirements.txt").write_text(requirements_txt, encoding='utf-8')

            # 下载LICENSE文件
            license_content = self._fetch_github_file(owner, repo, "LICENSE")
            if license_content:
                (project_path / "LICENSE").write_text(license_content, encoding='utf-8')

            return str(project_path)

        except Exception as e:
            print(f"下载GitHub文件失败: {str(e)}")
            raise

    def _fetch_github_file(self, owner: str, repo: str, filename: str) -> Optional[str]:
        """获取GitHub仓库中的文件内容"""
        try:
            import requests
            url = f"https://api.github.com/repos/{owner}/{repo}/contents/{filename}"
            headers = {
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "Project-Analyzer"
            }

            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                data = response.json()
                if data.get("encoding") == "base64":
                    import base64
                    content = base64.b64decode(data["content"]).decode('utf-8')
                    return content
                elif data.get("type") == "file":
                    return requests.get(data["download_url"], timeout=10).text

            return None

        except Exception:
            return None

    def get_github_repo_info(self, github_url: str) -> Dict:
        """获取GitHub仓库的基本信息"""
        try:
            import requests

            # 标准化URL并提取owner和repo
            github_url = self._normalize_github_url(github_url)
            owner, repo = github_url.strip('/').split('/')[-2:]

            url = f"https://api.github.com/repos/{owner}/{repo}"
            headers = {
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "Project-Analyzer"
            }

            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                data = response.json()
                return {
                    "name": data.get("name"),
                    "description": data.get("description"),
                    "language": data.get("language"),
                    "stars": data.get("stargazers_count"),
                    "forks": data.get("forks_count"),
                    "open_issues": data.get("open_issues_count"),
                    "created_at": data.get("created_at"),
                    "updated_at": data.get("updated_at"),
                    "license": data.get("license", {}).get("name") if data.get("license") else None,
                    "topics": data.get("topics", []),
                    "homepage": data.get("homepage"),
                    "size": data.get("size"),
                    "is_private": data.get("private", False)
                }
            else:
                return {"error": f"无法获取仓库信息: {response.status_code}"}

        except Exception as e:
            return {"error": f"GitHub API调用失败: {str(e)}"}

    def analyze_github_project(self, github_url: str, temp_dir: str = None) -> Dict:
        """分析GitHub项目"""
        try:
            # 获取仓库基本信息
            repo_info = self.get_github_repo_info(github_url)

            # 克隆或下载项目
            project_path = self.clone_or_extract_github_project(github_url, temp_dir)

            # 使用现有的分析器分析项目
            from analyze_project import ProjectAnalyzer
            from dependency_parser import DependencyParser
            from license_analyzer import LicenseAnalyzer

            analyzer = ProjectAnalyzer(project_path)
            dep_parser = DependencyParser(project_path)
            license_analyzer = LicenseAnalyzer(project_path)

            project_analysis = analyzer.generate_full_analysis()
            dependency_analysis = dep_parser.generate_dependency_report()
            license_analysis = license_analyzer.generate_license_analysis()

            # 清理临时文件
            if self.temp_dir:
                import shutil
                shutil.rmtree(self.temp_dir, ignore_errors=True)

            return {
                "github_info": repo_info,
                "project_analysis": project_analysis,
                "dependency_analysis": dependency_analysis,
                "license_analysis": license_analysis,
                "source": "github_analysis"
            }

        except Exception as e:
            return {
                "error": str(e),
                "source": "github_analysis"
            }

    def cleanup(self):
        """清理临时文件"""
        if self.temp_dir and os.path.exists(self.temp_dir):
            import shutil
            shutil.rmtree(self.temp_dir, ignore_errors=True)

def main():
    """命令行接口"""
    import sys

    if len(sys.argv) < 2:
        print("用法: python github_analyzer.py <GitHub_URL> [临时目录]")
        print("示例: python github_analyzer.py https://github.com/facebook/react")
        sys.exit(1)

    github_url = sys.argv[1]
    temp_dir = sys.argv[2] if len(sys.argv) > 2 else None

    analyzer = GitHubAnalyzer()

    try:
        result = analyzer.analyze_github_project(github_url, temp_dir)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"分析失败: {str(e)}")
    finally:
        analyzer.cleanup()

if __name__ == "__main__":
    main()