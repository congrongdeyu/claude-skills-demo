#!/usr/bin/env python3
"""
简单的报告生成器
直接接收项目信息并生成报告文件，无需JSON数据文件
"""

import os
from datetime import datetime
from pathlib import Path

class SimpleReportGenerator:
    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)
        # 报告目录设置为项目根目录下的reports文件夹
        self.reports_dir = self.skill_path.parent / "reports"

        # 确保报告目录存在
        self.reports_dir.mkdir(exist_ok=True)

    def generate_safe_filename(self, project_name: str, report_type: str = "tech") -> str:
        """生成安全的文件名"""
        # 清理项目名称
        safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_name = safe_name.replace(' ', '_')

        # 生成时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # 报告类型后缀
        type_suffix = {
            "requirements": "requirements_analysis",
            "competitor": "competitor_analysis",
            "scenario": "scenario_analysis"
        }.get(report_type, "requirements_analysis")

        return f"{safe_name}_project_{type_suffix}_{timestamp}.md"

    def create_report_from_template(self, project_name: str, report_type: str, content_data: dict) -> str:
        """根据模板数据创建报告文件"""
        try:
            # 生成文件名
            filename = self.generate_safe_filename(project_name, report_type)
            filepath = self.reports_dir / filename

            # 选择模板
            template_files = {
                "requirements": "requirements_analysis.md",
                "competitor": "competitor_analysis.md",
                "scenario": "scenario_analysis.md"
            }

            template_file = template_files.get(report_type, "requirements_analysis.md")
            template_path = self.skill_path / "assets" / "report_templates" / template_file

            # 读取模板
            if template_path.exists():
                with open(template_path, 'r', encoding='utf-8') as f:
                    template_content = f.read()

                # 替换占位符
                for key, value in content_data.items():
                    placeholder = "{{" + key + "}}"
                    template_content = template_content.replace(placeholder, str(value))

                report_content = template_content
            else:
                # 如果模板不存在，使用简单格式
                report_content = self._create_simple_report(project_name, content_data)

            # 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report_content)

            return str(filepath.absolute())

        except Exception as e:
            raise Exception(f"生成报告失败: {str(e)}")

    def _create_simple_report(self, project_name: str, data: dict) -> str:
        """创建简单格式的报告"""
        return f"""# 项目分析报告：{project_name}

## 项目概览
* **一句话总结：** {data.get('ONE_LINE_SUMMARY', '暂无信息')}
* **核心功能：** {data.get('CORE_FEATURES', '暂无信息')}
* **目标用户：** {data.get('TARGET_USERS', '暂无信息')}

## 技术栈
* **主要技术：** {data.get('PRIMARY_LANGUAGES', '暂无信息')}
* **框架：** {data.get('FRAMEWORKS', '暂无信息')}
* **数据库：** {data.get('DATABASES', '暂无信息')}

## 项目状态
* **维护状态：** {data.get('MAINTENANCE_STATUS', '暂无信息')}
* **许可证：** {data.get('LICENSE_TYPE', '暂无信息')}
* **商用许可：** {data.get('COMMERCIAL_USE', '暂无信息')}

## 快速开始
1. **安装依赖：** {data.get('INSTALL_COMMAND', '暂无信息')}
2. **运行项目：** {data.get('RUN_COMMAND', '暂无信息')}

---
报告生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

def main():
    """命令行接口"""
    import sys

    if len(sys.argv) < 3:
        print("用法: python simple_report_generator.py <项目名称> <报告类型> [标题] [总结]")
        print("报告类型: requirements, competitor, scenario")
        print("  requirements - 需求分析报告")
        print("  competitor - 竞品分析报告")
        print("  scenario - 用户场景分析")
        sys.exit(1)

    skill_path = Path(__file__).parent.parent
    generator = SimpleReportGenerator(skill_path)

    project_name = sys.argv[1]
    report_type = sys.argv[2]

    # 需求分析测试数据
    test_data = {
        'PROJECT_NAME': sys.argv[1],
        'PROJECT_POSITIONING': sys.argv[3] if len(sys.argv) > 3 else "面向开发者的协作工具",
        'VALUE_PROPOSITION': "提高团队协作效率，简化项目管理流程",
        'TARGET_MARKET': "软件开发团队、初创公司、自由职业者",
        'ANALYSIS_PURPOSE': "学习需求分析方法，为自己的项目提供参考",
        'PRIMARY_USER_GROUPS': "项目经理、开发人员、产品经理、团队负责人",
        'USER_PERSONAS': "经验丰富的项目经理、新手开发者、远程团队成员",
        'USER_CHARACTERISTICS': "技术水平中等，注重效率，需要协作工具",
        'USER_SCALE_GROWTH': "目标用户群体稳定增长，潜在市场较大",
        'USER_PAIN_POINTS': (sys.argv[4] if len(sys.argv) > 4 else "协作困难，进度跟踪复杂").split('，')[0] if '，' in (sys.argv[4] if len(sys.argv) > 4 else "协作困难，进度跟踪复杂") else (sys.argv[4] if len(sys.argv) > 4 else "协作困难，进度跟踪复杂"),
        'CORE_NEEDS': "提高协作效率，简化项目管理",
        'NEEDS_PRIORITY': "核心需求：任务管理，次要需求：团队协作",
        'UNMET_NEEDS': "深度集成开发工具，智能化任务分配",
        'CORE_BUSINESS_PROBLEMS': "团队协作效率低下，项目管理复杂",
        'PROBLEM_SEVERITY': "中等严重性，影响团队生产力",
        'MARKET_OPPORTUNITY': "远程办公趋势带来市场机会",
        'BUSINESS_VALUE': "提高团队效率，降低沟通成本",
        'CORE_FEATURES': "任务管理、团队协作、进度跟踪、文件共享",
        'FEATURES_NEEDS_MAPPING': "任务管理对应组织需求，团队协作对应沟通需求",
        'FEATURES_PRIORITY': "任务管理 > 团队协作 > 进度跟踪",
        'FEATURES_COMPLETENESS': "核心功能完整，高级功能待完善",
        'TYPICAL_SCENARIOS': "项目启动、日常协作、进度汇报、项目交付",
        'USER_JOURNEY': "注册登录 → 创建项目 → 邀请成员 → 分配任务 → 跟踪进度",
        'KEY_USER_PATHS': "新用户引导、项目创建流程、任务分配流程",
        'SCENARIO_COVERAGE': "主要场景覆盖良好，边缘场景待优化",
        'MAIN_COMPETITORS': "Jira、Trello、Asana、Microsoft Project",
        'DIFFERENTIATION': "更简洁的界面，更好的开发体验",
        'COMPETITIVE_LANDSCAPE': "竞争激烈，但仍有细分市场机会",
        'MARKET_POSITIONING': "面向开发团队的轻量级项目管理工具",
        'REVENUE_MODEL': "SaaS订阅模式，免费增值策略",
        'COST_STRUCTURE': "主要成本：服务器、开发人员、营销",
        'PROFITABILITY_ANALYSIS': "用户基数达到盈亏平衡点后盈利可观",
        'SCALABILITY_ASSESSMENT': "云原生架构，具有良好的可扩展性",
        'PRODUCT_OPTIMIZATION': "优化用户体验，提高易用性",
        'FEATURE_EXPANSION': "增加自动化功能，集成更多开发工具",
        'UX_IMPROVEMENTS': "简化界面设计，优化移动端体验",
        'BUSINESS_MODEL_OPTIMIZATION': "探索企业级市场，提供定制化服务",
        'LEARNABLE_REQUIREMENTS_METHODS': "用户访谈、场景分析、竞品研究",
        'PRODUCT_DESIGN_PRINCIPLES': "简洁优先、用户中心、渐进增强",
        'USER_RESEARCH_METHODS': "问卷调查、可用性测试、数据分析",
        'FEATURE_DESIGN_THINKING': "最小可行产品、快速迭代、用户反馈驱动",
        'ANALYSIS_TIME': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'REQUIREMENTS_VERSION': '1.0.0'
    }

    try:
        filepath = generator.create_report_from_template(project_name, report_type, test_data)
        print(f"报告生成成功!")
        print(f"文件路径: {filepath}")
    except Exception as e:
        print(f"生成失败: {str(e)}")

if __name__ == "__main__":
    main()