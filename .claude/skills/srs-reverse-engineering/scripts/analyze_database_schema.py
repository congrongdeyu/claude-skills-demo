#!/usr/bin/env python3
"""
数据库模式分析脚本
用于分析项目中的数据库设计和模式
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any

class DatabaseSchemaAnalyzer:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.database_info = {
            "database_type": "",
            "tables": [],
            "models": [],
            "migrations": [],
            "relationships": [],
            "indexes": [],
            "constraints": []
        }

    def analyze(self) -> Dict[str, Any]:
        """分析数据库模式"""
        self._detect_database_type()
        self._extract_models()
        self._extract_migrations()
        self._extract_relationships()
        self._extract_indexes_and_constraints()

        return self.database_info

    def _detect_database_type(self):
        """检测数据库类型"""
        indicators = {
            "MySQL": ["mysql", "pymysql", "mysql-connector", "MYSQL"],
            "PostgreSQL": ["postgresql", "psycopg2", "postgres", "POSTGRES"],
            "MongoDB": ["pymongo", "mongodb", "mongo", "MONGO"],
            "SQLite": ["sqlite3", "SQLITE"],
            "Oracle": ["cx_Oracle", "oracle", "ORACLE"],
            "SQL Server": ["pyodbc", "pymssql", "MSSQL"]
        }

        detected_db = []

        # 检查依赖文件
        dependency_files = ["requirements.txt", "package.json", "pom.xml", "build.gradle"]
        for dep_file in dependency_files:
            file_path = self.project_path / dep_file
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    for db_type, keywords in indicators.items():
                        if any(keyword in content for keyword in keywords):
                            detected_db.append(db_type)

        # 检查配置文件
        config_files = [".env", "config.py", "settings.py", "application.properties"]
        for config_file in config_files:
            file_path = self.project_path / config_file
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    for db_type, keywords in indicators.items():
                        if any(keyword in content for keyword in keywords):
                            detected_db.append(db_type)

        # 检查Docker配置
        docker_compose = self.project_path / "docker-compose.yml"
        if docker_compose.exists():
            with open(docker_compose, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()
                for db_type, keywords in indicators.items():
                    if any(keyword in content for keyword in keywords):
                        detected_db.append(db_type)

        self.database_info["database_type"] = list(set(detected_db)) if detected_db else ["Unknown"]

    def _extract_models(self):
        """提取数据模型"""
        model_patterns = {
            "SQLAlchemy": [
                r'class\s+(\w+)\s*\([^)]*Base[^)]*\):',
                r'__tablename__\s*=\s*[\'"]([^\'"]+)[\'"]',
                r'(\w+)\s*=\s*Column\([^)]+\)'
            ],
            "Django": [
                r'class\s+(\w+)\s*\([^)]*models\.Model[^)]*\):',
                r'(\w+)\s*=\s*models\.\w+\([^)]*\)'
            ],
            "Sequelize": [
                r'\.define\s*\(\s*[\'"]([^\'"]+)[\'"]',
                r'(\w+)\s*:\s*{\s*type:\s*[^}]+}'
            ],
            "Mongoose": [
                r'new\s+Schema\s*\(\s*{',
                r'(\w+)\s*:\s*{\s*type:\s*[^}]+}'
            ]
        }

        # 扫描模型文件
        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'target']]

            for file in files:
                if file.endswith(('.py', '.js', '.ts')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                            # 检测框架类型
                            framework = self._detect_orm_framework(content)
                            if framework:
                                model_info = self._parse_model(content, framework, file_path)
                                if model_info:
                                    self.database_info["models"].append(model_info)

                    except Exception as e:
                        print(f"读取模型文件失败 {file_path}: {e}")

    def _extract_migrations(self):
        """提取数据库迁移信息"""
        migration_dirs = ["migrations", "alembic", "django_migrations", "database/migrations"]

        for migration_dir in migration_dirs:
            dir_path = self.project_path / migration_dir
            if dir_path.exists():
                migrations = []
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        if file.endswith(('.py', '.sql', '.js')):
                            file_path = Path(root) / file
                            try:
                                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    content = f.read()
                                    migration_info = {
                                        "file": str(file_path.relative_to(self.project_path)),
                                        "name": file,
                                        "type": self._detect_migration_type(content),
                                        "description": self._extract_migration_description(content)
                                    }
                                    migrations.append(migration_info)
                            except Exception as e:
                                print(f"读取迁移文件失败 {file_path}: {e}")

                if migrations:
                    self.database_info["migrations"].extend(migrations)

    def _extract_relationships(self):
        """提取表关系"""
        relationship_patterns = {
            "SQLAlchemy": [
                r'relationship\s*\(\s*[\'"]([^\'"]+)[\'"]',
                r'ForeignKey\s*\(\s*[\'"]([^\'"]+)[\'"]',
                r'back_populates\s*=\s*[\'"]([^\'"]+)[\'"]'
            ],
            "Django": [
                r'ForeignKey\s*\([^,]+,\s*[\'"]([^\'"]+)[\'"]',
                r'ManyToManyField\s*\([^,]+,\s*[\'"]([^\'"]+)[\'"]',
                r'OneToOneField\s*\([^,]+,\s*[\'"]([^\'"]+)[\'"]'
            ],
            "Sequelize": [
                r'belongsTo\s*\(\s*[\'"]([^\'"]+)[\'"]',
                r'hasMany\s*\(\s*[\'"]([^\'"]+)[\'"]',
                r'hasOne\s*\(\s*[\'"]([^\'"]+)[\'"]',
                r'belongsToMany\s*\(\s*[\'"]([^\'"]+)[\'"]'
            ]
        }

        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'target']]

            for file in files:
                if file.endswith(('.py', '.js', '.ts')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                            framework = self._detect_orm_framework(content)
                            if framework and framework in relationship_patterns:
                                relationships = self._parse_relationships(content, relationship_patterns[framework], file_path)
                                self.database_info["relationships"].extend(relationships)

                    except Exception as e:
                        print(f"读取关系文件失败 {file_path}: {e}")

    def _extract_indexes_and_constraints(self):
        """提取索引和约束"""
        index_patterns = [
            r'Index\s*\(\s*[\'"]?([^\'",\)]+)',
            r'unique\s*=\s*True',
            r'primary_key\s*=\s*True',
            r'NOT\s+NULL',
            r'UNIQUE\s+INDEX',
            r'FOREIGN\s+KEY'
        ]

        constraint_patterns = [
            r'CheckConstraint\s*\(',
            r'UniqueConstraint\s*\(',
            r'ForeignKey\s*\(',
            r'PRIMARY\s+KEY',
            r'UNIQUE\s+CONSTRAINT'
        ]

        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'target']]

            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.sql')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                            # 提取索引
                            for pattern in index_patterns:
                                matches = re.findall(pattern, content, re.IGNORECASE)
                                for match in matches:
                                    self.database_info["indexes"].append({
                                        "name": match if isinstance(match, str) else "Unknown",
                                        "file": str(file_path.relative_to(self.project_path))
                                    })

                            # 提取约束
                            for pattern in constraint_patterns:
                                if re.search(pattern, content, re.IGNORECASE):
                                    constraint_type = pattern.split('\\')[0].replace('\\\\', '')
                                    self.database_info["constraints"].append({
                                        "type": constraint_type,
                                        "file": str(file_path.relative_to(self.project_path))
                                    })

                    except Exception as e:
                        print(f"读取索引约束文件失败 {file_path}: {e}")

    def _detect_orm_framework(self, content: str) -> str:
        """检测ORM框架类型"""
        if any(keyword in content for keyword in ['SQLAlchemy', 'from sqlalchemy', 'Base = declarative_base']):
            return "SQLAlchemy"
        elif any(keyword in content for keyword in ['models.Model', 'from django.db', 'class models']):
            return "Django"
        elif any(keyword in content for keyword in ['Sequelize', 'sequelize.define', 'DataTypes']):
            return "Sequelize"
        elif any(keyword in content for keyword in ['mongoose', 'new Schema', 'Schema.Types']):
            return "Mongoose"
        return ""

    def _parse_model(self, content: str, framework: str, file_path: Path) -> Dict[str, Any]:
        """解析数据模型"""
        if framework == "SQLAlchemy":
            return self._parse_sqlalchemy_model(content, file_path)
        elif framework == "Django":
            return self._parse_django_model(content, file_path)
        elif framework == "Sequelize":
            return self._parse_sequelize_model(content, file_path)
        elif framework == "Mongoose":
            return self._parse_mongoose_model(content, file_path)
        return None

    def _parse_sqlalchemy_model(self, content: str, file_path: Path) -> Dict[str, Any]:
        """解析SQLAlchemy模型"""
        model_pattern = r'class\s+(\w+)\s*\([^)]*Base[^)]*\):([^}]+?)(?=class|\Z)'
        table_pattern = r'__tablename__\s*=\s*[\'"]([^\'"]+)[\'"]'
        column_pattern = r'(\w+)\s*=\s*Column\(([^)]+)\)'

        models = []
        model_matches = re.findall(model_pattern, content, re.DOTALL)

        for class_name, model_body in model_matches:
            table_match = re.search(table_pattern, model_body)
            table_name = table_match.group(1) if table_match else class_name.lower()

            columns = []
            column_matches = re.findall(column_pattern, model_body)
            for col_name, col_def in column_matches:
                columns.append({
                    "name": col_name,
                    "definition": col_def.strip()
                })

            models.append({
                "name": class_name,
                "table_name": table_name,
                "file": str(file_path.relative_to(self.project_path)),
                "columns": columns
            })

        return {"models": models} if models else None

    def _parse_django_model(self, content: str, file_path: Path) -> Dict[str, Any]:
        """解析Django模型"""
        model_pattern = r'class\s+(\w+)\s*\([^)]*models\.Model[^)]*\):([^}]+?)(?=class|\Z)'
        field_pattern = r'(\w+)\s*=\s*models\.(\w+)\([^)]*\)'

        models = []
        model_matches = re.findall(model_pattern, content, re.DOTALL)

        for class_name, model_body in model_matches:
            fields = []
            field_matches = re.findall(field_pattern, model_body)
            for field_name, field_type in field_matches:
                fields.append({
                    "name": field_name,
                    "type": field_type
                })

            models.append({
                "name": class_name,
                "file": str(file_path.relative_to(self.project_path)),
                "fields": fields
            })

        return {"models": models} if models else None

    def _parse_sequelize_model(self, content: str, file_path: Path) -> Dict[str, Any]:
        """解析Sequelize模型"""
        define_pattern = r'\.define\s*\(\s*[\'"]([^\'"]+)[\'"]\s*,\s*{([^}]+)}'
        field_pattern = r'(\w+)\s*:\s*{\s*type:\s*([^}]+)}'

        models = []
        define_matches = re.findall(define_pattern, content, re.DOTALL)

        for table_name, model_body in define_matches:
            fields = []
            field_matches = re.findall(field_pattern, model_body)
            for field_name, field_type in field_matches:
                fields.append({
                    "name": field_name,
                    "type": field_type.strip()
                })

            models.append({
                "name": table_name.capitalize(),
                "table_name": table_name,
                "file": str(file_path.relative_to(self.project_path)),
                "fields": fields
            })

        return {"models": models} if models else None

    def _parse_mongoose_model(self, content: str, file_path: Path) -> Dict[str, Any]:
        """解析Mongoose模型"""
        schema_pattern = r'new\s+Schema\s*\(\s*{([^}]+)}'
        field_pattern = r'(\w+)\s*:\s*{\s*type:\s*([^}]+)}'

        models = []
        schema_matches = re.findall(schema_pattern, content, re.DOTALL)

        for schema_body in schema_matches:
            fields = []
            field_matches = re.findall(field_pattern, schema_body)
            for field_name, field_type in field_matches:
                fields.append({
                    "name": field_name,
                    "type": field_type.strip()
                })

            models.append({
                "name": "MongooseSchema",
                "file": str(file_path.relative_to(self.project_path)),
                "fields": fields
            })

        return {"models": models} if models else None

    def _parse_relationships(self, content: str, patterns: List[str], file_path: Path) -> List[Dict[str, Any]]:
        """解析关系"""
        relationships = []
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                relationships.append({
                    "type": pattern.split('\\')[0].replace('\\\\', ''),
                    "target": match,
                    "file": str(file_path.relative_to(self.project_path))
                })
        return relationships

    def _detect_migration_type(self, content: str) -> str:
        """检测迁移类型"""
        if 'create_table' in content or 'CREATE TABLE' in content:
            return "Create Table"
        elif 'add_column' in content or 'ALTER TABLE ADD' in content:
            return "Add Column"
        elif 'drop_table' in content or 'DROP TABLE' in content:
            return "Drop Table"
        elif 'modify_column' in content or 'ALTER TABLE MODIFY' in content:
            return "Modify Column"
        else:
            return "Unknown"

    def _extract_migration_description(self, content: str) -> str:
        """提取迁移描述"""
        # 尝试提取注释或文档字符串
        comment_patterns = [
            r'"""([^"]+)"""',
            r"'''([^']+)'''",
            r'#\s*(.+)$',
            r'--\s*(.+)$'
        ]

        for pattern in comment_patterns:
            match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
            if match:
                return match.group(1).strip()

        return "No description available"

def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description="分析数据库模式")
    parser.add_argument("project_path", help="项目路径")
    parser.add_argument("--output", "-o", help="输出JSON文件路径")

    args = parser.parse_args()

    analyzer = DatabaseSchemaAnalyzer(args.project_path)
    result = analyzer.analyze()

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"数据库分析结果已保存到: {args.output}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()