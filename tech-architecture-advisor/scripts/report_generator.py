#!/usr/bin/env python3
"""
技术选型与架构设计报告生成器
生成技术选型分析报告和架构设计文档
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

class ReportGenerator:
    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)
        self.reports_dir = self.skill_path.parent / "reports"

        # 确保报告目录存在
        self.reports_dir.mkdir(exist_ok=True)

    def generate_safe_filename(self, project_name: str, report_type: str) -> str:
        """生成安全的文件名"""
        # 清理项目名称
        safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_name = safe_name.replace(' ', '_')

        # 生成时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # 报告类型后缀
        type_suffix = {
            "tech_selection": "tech_selection",
            "architecture_design": "architecture_design"
        }.get(report_type, report_type)

        return f"{safe_name}_{type_suffix}_{timestamp}.md"

    def load_template(self, template_name: str) -> str:
        """加载报告模板"""
        template_file = self.skill_path / "assets" / "reports" / f"{template_name}.md"

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

    def generate_tech_selection_report(self, project_name: str, tech_analysis: Dict, project_data: Dict) -> str:
        """生成技术选型分析报告"""
        try:
            # 生成文件名
            filename = self.generate_safe_filename(project_name, "tech_selection")

            # 加载模板
            template_content = self.load_template("tech_selection_template")

            # 准备数据
            report_data = {
                "PROJECT_NAME": project_name,
                "ANALYSIS_DATE": datetime.now().strftime("%Y年%m月%d日 %H:%M"),
                "PROJECT_TYPE": project_data.get("project_type", "web_application"),
                "SCALE_LEVEL": project_data.get("scale_level", "medium"),
                "TEAM_SIZE": project_data.get("team_size", "unknown"),
                "TIMELINE": project_data.get("timeline", "medium"),
                "BUDGET": project_data.get("budget", "unknown"),
                "DOMAIN": project_data.get("domain", "general"),
                "PERFORMANCE_REQUIREMENTS": ", ".join(project_data.get("performance_requirements", [])),
                "SECURITY_REQUIREMENTS": ", ".join(project_data.get("security_requirements", [])),
                "TEAM_SKILLS": ", ".join(project_data.get("team_skills", [])),

                # 技术栈对比结果
                "COMPARISON_RESULTS": self._format_comparison_results(tech_analysis),
                "TOP_RECOMMENDATION": self._format_top_recommendation(tech_analysis.get("top_recommendation", {})),
                "ANALYSIS_SUMMARY": tech_analysis.get("analysis_summary", ""),

                # 生成详细的技术栈分析
                "TECH_STACK_ANALYSIS": self._generate_tech_stack_analysis(tech_analysis),

                # 风险评估
                "RISK_ASSESSMENT": self._generate_risk_assessment(tech_analysis, project_data),

                # 实施建议
                "IMPLEMENTATION_RECOMMENDATIONS": self._generate_implementation_recommendations(tech_analysis, project_data),

                # 长期考虑
                "LONG_TERM_CONSIDERATIONS": self._generate_long_term_considerations(tech_analysis, project_data)
            }

            # 填充模板
            filled_content = self.fill_template(template_content, report_data)

            # 保存报告
            return self.save_report(filled_content, filename)

        except Exception as e:
            raise Exception(f"生成技术选型报告失败: {str(e)}")

    def generate_architecture_design_report(self, project_name: str, architecture_design: Dict) -> str:
        """生成架构设计文档"""
        try:
            # 生成文件名
            filename = self.generate_safe_filename(project_name, "architecture_design")

            # 加载模板
            template_content = self.load_template("architecture_design_template")

            # 准备数据
            report_data = {
                "PROJECT_NAME": project_name,
                "DESIGN_DATE": datetime.now().strftime("%Y年%m月%d日 %H:%M"),
                "ARCHITECTURE_PATTERN": architecture_design["pattern"],
                "PATTERN_DESCRIPTION": architecture_design["description"],

                # 组件设计
                "COMPONENTS_OVERVIEW": self._format_components_overview(architecture_design["components"]),
                "COMPONENT_DETAILS": self._generate_component_details(architecture_design["components"]),

                # 数据流设计
                "DATA_FLOW_OVERVIEW": " → ".join(architecture_design["data_flow"]),
                "DATA_FLOW_DETAILS": self._generate_data_flow_details(architecture_design["data_flow"], architecture_design["components"]),

                # 非功能性需求
                "PERFORMANCE_REQUIREMENTS": self._format_performance_requirements(architecture_design["non_functional_requirements"].get("performance", {})),
                "AVAILABILITY_REQUIREMENTS": self._format_availability_requirements(architecture_design["non_functional_requirements"].get("availability", {})),
                "SECURITY_REQUIREMENTS": self._format_security_requirements(architecture_design["non_functional_requirements"].get("security", {})),
                "MAINTAINABILITY_REQUIREMENTS": self._format_maintainability_requirements(architecture_design["non_functional_requirements"].get("maintainability", {})),

                # 部署架构
                "DEPLOYMENT_ARCHITECTURE": architecture_design["deployment_architecture"],
                "DEPLOYMENT_STRATEGY": self._generate_deployment_strategy(architecture_design),
                "INFRASTRUCTURE_COMPONENTS": self._generate_infrastructure_components(architecture_design),

                # 实施计划
                "IMPLEMENTATION_PHASES": self._generate_implementation_phases(architecture_design),
                "MIGRATION_STRATEGY": self._generate_migration_strategy(architecture_design),
                "MONITORING_PLAN": self._generate_monitoring_plan(architecture_design)
            }

            # 填充模板
            filled_content = self.fill_template(template_content, report_data)

            # 保存报告
            return self.save_report(filled_content, filename)

        except Exception as e:
            raise Exception(f"生成架构设计文档失败: {str(e)}")

    def _format_comparison_results(self, tech_analysis: Dict) -> str:
        """格式化技术栈对比结果"""
        if not tech_analysis or "comparison_results" not in tech_analysis:
            return "暂无对比结果"

        results = []
        for tech_name, tech_data in tech_analysis["comparison_results"].items():
            scores = tech_data["scores"]
            tech_info = tech_data["tech_info"]

            result = f"### {tech_info['name']}\n"
            result += f"- **综合评分**: {scores['overall']:.1f}/10\n"
            result += f"- **语言**: {tech_info['language']}\n"
            result += f"- **框架**: {tech_info['framework']}\n"
            result += f"- **性能**: {scores['performance']}/10\n"
            result += f"- **可扩展性**: {scores['scalability']}/10\n"
            result += f"- **团队匹配度**: {scores['team_fit']}/10\n"
            result += f"- **推荐理由**: {tech_data['recommendation']}\n"
            result += f"\n**优势**:\n"
            for pro in tech_info['pros'][:3]:
                result += f"- {pro}\n"
            result += f"\n**考虑因素**:\n"
            for con in tech_info['cons'][:3]:
                result += f"- {con}\n"
            result += "\n"

            results.append(result)

        return "\n".join(results)

    def _format_top_recommendation(self, top_recommendation: Dict) -> str:
        """格式化顶部推荐"""
        if not top_recommendation:
            return "暂无推荐"

        tech_info = top_recommendation["tech_info"]
        scores = top_recommendation["scores"]

        return f"### 推荐技术栈\n**{tech_info['name']}** (综合评分: {scores['overall']:.1f}/10)\n\n{top_recommendation['recommendation']}"

    def _generate_tech_stack_analysis(self, tech_analysis: Dict) -> str:
        """生成详细的技术栈分析"""
        if not tech_analysis or "comparison_results" not in tech_analysis:
            return "暂无技术栈分析"

        analysis = []
        for tech_name, tech_data in tech_analysis["comparison_results"].items():
            analysis.append(f"#### {tech_data['tech_info']['name']}")

            # 技术特性
            analysis.append(f"- **开发效率**: {'high': '高', 'medium': '中', 'low': '低'}.get(self._get_efficiency_level(tech_data['tech_info'].framework), '中等')}")
            analysis.append(f"- **学习曲线**: {tech_data['tech_info']['learning_curve']}")
            analysis.append(f"- **社区支持**: {tech_data['tech_info']['community_support']}")

            # 适用场景分析
            patterns = self.patterns.get(tech_name.split('_')[0], {})
            if patterns:
                analysis.append(f"\n**适用场景**:")
                for suitable in patterns.get("suitable_for", []):
                    analysis.append(f"- {suitable}")
                analysis.append(f"\n**不适用场景**:")
                for not_suitable in patterns.get("not_suitable_for", []):
                    analysis.append(f"- {not_suitable}")

            analysis.append("\n")

        return "\n".join(analysis)

    def _get_efficiency_level(self, framework: str) -> str:
        """获取开发效率等级"""
        high_efficiency = ["django", "flask", "express", "spring", "gin"]
        medium_efficiency = ["fastapi", "nestjs", "quarkus"]

        if framework.lower() in high_efficiency:
            return "high"
        elif framework.lower() in medium_efficiency:
            return "medium"
        else:
            return "low"

    def _generate_risk_assessment(self, tech_analysis: Dict, project_data: Dict) -> str:
        """生成风险评估"""
        risks = []

        # 技术风险
        if not project_data.get("team_skills"):
            risks.append("- **技术栈风险**: 团队缺乏相关技术经验，需要培训和学习")

        if project_data.get("timeline") == "fast":
            risks.append("- **时间风险**: 复杂技术栈可能影响项目进度")

        # 团队规模风险
        team_size = project_data.get("team_size", "small")
        if team_size == "small" and project_data.get("scale_level") in ["large", "very_large"]:
            risks.append("- **团队能力风险**: 小团队难以支撑大规模系统")

        # 预算风险
        budget = project_data.get("budget", "medium")
        if budget == "low":
            risks.append("- **预算风险**: 可能需要额外的基础设施投入")
        elif budget == "high":
            risks.append("- **过度工程风险**: 可能导致过度设计和资源浪费")

        if risks:
            return "\n".join(risks)
        else:
            return "当前技术选型风险较低，可以安全实施。"

    def _generate_implementation_recommendations(self, tech_analysis: Dict, project_data: Dict) -> str:
        """生成实施建议"""
        recommendations = []

        # 团队培训建议
        if not project_data.get("team_skills"):
            recommendations.append("1. **团队培训计划**")
            recommendations.append("   - 组织技术栈相关培训")
            recommendations.append("   - 安排技术导师指导")
            recommendations.append("   - 逐步引入新技术")

        # 分阶段实施建议
        if project_data.get("scale_level") in ["large", "very_large"]:
            recommendations.append("2. **分阶段实施**")
            recommendations.append("   - 先实现核心功能MVP")
            recommendations.append("   - 逐步扩展和优化")
            recommendations.append("   - 建立监控和反馈机制")

        # 监控和运维建议
        recommendations.append("3. **监控和运维**")
        recommendations.append("   - 建立应用性能监控")
        recommendations.append("   - 设置日志收集和分析")
        recommendations.append("   - 建立告警机制")
            recommendations.append("   - 制定运维手册")

        return "\n".join(recommendations)

    def _generate_long_term_considerations(self, tech_analysis: Dict, project_data: Dict) -> str:
        """生成长期考虑"""
        considerations = []

        # 技术债务管理
        considerations.append("1. **技术债务管理**")
        considerations.append("   - 建立代码质量标准")
        considerations.append("   - 定期重构和优化")
        considerations.append("   - 技术债务跟踪和评估")

        # 可扩展性规划
        if project_data.get("scale_level") != "small":
            considerations.append("2. **可扩展性规划**")
            considerations.append("   - 设计水平扩展架构")
            considerations.append("   - 制定扩容策略")
            " - 建立性能基准测试")

        # 技术栈演进
        considerations.append("3. **技术栈演进**")
        considerations.append("   - 跟踪技术发展趋势")
        considerations.append("   - 建立技术栈升级计划")
        considerations.append("   - 预留技术迁移空间")

        return "\n".join(considerations)

    def _format_components_overview(self, components: List[Dict]) -> str:
        """格式化组件概览"""
        if not components:
            return "暂无组件设计"

        overview = "### 组件概览\n"
        for comp in components:
            overview += f"- **{comp['name']}** ({comp['type']}): {comp['responsibility']}\n"

        return overview

    def _generate_component_details(self, components: List[Dict]) -> str:
        """生成组件详细说明"""
        if not components:
            return "暂无组件设计"

        details = "### 组件详细设计\n"
        for comp in components:
            details += f"#### {comp['name']}\n"
            details += f"**类型**: {comp['type']}\n"
            details += f"**职责**: {comp['responsibility']}\n"
            details += f"**接口**: {', '.join(comp['interfaces'])}\n"
            if comp['dependencies']:
                details += f"**依赖**: {', '.join(comp['dependencies'])}\n"
            details += "\n"

        return details

    def _generate_data_flow_details(self, data_flow: List[str], components: List[Dict]) -> str:
        """生成数据流详细说明"""
        if not data_flow:
            return "暂无数据流设计"

        details = "### 数据流设计\n"
        details += f"**主要数据流**: {data_flow[0] if data_flow else '暂无'}\n\n"

        details += "**组件间交互**:\n"
        for i, flow in enumerate(data_flow):
            if i < len(data_flow) - 1:
                details += f"{i+1}. {flow}\n"
            else:
                details += f"{i+1}. {flow} (流程结束)\n"

        return details

    def _format_performance_requirements(self, perf_req: Dict) -> str:
        """格式化性能需求"""
        if not perf_req:
            return "暂无特殊性能需求"

        requirements = "### 性能需求\n"
        if "response_time" in perf_req:
            requirements += f"- **响应时间**: {perf_req['response_time']}\n"
        if "throughput" in perf_req:
            requirements += f"- **吞吐量**: {perf_req['throughput']}\n"
        if "concurrent_users" in perf_req:
            requirements += f"- **并发用户数**: {perf_req['concurrent_users']}\n"
        if "scalability_target" in perf_req:
            requirements += f"- **扩展目标**: {perf_req['scalability_target']}\n"

        return requirements

    def _format_availability_requirements(self, avail_req: Dict) -> str:
        """格式化可用性需求"""
        if not avail_req:
            return "暂无特殊可用性需求"

        requirements = "### 可用性需求\n"
        if "uptime_target" in avail_req:
            requirements += f"- **可用性目标**: {avail_req['uptime_target']}\n"
        if "recovery_time" in avail_req:
            requirements += f"- **恢复时间**: {avail_req['recovery_time']}\n"
        if "data_backup" in avail_req:
            requirements += f"- **数据备份**: {avail_req['data_backup']}\n"
        if "disaster_recovery" in avail_req:
            requirements += f"- **灾难恢复**: {avail_req['disaster_recovery']}\n"

        return requirements

    def _format_security_requirements(self, sec_req: Dict) -> str:
        """格式化安全需求"""
        if not sec_req:
            return "暂无特殊安全需求"

        requirements = "### 安全需求\n"
        if "authentication" in sec_req:
            requirements += f"- **身份认证**: {sec_req['authentication']}\n"
        if "authorization" in sec_req:
            requirements += f"- **权限控制**: {sec_req['authorization']}\n"
        if "data_encryption" in sec_req:
            requirements += f"- **数据加密**: {sec_req['data_encryption']}\n"
        if "security_scanning" in sec_req:
            requirements += f"- **安全扫描**: {sec_req['security_scanning']}\n"

        return requirements

    def _format_maintainability_requirements(self, maint_req: Dict) -> str:
        """格式化可维护性需求"""
        if not maint_req:
            return "暂无特殊可维护性需求"

        requirements = "### 可维护性需求\n"
        if "code_coverage" in maint_req:
            requirements += f"- **代码覆盖率**: {maint_req['code_coverage']}\n"
        if "documentation" in maint_req:
            requirements += f"- **文档要求**: {maint_req['documentation']}\n"
        if "logging" in maint_req:
            requirements += f"- **日志记录**: {maint_req['logging']}\n"
        if "monitoring" in maint_req:
            requirements += f"- **监控要求**: {maint_req['monitoring']}\n"

        return requirements

    def _generate_deployment_strategy(self, architecture_design: Dict) -> str:
        """生成部署策略"""
        pattern = architecture_design["pattern"]

        strategies = {
            "monolithic": [
                "部署单个应用包",
                "使用负载均衡器分发请求",
                "数据库读写分离",
                "静态资源CDN分发"
            ],
            "microservices": [
                "容器化部署",
                "Kubernetes编排管理",
                "服务自动扩缩容",
                "服务网格通信"
            ],
            "event_driven": [
                "事件处理器独立部署",
                "消息队列集群",
                "事件总线管理",
                "容器化部署"
            ],
            "layered": [
                "应用服务器集群",
                "数据库主从复制",
                "缓存集群部署",
                "负载均衡配置"
            ],
            "clean_architecture": [
                "容器化部署",
                "分层独立部署",
                "基础设施自动化",
                "数据库容器化"
            ]
        }

        pattern_name = pattern.value if isinstance(pattern, ArchitecturePattern) else pattern
        strategy_list = strategies.get(pattern_name, ["标准部署策略"])

        strategy = "### 部署策略\n"
        for i, item in enumerate(strategy_list, 1):
            strategy += f"{i}. {item}\n"

        return strategy

    def _generate_infrastructure_components(self, architecture_design: Dict) -> str:
        """生成基础设施组件"""
        components = architecture_design["components"]

        infrastructure = "### 基础设施组件\n"
        infra_components = set()

        for comp in components:
            comp_type = comp["type"]
            if comp_type == ComponentType.INFRASTRUCTURE.value:
                infra_components.add(comp["name"])
            elif comp_type == ComponentType.INTEGRATION.value:
                infra_components.add(comp["name"])

        if infra_components:
            for component in sorted(infra_components):
                infrastructure += f"- **{component}**: 负责相应的基础设施功能\n"

        return infrastructure

    def _generate_implementation_phases(self, architecture_design: Dict) -> str:
        """生成实施阶段"""
        phases = [
            "### 第一阶段：基础设施搭建",
            "1. 开发环境和工具链配置",
            "2. 基础设施组件部署",
            "3. CI/CD流水线建立",
            "4. 监控和日志系统配置",
            "",
            "### 第二阶段：核心功能开发",
            "1. 核心组件开发",
            "2. 数据模型设计",
            "3 API接口实现",
            "4. 基础功能测试",
            "",
            "### 第三阶段：集成测试",
            "1. 组件集成测试",
            "2. 端到端测试",
            "3. 性能测试和优化",
            "4. 安全测试和加固",
            "",
            "### 第四阶段：部署上线",
            "1. 生产环境部署",
            "2. 数据迁移（如需要）",
            "3. 灰度发布",
            "4. 生产监控和观察"
        ]

        return phases

    def _generate_migration_strategy(self, architecture_design: Dict) -> str:
        """生成迁移策略"""
        strategy = "### 迁移策略\n"

        strategy += "**现有系统评估**:\n"
        strategy += "- 分析现有系统架构和技术栈\n"
        strategy += "- 识别迁移风险和依赖关系\n"
        strategy += "- 评估业务连续性要求\n\n"

        strategy += "**迁移方法**:\n"
        strategy += "- 蓝绿迁移：直接部署新系统",
            "- 蓝蓝迁移：新老系统并行运行",
            "- 滚动迁移：逐步替换系统组件\n"

        strategy += "**风险控制**:\n"
        strategy += "- 建立回滚机制",
            "- 数据一致性验证",
            "- 性能监控和对比",
            "- 用户培训和适应"

        return strategy

    def _generate_monitoring_plan(self, architecture_design: Dict) -> str:
        """生成监控计划"""
        plan = "### 监控计划\n"

        plan += "**应用监控**:\n"
        plan += "- 应用性能指标监控",
        plan += "- 错误率和异常监控",
        plan += "- 用户行为分析",
        plan += "- 业务指标跟踪\n\n"

        plan += "**基础设施监控**:\n"
        plan += "- 服务器资源监控",
        plan += "- 网络流量监控",
        plan += "- 数据库性能监控",
        plan += "- 安全事件监控\n\n"

        plan += "**告警机制**:\n"
        plan += "- 关键指标阈值告警",
        plan += "- 异常情况自动通知",
        plan += "- 多渠道告警通知",
        plan += "- 告警级别分类"

        return plan

def main():
    """命令行接口"""
    import sys
    import json

    if len(sys.argv) < 4:
        print("用法: python report_generator.py <报告类型> <项目名称> <数据文件>")
        print("报告类型: tech_selection, architecture_design")
        print("示例: python report_generator.py tech_selection myapp tech_analysis.json")
        sys.exit(1)

    report_type = sys.argv[1]
    project_name = sys.argv[2]
    data_file = sys.argv[3]

    generator = ReportGenerator(".")

    try:
        # 读取数据文件
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if report_type == "tech_selection":
            # 需要先进行技术分析
            # 这里应该调用tech_selector.py
            tech_analysis = {"mock": "data"}  # 实际使用时应该调用tech_selector
            result = generator.generate_tech_selection_report(project_name, tech_analysis, data)
        elif report_type == "architecture_design":
            # 需要先进行架构设计
            # 这里应该调用architecture_designer.py
            architecture_design = {"mock": "data"}  # 实际使用时应该调用architecture_designer
            result = generator.generate_architecture_design_report(project_name, architecture_design)
        else:
            raise ValueError(f"不支持的报告类型: {report_type}")

        print(f"报告生成成功!")
        print(f"文件路径: {result}")

    except Exception as e:
        print(f"生成报告失败: {str(e)}")

if __name__ == "__main__":
    main()