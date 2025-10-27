#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据库逆向工程脚本
自动分析数据库结构并生成ERD和数据字典
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

@dataclass
class Column:
    name: str
    data_type: str
    is_nullable: bool = True
    is_primary_key: bool = False
    is_foreign_key: bool = False
    foreign_table: Optional[str] = None
    foreign_column: Optional[str] = None
    default_value: Optional[str] = None
    max_length: Optional[int] = None

@dataclass
class Table:
    name: str
    columns: List[Column]
    primary_keys: List[str]
    foreign_keys: Dict[str, str]

class DatabaseAnalyzer:
    def __init__(self):
        self.tables: Dict[str, Table] = {}

    def analyze_sql_file(self, file_path: str) -> None:
        """分析SQL创建脚本"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self._parse_sql_content(content)
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")

    def analyze_prisma_schema(self, file_path: str) -> None:
        """分析Prisma schema文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self._parse_prisma_content(content)
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")

    def _parse_sql_content(self, content: str) -> None:
        """解析SQL内容"""
        # 匹配CREATE TABLE语句
        table_pattern = r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?`?(\w+)`?\s*\((.*?)\)\s*(?:ENGINE|;|$)'
        matches = re.findall(table_pattern, content, re.IGNORECASE | re.DOTALL)

        for table_name, table_content in matches:
            columns = []
            primary_keys = []
            foreign_keys = {}

            # 解析列定义
            lines = [line.strip() for line in table_content.split('\n') if line.strip()]
            for line in lines:
                if line.upper().startswith('PRIMARY KEY'):
                    # 解析主键
                    pk_match = re.search(r'PRIMARY\s+KEY\s*\(([^)]+)\)', line, re.IGNORECASE)
                    if pk_match:
                        pk_cols = [col.strip().strip('`') for col in pk_match.group(1).split(',')]
                        primary_keys.extend(pk_cols)
                elif line.upper().startswith('FOREIGN KEY'):
                    # 解析外键
                    fk_match = re.search(r'FOREIGN\s+KEY\s*\(([^)]+)\)\s*REFERENCES\s+`?(\w+)`?\s*\(([^)]+)\)', line, re.IGNORECASE)
                    if fk_match:
                        foreign_keys[fk_match.group(1).strip().strip('`')] = f"{fk_match.group(2)}.{fk_match.group(3)}"
                else:
                    # 解析列定义
                    column = self._parse_sql_column(line)
                    if column:
                        columns.append(column)

            self.tables[table_name] = Table(table_name, columns, primary_keys, foreign_keys)

    def _parse_prisma_content(self, content: str) -> None:
        """解析Prisma schema内容"""
        # 匹配model定义
        model_pattern = r'model\s+(\w+)\s*\{(.*?)\}'
        matches = re.findall(model_pattern, content, re.DOTALL)

        for model_name, model_content in matches:
            columns = []
            primary_keys = []
            foreign_keys = {}

            lines = [line.strip() for line in model_content.split('\n') if line.strip()]
            for line in lines:
                if line.startswith('@') or line.startswith('//'):
                    continue

                parts = line.split()
                if len(parts) >= 2:
                    col_name = parts[0]
                    col_type = parts[1]

                    # 分析字段属性
                    is_optional = '?' in col_type
                    is_list = '[]' in col_type
                    base_type = col_type.replace('?', '').replace('[]', '')

                    # 查找关系属性
                    relation_match = re.search(r'@relation\(([^)]+)\)', line)
                    if relation_match:
                        # 这是一个外键关系
                        fields_match = re.search(r'fields:\s*\[?(\w+)\]?', relation_match.group(1))
                        refs_match = re.search(r'references:\s*\[?(\w+)\]?', relation_match.group(1))
                        if fields_match and refs_match:
                            foreign_keys[fields_match.group(1)] = f"{base_type}.{refs_match.group(1)}"

                    column = Column(
                        name=col_name,
                        data_type=base_type,
                        is_nullable=is_optional,
                        is_primary_key='@id' in line,
                        is_foreign_key=bool(relation_match)
                    )
                    columns.append(column)

            self.tables[model_name] = Table(model_name, columns, [], foreign_keys)

    def _parse_sql_column(self, line: str) -> Optional[Column]:
        """解析SQL列定义"""
        # 基本列定义模式
        column_pattern = r'`?(\w+)`?\s+(\w+)(?:\(([^)]+)\))?(.*)'
        match = re.match(column_pattern, line.strip())

        if not match:
            return None

        column_name = match.group(1)
        data_type = match.group(2).upper()
        length_info = match.group(3)
        constraints = match.group(4)

        # 解析约束
        is_primary_key = 'PRIMARY KEY' in constraints.upper()
        is_nullable = 'NOT NULL' not in constraints.upper()
        is_auto_increment = 'AUTO_INCREMENT' in constraints.upper()

        # 解析外键
        is_foreign_key = False
        foreign_table = None
        foreign_column = None

        if 'REFERENCES' in constraints.upper():
            ref_match = re.search(r'REFERENCES\s+`?(\w+)`?\s*\(`?(\w+)`?\)', constraints, re.IGNORECASE)
            if ref_match:
                is_foreign_key = True
                foreign_table = ref_match.group(1)
                foreign_column = ref_match.group(2)

        # 解析默认值
        default_value = None
        default_match = re.search(r'DEFAULT\s+(\S+)', constraints, re.IGNORECASE)
        if default_match:
            default_value = default_match.group(1).strip("'\"")

        max_length = None
        if length_info:
            try:
                max_length = int(length_info.split(',')[0])
            except ValueError:
                pass

        return Column(
            name=column_name,
            data_type=data_type,
            is_nullable=is_nullable,
            is_primary_key=is_primary_key,
            is_foreign_key=is_foreign_key,
            foreign_table=foreign_table,
            foreign_column=foreign_column,
            default_value=default_value,
            max_length=max_length
        )

    def generate_erd_mermaid(self) -> str:
        """生成Mermaid格式的ERD"""
        mermaid_lines = ["erDiagram"]

        # 添加实体定义
        for table_name, table in self.tables.items():
            columns_def = []
            for col in table.columns:
                col_str = f"    {col.name} {col.data_type}"
                if col.is_primary_key:
                    col_str += " PK"
                if col.is_foreign_key:
                    col_str += " FK"
                columns_def.append(col_str)

            if columns_def:
                mermaid_lines.append(f"    {table_name} {{")
                mermaid_lines.extend(columns_def)
                mermaid_lines.append("    }")

        # 添加关系
        for table_name, table in self.tables.items():
            for fk_col, ref_table in table.foreign_keys.items():
                if '.' in ref_table:
                    ref_table_name, ref_col = ref_table.split('.', 1)
                    mermaid_lines.append(f"    {table_name} ||--o{{ {ref_table_name} : \"{fk_col} -> {ref_col}\"}}")

        return "\n".join(mermaid_lines)

    def generate_data_dictionary(self) -> str:
        """生成数据字典"""
        dictionary_lines = ["# 数据字典\n"]

        for table_name, table in self.tables.items():
            dictionary_lines.append(f"## 表: {table_name}")
            dictionary_lines.append("")

            # 表格头
            dictionary_lines.append("| 字段名 | 数据类型 | 可空 | 主键 | 外键 | 默认值 | 描述 |")
            dictionary_lines.append("|--------|----------|------|------|------|--------|------|")

            for col in table.columns:
                nullable = "是" if col.is_nullable else "否"
                primary_key = "是" if col.is_primary_key else "否"
                foreign_key = "是" if col.is_foreign_key else "否"
                default_val = col.default_value or ""

                foreign_ref = ""
                if col.is_foreign_key and col.foreign_table:
                    foreign_ref = f" -> {col.foreign_table}"

                dictionary_lines.append(f"| {col.name} | {col.data_type}{foreign_ref} | {nullable} | {primary_key} | {foreign_key} | {default_val} |  |")

            dictionary_lines.append("")

        return "\n".join(dictionary_lines)

    def export_analysis(self, output_dir: str) -> None:
        """导出分析结果"""
        os.makedirs(output_dir, exist_ok=True)

        # 生成ERD
        erd_content = self.generate_erd_mermaid()
        with open(os.path.join(output_dir, "erd.md"), "w", encoding="utf-8") as f:
            f.write("# 实体关系图 (ERD)\n\n")
            f.write("```mermaid\n")
            f.write(erd_content)
            f.write("\n```\n")

        # 生成数据字典
        dict_content = self.generate_data_dictionary()
        with open(os.path.join(output_dir, "data_dictionary.md"), "w", encoding="utf-8") as f:
            f.write(dict_content)

        # 生成JSON格式的分析结果
        json_data = {}
        for table_name, table in self.tables.items():
            json_data[table_name] = {
                "columns": [
                    {
                        "name": col.name,
                        "data_type": col.data_type,
                        "is_nullable": col.is_nullable,
                        "is_primary_key": col.is_primary_key,
                        "is_foreign_key": col.is_foreign_key,
                        "foreign_table": col.foreign_table,
                        "foreign_column": col.foreign_column,
                        "default_value": col.default_value,
                        "max_length": col.max_length
                    }
                    for col in table.columns
                ],
                "primary_keys": table.primary_keys,
                "foreign_keys": table.foreign_keys
            }

        with open(os.path.join(output_dir, "database_analysis.json"), "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="数据库逆向工程分析工具")
    parser.add_argument("path", help="要分析的项目路径")
    parser.add_argument("--output", "-o", default="./srs_analysis", help="输出目录")

    args = parser.parse_args()

    # 验证输入路径
    if not os.path.exists(args.path):
        print(f"错误: 路径 '{args.path}' 不存在")
        return 1

    # 创建输出目录
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)

    analyzer = DatabaseAnalyzer()

    # 查找数据库相关文件
    project_path = Path(args.path)

    # 查找SQL文件
    sql_files = list(project_path.rglob("*.sql"))
    for sql_file in sql_files:
        print(f"分析SQL文件: {sql_file}")
        try:
            analyzer.analyze_sql_file(str(sql_file))
        except Exception as e:
            print(f"警告: 分析文件 {sql_file} 时出错: {e}")

    # 查找Prisma schema文件
    prisma_files = list(project_path.rglob("schema.prisma"))
    for prisma_file in prisma_files:
        print(f"分析Prisma文件: {prisma_file}")
        try:
            analyzer.analyze_prisma_schema(str(prisma_file))
        except Exception as e:
            print(f"警告: 分析文件 {prisma_file} 时出错: {e}")

    # 查找常见的数据库迁移文件
    migration_patterns = ["**/migrations/**/*.sql", "**/database/**/*.sql"]
    for pattern in migration_patterns:
        for file_path in project_path.glob(pattern):
            print(f"分析迁移文件: {file_path}")
            try:
                analyzer.analyze_sql_file(str(file_path))
            except Exception as e:
                print(f"警告: 分析文件 {file_path} 时出错: {e}")

    if not analyzer.tables:
        print("未找到数据库相关文件")
        return 1

    # 导出分析结果
    analyzer.export_analysis(args.output)
    print(f"\n数据库分析完成！结果已保存到: {args.output}")
    print(f"发现 {len(analyzer.tables)} 个表")

if __name__ == "__main__":
    main()