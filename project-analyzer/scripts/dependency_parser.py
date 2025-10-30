#!/usr/bin/env python3
"""
Dependency Parser Script
Parse and analyze project dependencies from various package manager files
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set

class DependencyParser:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)

    def parse_package_json(self) -> Dict:
        """Parse Node.js package.json dependencies"""
        package_json_path = self.project_path / "package.json"
        if not package_json_path.exists():
            return {}

        try:
            with open(package_json_path, 'r', encoding='utf-8') as f:
                package_data = json.load(f)

            dependencies = {
                "dependencies": package_data.get("dependencies", {}),
                "devDependencies": package_data.get("devDependencies", {}),
                "peerDependencies": package_data.get("peerDependencies", {})
            }

            return {
                "type": "nodejs",
                "name": package_data.get("name", "unknown"),
                "version": package_data.get("version", "unknown"),
                "dependencies": dependencies,
                "scripts": package_data.get("scripts", {})
            }
        except Exception as e:
            return {"错误": str(e)}

    def parse_requirements_txt(self) -> Dict:
        """Parse Python requirements.txt"""
        requirements_path = self.project_path / "requirements.txt"
        if not requirements_path.exists():
            return {}

        try:
            with open(requirements_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            dependencies = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Parse version specifications
                    match = re.match(r'^([a-zA-Z0-9\-_]+)([><=!]+.*)?$', line)
                    if match:
                        package_name = match.group(1)
                        version_spec = match.group(2) or ""
                        dependencies.append({
                            "name": package_name,
                            "version": version_spec.strip()
                        })

            return {
                "type": "python",
                "dependencies": dependencies
            }
        except Exception as e:
            return {"错误": str(e)}

    def parse_pom_xml(self) -> Dict:
        """Parse Maven pom.xml for Java projects"""
        pom_path = self.project_path / "pom.xml"
        if not pom_path.exists():
            return {}

        try:
            with open(pom_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Simple regex-based parsing (for basic cases)
            # In production, use proper XML parsing
            dependencies = []
            dep_matches = re.findall(r'<dependency>.*?<groupId>(.*?)</groupId>.*?<artifactId>(.*?)</artifactId>.*?<version>(.*?)</version>.*?</dependency>', content, re.DOTALL)

            for group_id, artifact_id, version in dep_matches:
                dependencies.append({
                    "groupId": group_id.strip(),
                    "artifactId": artifact_id.strip(),
                    "version": version.strip()
                })

            return {
                "type": "java",
                "dependencies": dependencies
            }
        except Exception as e:
            return {"错误": str(e)}

    def detect_tech_stack(self) -> Dict:
        """Detect technology stack based on dependencies"""
        tech_indicators = {
            "frontend": {
                "react": ["react", "react-dom"],
                "vue": ["vue"],
                "angular": ["@angular/core"],
                "svelte": ["svelte"],
                "next": ["next"],
                "nuxt": ["nuxt"],
                "webpack": ["webpack"],
                "vite": ["vite"],
                "tailwind": ["tailwindcss"],
                "bootstrap": ["bootstrap"],
                "material-ui": ["@mui/material"]
            },
            "backend": {
                "express": ["express"],
                "fastapi": ["fastapi"],
                "django": ["django"],
                "flask": ["flask"],
                "spring": ["spring-boot-starter"],
                "rails": ["rails"],
                "laravel": ["laravel"]
            },
            "database": {
                "postgresql": ["pg", "psycopg2"],
                "mysql": ["mysql", "mysql2"],
                "mongodb": ["mongoose", "pymongo"],
                "redis": ["redis", "ioredis"],
                "sqlite": ["sqlite3"]
            },
            "tools": {
                "docker": ["docker"],
                "testing": ["jest", "pytest", "junit"],
                "linting": ["eslint", "pylint", "checkstyle"],
                "bundler": ["webpack", "vite", "parcel"]
            }
        }

        detected_tech = {category: [] for category in tech_indicators}

        # Parse all dependency files
        all_deps = []

        package_data = self.parse_package_json()
        if package_data:
            all_deps.extend(package_data.get("dependencies", {}).keys())
            all_deps.extend(package_data.get("devDependencies", {}).keys())

        python_deps = self.parse_requirements_txt()
        if python_deps:
            all_deps.extend([dep["name"] for dep in python_deps.get("dependencies", [])])

        java_deps = self.parse_pom_xml()
        if java_deps:
            all_deps.extend([f"{dep['groupId']}:{dep['artifactId']}" for dep in java_deps.get("dependencies", [])])

        # Match dependencies with tech indicators
        for dep in all_deps:
            dep_lower = dep.lower()
            for category, technologies in tech_indicators.items():
                for tech_name, indicators in technologies.items():
                    if any(indicator.lower() in dep_lower for indicator in indicators):
                        if tech_name not in detected_tech[category]:
                            detected_tech[category].append(tech_name)

        return detected_tech

    def generate_dependency_report(self) -> Dict:
        """Generate comprehensive dependency analysis"""
        return {
            "package_json": self.parse_package_json(),
            "requirements_txt": self.parse_requirements_txt(),
            "pom_xml": self.parse_pom_xml(),
            "tech_stack": self.detect_tech_stack()
        }

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python dependency_parser.py <project_path>")
        sys.exit(1)

    parser = DependencyParser(sys.argv[1])
    result = parser.generate_dependency_report()
    print(json.dumps(result, indent=2))