#!/usr/bin/env python3
"""
GitHub Repository Analysis Script

This script analyzes a GitHub repository to extract product information
for PRD (Product Requirements Document) generation.
"""

import requests
import json
import re
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class GitHubRepo:
    owner: str
    repo: str
    url: str
    api_base: str = "https://api.github.com"

class GitHubAnalyzer:
    def __init__(self, token: Optional[str] = None):
        """
        Initialize GitHub analyzer with optional authentication token.

        Args:
            token: GitHub personal access token for higher rate limits
        """
        self.token = token
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        if token:
            self.headers["Authorization"] = f"token {token}"

    def parse_github_url(self, url: str) -> GitHubRepo:
        """Parse GitHub URL to extract owner and repository name."""
        parsed = urlparse(url)
        path_parts = parsed.path.strip('/').split('/')

        if len(path_parts) < 2:
            raise ValueError("Invalid GitHub URL format")

        return GitHubRepo(
            owner=path_parts[0],
            repo=path_parts[1],
            url=url
        )

    def get_repo_info(self, repo: GitHubRepo) -> Dict[str, Any]:
        """Get basic repository information."""
        url = f"{repo.api_base}/repos/{repo.owner}/{repo.repo}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 404:
            raise ValueError(f"Repository {repo.owner}/{repo.repo} not found")
        elif response.status_code != 200:
            raise ValueError(f"GitHub API error: {response.status_code}")

        return response.json()

    def get_readme(self, repo: GitHubRepo) -> Optional[str]:
        """Get repository README content."""
        url = f"{repo.api_base}/repos/{repo.owner}/{repo.repo}/readme"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 404:
            return None

        data = response.json()
        # README content is base64 encoded
        import base64
        content = base64.b64decode(data['content']).decode('utf-8')
        return content

    def get_languages(self, repo: GitHubRepo) -> Dict[str, int]:
        """Get programming languages used in the repository."""
        url = f"{repo.api_base}/repos/{repo.owner}/{repo.repo}/languages"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.status_code == 200 else {}

    def get_package_info(self, repo: GitHubRepo) -> Dict[str, Any]:
        """Get package.json, requirements.txt, or similar dependency files."""
        package_info = {}

        # Try to get package.json (Node.js)
        try:
            url = f"{repo.api_base}/repos/{repo.owner}/{repo.repo}/contents/package.json"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                import base64
                content = base64.b64decode(response.json()['content']).decode('utf-8')
                package_info['package.json'] = json.loads(content)
        except:
            pass

        # Try to get requirements.txt (Python)
        try:
            url = f"{repo.api_base}/repos/{repo.owner}/{repo.repo}/contents/requirements.txt"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                import base64
                content = base64.b64decode(response.json()['content']).decode('utf-8')
                package_info['requirements.txt'] = content
        except:
            pass

        # Try to get pyproject.toml (Python)
        try:
            url = f"{repo.api_base}/repos/{repo.owner}/{repo.repo}/contents/pyproject.toml"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                import base64
                content = base64.b64decode(response.json()['content']).decode('utf-8')
                package_info['pyproject.toml'] = content
        except:
            pass

        return package_info

    def get_directory_structure(self, repo: GitHubRepo, path: str = "") -> List[Dict[str, Any]]:
        """Get directory structure of the repository."""
        url = f"{repo.api_base}/repos/{repo.owner}/{repo.repo}/contents/{path}"
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            return []

        contents = response.json()
        if isinstance(contents, dict):  # Single file
            return [contents]

        return contents

    def analyze_tech_stack(self, languages: Dict[str, int], package_info: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze technology stack from languages and package files."""
        tech_stack = {
            "frontend": [],
            "backend": [],
            "database": [],
            "frameworks": [],
            "tools": []
        }

        # Analyze from languages
        for lang, bytes_count in languages.items():
            if lang.lower() in ['javascript', 'typescript']:
                tech_stack["frontend"].append(lang.lower())
            elif lang.lower() in ['python', 'java', 'go', 'rust', 'c#', 'php']:
                tech_stack["backend"].append(lang.lower())
            elif lang.lower() in ['html', 'css']:
                tech_stack["frontend"].append(lang.lower())

        # Analyze from package.json
        if 'package.json' in package_info:
            deps = {**package_info['package.json'].get('dependencies', {}),
                   **package_info['package_json'].get('devDependencies', {})}

            for dep in deps.keys():
                if dep.startswith('react'):
                    tech_stack["frameworks"].append("React")
                elif dep.startswith('vue'):
                    tech_stack["frameworks"].append("Vue.js")
                elif dep.startswith('angular'):
                    tech_stack["frameworks"].append("Angular")
                elif dep.startswith('express'):
                    tech_stack["backend"].append("Express.js")
                elif dep.startswith('next'):
                    tech_stack["frameworks"].append("Next.js")
                elif dep in ['mongodb', 'mongoose']:
                    tech_stack["database"].append("MongoDB")
                elif dep in ['pg', 'postgresql']:
                    tech_stack["database"].append("PostgreSQL")
                elif dep in ['mysql']:
                    tech_stack["database"].append("MySQL")

        # Enhanced analysis from pyproject.toml
        if 'pyproject.toml' in package_info:
            try:
                import tomllib  # Python 3.11+
                import io
                data = tomllib.loads(io.StringIO(package_info['pyproject.toml']).read())
            except ImportError:
                try:
                    import toml
                    data = toml.loads(package_info['pyproject.toml'])
                except:
                    data = {}

            # Extract dependencies
            deps = []
            if 'project' in data and 'dependencies' in data['project']:
                deps.extend(data['project']['dependencies'])
            if 'tool' in data and 'poetry' in data['tool'] and 'dependencies' in data['tool']['poetry']:
                deps.extend(data['tool']['poetry']['dependencies'].keys())

            # Map dependencies to technologies
            tech_mapping = {
                'fastapi': 'FastAPI',
                'django': 'Django',
                'flask': 'Flask',
                'sqlalchemy': 'SQLAlchemy',
                'alembic': 'Alembic',
                'pytest': 'Pytest',
                'numpy': 'NumPy',
                'pandas': 'Pandas',
                'scikit-learn': 'Scikit-learn',
                'torch': 'PyTorch',
                'tensorflow': 'TensorFlow',
                'neo4j': 'Neo4j',
                'chromadb': 'ChromaDB',
                'pinecone': 'Pinecone',
                'redis': 'Redis',
                'postgresql': 'PostgreSQL',
                'mongodb': 'MongoDB',
                'requests': 'Requests',
                'asyncio': 'AsyncIO'
            }

            detected_tech = set()
            for dep in deps:
                for tech_name, tech_display in tech_mapping.items():
                    if tech_name in dep.lower():
                        detected_tech.add(tech_display)

            # Categorize detected technologies
            for tech in detected_tech:
                if tech in ['FastAPI', 'Django', 'Flask', 'SQLAlchemy', 'Alembic']:
                    tech_stack["frameworks"].append(tech)
                elif tech in ['Neo4j', 'ChromaDB', 'Pinecone', 'Redis', 'PostgreSQL', 'MongoDB']:
                    tech_stack["database"].append(tech)
                elif tech in ['Pytest', 'Requests', 'AsyncIO']:
                    tech_stack["tools"].append(tech)
                elif tech in ['NumPy', 'Pandas', 'Scikit-learn', 'PyTorch', 'TensorFlow']:
                    tech_stack["backend"].append(f"ML/{tech}")

        # Analyze from requirements.txt
        if 'requirements.txt' in package_info:
            content = package_info['requirements.txt'].lower()
            if 'django' in content:
                tech_stack["frameworks"].append("Django")
            if 'flask' in content:
                tech_stack["frameworks"].append("Flask")
            if 'fastapi' in content:
                tech_stack["frameworks"].append("FastAPI")
            if 'sqlalchemy' in content:
                tech_stack["backend"].append("SQLAlchemy")
            if 'neo4j' in content:
                tech_stack["database"].append("Neo4j")
            if 'chromadb' in content:
                tech_stack["database"].append("ChromaDB")

        return tech_stack

    def extract_features_from_readme(self, readme: str) -> List[str]:
        """Extract feature list from README content."""
        features = []

        # Look for feature lists in README
        patterns = [
            r'## Features?\s*\n(.+?)(?=\n##|\n#|$)',
            r'### Features?\s*\n(.+?)(?=\n###|\n##|$)',
            r'-\s+([A-Z][^.!?]*[.!?])',
            r'\*\s+([A-Z][^.!?]*[.!?])',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, readme, re.DOTALL | re.IGNORECASE)
            for match in matches:
                lines = match.strip().split('\n')
                for line in lines:
                    line = line.strip()
                    if line.startswith(('-', '*', '•')):
                        line = line[1:].strip()
                    if line and len(line) > 10:  # Filter out short lines
                        features.append(line)

        return features[:10]  # Limit to top 10 features

    def analyze_repository(self, github_url: str) -> Dict[str, Any]:
        """
        Complete repository analysis for PRD generation.

        Args:
            github_url: GitHub repository URL

        Returns:
            Dictionary containing analysis results
        """
        try:
            repo = self.parse_github_url(github_url)

            # Gather information
            repo_info = self.get_repo_info(repo)
            readme = self.get_readme(repo)
            languages = self.get_languages(repo)
            package_info = self.get_package_info(repo)
            directory_structure = self.get_directory_structure(repo)

            # Analyze information
            tech_stack = self.analyze_tech_stack(languages, package_info)
            features = self.extract_features_from_readme(readme) if readme else []

            return {
                "repository": {
                    "name": repo_info.get("name"),
                    "full_name": repo_info.get("full_name"),
                    "description": repo_info.get("description"),
                    "url": repo_info.get("html_url"),
                    "stars": repo_info.get("stargazers_count"),
                    "forks": repo_info.get("forks_count"),
                    "open_issues": repo_info.get("open_issues_count"),
                    "language": repo_info.get("language"),
                    "created_at": repo_info.get("created_at"),
                    "updated_at": repo_info.get("updated_at")
                },
                "readme": {
                    "exists": readme is not None,
                    "content": readme[:1000] + "..." if readme and len(readme) > 1000 else readme,
                    "features": features
                },
                "technology": {
                    "languages": languages,
                    "tech_stack": tech_stack,
                    "package_files": list(package_info.keys())
                },
                "structure": {
                    "total_files": len(directory_structure),
                    "main_directories": [item["name"] for item in directory_structure if item["type"] == "dir"]
                },
                "analysis": {
                    "project_type": self._infer_project_type(tech_stack, languages),
                    "complexity": self._assess_complexity(languages, len(directory_structure)),
                    "maturity": self._assess_maturity(repo_info)
                }
            }

        except Exception as e:
            return {"error": str(e)}

    def _infer_project_type(self, tech_stack: Dict[str, Any], languages: Dict[str, int]) -> str:
        """Infer project type from technology stack."""
        if "React" in tech_stack.get("frameworks", []) or "Vue.js" in tech_stack.get("frameworks", []):
            return "Web Application (Frontend)"
        elif "Django" in tech_stack.get("frameworks", []) or "Express.js" in tech_stack.get("backend", []):
            return "Web Application (Backend)"
        elif "Next.js" in tech_stack.get("frameworks", []):
            return "Full-stack Web Application"
        elif any(lang in languages for lang in ["Python", "R", "Jupyter Notebook"]):
            return "Data Science/Machine Learning"
        elif any(lang in languages for lang in ["Java", "Kotlin"]):
            return "Mobile/Enterprise Application"
        else:
            return "General Software Project"

    def _assess_complexity(self, languages: Dict[str, int], file_count: int) -> str:
        """Assess project complexity."""
        language_count = len(languages)

        if language_count <= 2 and file_count <= 50:
            return "Low"
        elif language_count <= 4 and file_count <= 200:
            return "Medium"
        else:
            return "High"

    def _assess_maturity(self, repo_info: Dict[str, Any]) -> str:
        """Assess project maturity."""
        stars = repo_info.get("stargazers_count", 0)
        open_issues = repo_info.get("open_issues_count", 0)
        forks = repo_info.get("forks_count", 0)

        if stars >= 1000 or forks >= 500:
            return "Mature"
        elif stars >= 100 or forks >= 50:
            return "Developing"
        else:
            return "Early Stage"

def main():
    """Main function for command line usage."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: python analyze_github_repo.py <github_url>")
        sys.exit(1)

    github_url = sys.argv[1]
    analyzer = GitHubAnalyzer()

    print(f"Analyzing repository: {github_url}")
    result = analyzer.analyze_repository(github_url)

    if "error" in result:
        print(f"Error: {result['error']}")
        sys.exit(1)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()