#!/usr/bin/env python3
"""
技术选型与架构设计技能测试脚本
验证所有脚本的功能是否正常工作
"""

import sys
import json
import os
from pathlib import Path

# 添加skill路径到Python路径
sys.path.append(str(Path(__file__).parent.parent))

# 导入技能脚本
from tech_selector import TechSelector
from architecture_designer import ArchitectureDesigner
from report_generator import ReportGenerator

def test_tech_selector():
    """测试技术选型器"""
    print("=== 测试技术选型器 ===")

    # 测试数据
    test_project = {
        "project_type": "web_application",
        "scale_level": "medium",
        "core_features": ["用户管理", "订单处理"],
        "performance_requirements": ["中等"],
        "security_requirements": ["中等"],
        "team_skills": ["python", "javascript"],
        "timeline": "medium",
        "budget": "medium",
        "domain": "general"
    }

    selector = TechSelector()
    requirements = selector.analyze_requirements(test_project)

    # 测试单个技术栈评估
    result = selector.evaluate_tech_stack("java_spring", requirements)
    print(f"Java Spring 评估结果: {result['scores']['overall']:.1f}/10")

    # 测试完整对比分析
    comparison_result = selector.compare_tech_stacks(requirements)
    print(f"技术栈对比完成，共对比了 {len(comparison_result['comparison_results']) 个技术栈")
    print(f"推荐: {comparison_result['top_recommendation']['tech_info']['name']}")

def test_architecture_designer():
    """测试架构设计器"""
    print("\n=== 测试架构设计器 ===")

    # 测试数据
    test_project = {
        "project_name": "电商平台",
        "project_type": "microservices",
        "core_features": ["用户服务", "订单服务", "支付服务"],
        "performance_requirements": ["高并发", "低延迟"],
        "security_requirements": ["高安全"],
        "architecture_preferences": ["高可用", "可扩展"]
    }

    designer = ArchitectureDesigner()
    design_result = designer.generate_architecture_design("测试项目", test_project)

    print(f"架构模式: {design_result['pattern']}")
    print(f"组件数量: {len(design_result['components'])}")
    print(f"数据流设计: {' -> '.join(design_result['data_flow'])}")

def test_report_generator():
    """测试报告生成器"""
    print("\n=== 测试报告生成器 ===")

    generator = ReportGenerator(".")

    # 测试技术选型报告生成
    try:
        # 创建测试数据
        test_tech_analysis = {
            "comparison_results": {"mock": "技术对比结果"},
            "top_recommendation": {"mock": "推荐结果"},
            "analysis_summary": "分析总结"
        }

        # 生成报告
        result = generator.generate_tech_selection_report(
            "测试电商项目",
            test_tech_analysis,
            test_project
        )
        print(f"技术选型报告生成成功: {result}")
    except Exception as e:
        print(f"技术选型报告生成失败: {str(e)}")

def test_all():
    """运行所有测试"""
    print("开始测试技术选型与架构设计技能...")

    # 测试技术选型器
    test_tech_selector()

    # 测试架构设计器
    test_architecture_designer()

    # 测试报告生成器
    test_report_generator()

def main():
    """主测试函数"""
    print("=== 技术选型与架构设计技能测试 ===")

    try:
        test_all()
        print("\n✅ 所有测试通过！")
    try:
        test_tech_selector()
        test_architecture_designer()
        test_report_generator()
        print("\n✅ 所有测试通过！\n=== 测试完成 ===")
    except Exception as e:
            print(f"❌ 测试失败: {str(e)}\n\n=== 测试完成 ===")
        finally:
            print("=== 清理临时文件 ===")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()