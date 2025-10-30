#!/usr/bin/env python3
"""
Report Generator Script
Generates project analysis reports and saves them to the reports directory
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

class ReportGenerator:
    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)
        self.reports_dir = self.skill_path / "reports"
        self.templates_dir = self.skill_path / "assets" / "report_templates"

        # 确保报告目录存在
        self.reports_dir.mkdir(exist_ok=True)

    def generate_filename(self, project_name: str, report_type: str) -> str:
        """生成报告文件名"""
        # 清理项目名称，移除不安全的文件名字符
        safe_project_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_project_name = safe_project_name.replace(' ', '_')

        # 生成时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # 报告类型映射
        type_mapping = {
            "full": "full_analysis",
            "commercial": "commercial_eval",
            "quick": "quick_summary"
        }

        report_suffix = type_mapping.get(report_type, report_type)

        return f"{safe_project_name}_{report_suffix}_{timestamp}.md"

    def load_template(self, template_name: str) -> str:
        """加载报告模板"""
        template_file = self.templates_dir / f"{template_name}.md"

        if not template_file.exists():
            raise FileNotFoundError(f"模板文件不存在: {template_file}")

        with open(template_file, 'r', encoding='utf-8') as f:
            return f.read()

    def fill_template(self, template_content: str, data: Dict) -> str:
        """填充模板内容"""
        try:
            filled_content = template_content

            # 替换所有模板变量
            for key, value in data.items():
                placeholder = "{{" + key + "}}"
                if placeholder in filled_content:
                    filled_content = filled_content.replace(placeholder, str(value))

            return filled_content
        except Exception as e:
            raise Exception(f"模板填充失败: {str(e)}")

    def save_report(self, content: str, filename: str) -> str:
        """保存报告到文件"""
        report_path = self.reports_dir / filename

        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(content)

            return str(report_path.absolute())
        except Exception as e:
            raise Exception(f"保存报告失败: {str(e)}")

    def generate_report(self, project_name: str, report_type: str, data: Dict) -> Dict:
        """生成完整的报告"""
        try:
            # 确定模板名称
            template_mapping = {
                "full": "full_analysis",
                "commercial": "commercial_evaluation",
                "quick": "quick_summary"
            }

            template_name = template_mapping.get(report_type, "full_analysis")

            # 生成文件名
            filename = self.generate_filename(project_name, report_type)

            # 加载模板
            template_content = self.load_template(template_name)

            # 填充模板
            filled_content = self.fill_template(template_content, data)

            # 保存报告
            report_path = self.save_report(filled_content, filename)

            return {
                "status": "成功",
                "filename": filename,
                "path": report_path,
                "report_type": report_type,
                "project_name": project_name
            }

        except Exception as e:
            return {
                "status": "错误",
                "error": str(e)
            }

    def list_reports(self) -> list:
        """列出所有已生成的报告"""
        if not self.reports_dir.exists():
            return []

        reports = []
        for report_file in self.reports_dir.glob("*.md"):
            reports.append({
                "filename": report_file.name,
                "path": str(report_file.absolute()),
                "size": report_file.stat().st_size,
                "modified": datetime.fromtimestamp(report_file.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            })

        return sorted(reports, key=lambda x: x["modified"], reverse=True)

    def get_report_path(self, filename: str) -> Optional[str]:
        """获取报告文件的完整路径"""
        report_path = self.reports_dir / filename
        if report_path.exists():
            return str(report_path.absolute())
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("用法: python generate_report.py <项目名称> <报告类型> <数据文件路径>")
        print("报告类型: full, commercial, quick")
        sys.exit(1)

    skill_path = Path(__file__).parent.parent
    generator = ReportGenerator(skill_path)

    project_name = sys.argv[1]
    report_type = sys.argv[2]
    data_file = sys.argv[3]

    try:
        # 读取数据文件
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 生成报告
        result = generator.generate_report(project_name, report_type, data)

        if result["status"] == "成功":
            print(f"报告生成成功!")
            print(f"文件名: {result['filename']}")
            print(f"路径: {result['path']}")
        else:
            print(f"报告生成失败: {result['error']}")

    except Exception as e:
        print(f"执行失败: {str(e)}")