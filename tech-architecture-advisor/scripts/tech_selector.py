#!/usr/bin/env python3
"""
技术选型分析器
提供技术栈对比分析、评估和推荐功能
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class ProjectType(Enum):
    WEB_APPLICATION = "web_application"
    MICROSERVICES = "microservices"
    BIG_DATA = "big_data"
    MOBILE_APPLICATION = "mobile_application"
    ENTERPRISE_APPLICATION = "enterprise_application"
    AI_ML_SYSTEM = "ai_ml_system"

class ScaleLevel(Enum):
    SMALL = "small"          # < 1000 用户
    MEDIUM = "medium"        # 1000-10000 用户
    LARGE = "large"          # 10000-100000 用户
    VERY_LARGE = "very_large" # > 100000 用户

@dataclass TechStack:
    def __init__(self, name, language, framework, database, deployment, pros, cons, learning_curve, community_support, performance, scalability):
        self.name = name
        self.language = language
        self.framework = framework
        self.database = database
        self.deployment = deployment
        self.pros = pros
        self.cons = cons
        self.learning_curve = learning_curve
        self.community_support = community_support
        self.performance = performance
        self.scalability = scalability

    def to_dict(self):
        return {
            "name": self.name,
            "language": self.language,
            "framework": self.framework,
            "database": self.database,
            "deployment": self.deployment,
            "pros": self.pros,
            "cons": self.cons,
            "learning_curve": self.learning_curve,
            "community_support": self.community_support,
            "performance": self.performance,
            "scalability": self.scalability
        }

@dataclass
class ProjectRequirements:
    project_type: ProjectType
    scale_level: ScaleLevel
    performance_requirements: List[str]
    security_requirements: List[str]
    team_skills: List[str]
    budget_constraints: str
    timeline: str
    domain_knowledge: str

class TechSelector:
    def __init__(self):
        self.tech_stacks = self._initialize_tech_stacks()
        self.comparison_criteria = self._initialize_criteria()

    def _initialize_tech_stacks(self) -> Dict[str, TechStack]:
        """初始化技术栈数据库"""
        return {
            "java_spring": TechStack(
                name="Java + Spring Boot",
                language="Java",
                framework="Spring Boot",
                database="PostgreSQL/MySQL",
                deployment="Docker/Kubernetes",
                pros=["成熟稳定", "企业级支持", "丰富的生态系统", "类型安全"],
                cons=["学习曲线陡峭", "内存占用较高", "启动时间较长"],
                learning_curve="高",
                community_support="优秀",
                performance="高",
                scalability="优秀"
            ),
            "python_django": TechStack(
                name="Python + Django",
                language="Python",
                framework="Django",
                database="PostgreSQL/MySQL",
                deployment="Docker/Heroku",
                pros=["开发效率高", "语法简洁", "丰富的库", "快速原型开发"],
                cons=["性能相对较低", "GIL限制", "类型安全不足"],
                learning_curve="中等",
                community_support="优秀",
                performance="中等",
                scalability="中等"
            ),
            "nodejs_express": TechStack(
                name="Node.js + Express",
                language="JavaScript/TypeScript",
                framework="Express",
                database="MongoDB/PostgreSQL",
                deployment="Docker/AWS",
                pros=["前端后端统一语言", "生态活跃", "高并发处理", "开发速度快"],
                cons=["单线程限制", "回调地狱", "内存管理"],
                learning_curve="中等",
                community_support="优秀",
                performance="高",
                scalability="良好"
            ),
            "go_gin": TechStack(
                name="Go + Gin",
                language="Go",
                framework="Gin",
                database="PostgreSQL/MongoDB",
                deployment="Docker/Kubernetes",
                pros=["性能优秀", "并发处理强", "编译型语言", "部署简单"],
                cons=["生态系统较小", "库相对较少", "错误处理较基础"],
                learning_curve="中等",
                community_support="良好",
                performance="优秀",
                scalability="优秀"
            ),
            "net_core": TechStack(
                name=".NET Core",
                language="C#",
                framework="ASP.NET Core",
                database="SQL Server/PostgreSQL",
                deployment="Docker/Azure",
                pros=["企业级支持", "性能优秀", "类型安全", "微软生态"],
                cons=["平台限制", "学习曲线陡峭", "开源生态相对较小"],
                learning_curve="高",
                community_support="良好",
                performance="优秀",
                scalability="优秀"
            )
        }

    def _initialize_criteria(self) -> Dict[str, Dict]:
        """初始化评估标准"""
        return {
            "performance": {
                "high": {"java_spring": 9, "go_gin": 10, "net_core": 9, "nodejs_express": 8, "python_django": 6},
                "medium": {"java_spring": 8, "go_gin": 9, "net_core": 8, "nodejs_express": 7, "python_django": 7},
                "low": {"java_spring": 7, "go_gin": 8, "net_core": 7, "nodejs_express": 7, "python_django": 8}
            },
            "scalability": {
                "very_large": {"java_spring": 9, "go_gin": 9, "net_core": 9, "nodejs_express": 7, "python_django": 5},
                "large": {"java_spring": 8, "go_gin": 9, "net_core": 8, "nodejs_express": 8, "python_django": 6},
                "medium": {"java_spring": 7, "go_gin": 8, "net_core": 7, "nodejs_express": 7, "python_django": 8},
                "small": {"java_spring": 6, "go_gin": 7, "net_core": 6, "nodejs_express": 8, "python_django": 9}
            },
            "development_speed": {
                "fast": {"python_django": 9, "nodejs_express": 9, "go_gin": 7, "java_spring": 5, "net_core": 5},
                "medium": {"python_django": 8, "nodejs_express": 8, "go_gin": 8, "java_spring": 6, "net_core": 6},
                "slow": {"python_django": 7, "nodejs_express": 7, "go_gin": 7, "java_spring": 7, "net_core": 7}
            },
            "team_skills": {
                "java": {"java_spring": 9, "net_core": 7, "go_gin": 6, "nodejs_express": 5, "python_django": 4},
                "python": {"python_django": 9, "nodejs_express": 8, "go_gin": 5, "java_spring": 4, "net_core": 3},
                "javascript": {"nodejs_express": 9, "python_django": 7, "go_gin": 5, "java_spring": 3, "net_core": 3},
                "csharp": {"net_core": 9, "java_spring": 7, "go_gin": 4, "nodejs_express": 3, "python_django": 2},
                "go": {"go_gin": 9, "java_spring": 6, "net_core": 4, "nodejs_express": 4, "python_django": 3},
                "beginner": {"python_django": 9, "nodejs_express": 8, "go_gin": 6, "java_spring": 4, "net_core": 3}
            },
            "security": {
                "high": {"java_spring": 9, "net_core": 9, "go_gin": 8, "python_django": 7, "nodejs_express": 7},
                "medium": {"java_spring": 8, "net_core": 8, "go_gin": 7, "python_django": 8, "nodejs_express": 7},
                "low": {"java_spring": 7, "net_core": 7, "go_gin": 6, "python_django": 6, "nodejs_express": 6}
            }
        }

    def analyze_requirements(self, project_data: Dict) -> ProjectRequirements:
        """分析项目需求"""
        project_type = ProjectType(project_data.get("project_type", "web_application"))
        scale_level = ScaleLevel(project_data.get("scale_level", "medium"))

        return ProjectRequirements(
            project_type=project_type,
            scale_level=scale_level,
            performance_requirements=project_data.get("performance_requirements", []),
            security_requirements=project_data.get("security_requirements", []),
            team_skills=project_data.get("team_skills", []),
            budget_constraints=project_data.get("budget_constraints", "medium"),
            timeline=project_data.get("timeline", "medium"),
            domain_knowledge=project_data.get("domain_knowledge", "general")
        )

    def evaluate_tech_stack(self, tech_name: str, requirements: ProjectRequirements) -> Dict:
        """评估技术栈适用性"""
        if tech_name not in self.tech_stacks:
            return {"error": f"未找到技术栈: {tech_name}"}

        tech = self.tech_stacks[tech_name]
        scores = {}

        # 性能评分
        if "high" in requirements.performance_requirements:
            scores["performance"] = self.comparison_criteria["performance"]["high"].get(tech_name, 5)
        elif "medium" in requirements.performance_requirements:
            scores["performance"] = self.comparison_criteria["performance"]["medium"].get(tech_name, 5)
        else:
            scores["performance"] = self.comparison_criteria["performance"]["low"].get(tech_name, 5)

        # 可扩展性评分
        scale_key = requirements.scale_level.value
        scores["scalability"] = self.comparison_criteria["scalability"][scale_key].get(tech_name, 5)

        # 开发速度评分
        if requirements.timeline == "fast":
            scores["development_speed"] = self.comparison_criteria["development_speed"]["fast"].get(tech_name, 5)
        elif requirements.timeline == "medium":
            scores["development_speed"] = self.comparison_criteria["development_speed"]["medium"].get(tech_name, 5)
        else:
            scores["development_speed"] = self.comparison_criteria["development_speed"]["slow"].get(tech_name, 5)

        # 团队技能匹配度
        team_score = 0
        for skill in requirements.team_skills:
            if skill in self.comparison_criteria["team_skills"]:
                team_score = max(team_score, self.comparison_criteria["team_skills"][skill].get(tech_name, 5))
        scores["team_fit"] = team_score if team_score > 0 else 3  # 如果没有匹配技能，给中性分数

        # 安全性评分
        if "high" in requirements.security_requirements:
            scores["security"] = self.comparison_criteria["security"]["high"].get(tech_name, 5)
        elif "medium" in requirements.security_requirements:
            scores["security"] = self.comparison_criteria["security"]["medium"].get(tech_name, 5)
        else:
            scores["security"] = self.comparison_criteria["security"]["low"].get(tech_name, 5)

        # 综合评分
        total_score = sum(scores.values()) / len(scores)
        scores["overall"] = total_score

        return {
            "tech_name": tech_name,
            "tech_info": tech,
            "scores": scores,
            "recommendation": self._generate_recommendation(tech, scores, requirements)
        }

    def _generate_recommendation(self, tech: TechStack, scores: Dict, requirements: ProjectRequirements) -> str:
        """生成推荐语"""
        score = scores["overall"]

        if score >= 8:
            return f"强烈推荐。{tech.name}在性能、可扩展性和生态系统方面表现出色，非常适合{requirements.project_type.value}项目。"
        elif score >= 6:
            return f"推荐。{tech.name}是一个不错的选择，在多个维度表现良好，可以考虑作为技术栈选项。"
        elif score >= 4:
            return f"可以考虑。{tech.name}有一些限制，但在特定场景下可能适用，需要仔细评估风险。"
        else:
            return f"不推荐。{tech.name}与项目需求匹配度较低，建议考虑其他技术栈选项。"

    def compare_tech_stacks(self, requirements: ProjectRequirements) -> Dict:
        """对比技术栈"""
        results = {}

        for tech_name in self.tech_stacks.keys():
            results[tech_name] = self.evaluate_tech_stack(tech_name, requirements)

        # 按综合评分排序
        sorted_results = sorted(results.items(), key=lambda x: x[1]["scores"]["overall"], reverse=True)

        return {
            "comparison_results": dict(sorted_results),
            "top_recommendation": sorted_results[0][1] if sorted_results else None,
            "analysis_summary": self._generate_analysis_summary(dict(sorted_results), requirements)
        }

    def _generate_analysis_summary(self, results: Dict, requirements: ProjectRequirements) -> str:
        """生成分析总结"""
        if not results:
            return "无法生成分析总结。"

        top_tech = list(results.keys())[0]
        top_score = results[top_tech]["scores"]["overall"]

        summary = f"基于项目需求分析，推荐使用 {results[top_tech]['tech_info']['name']} (综合评分: {top_score:.1f}/10)。\n\n"

        summary += "主要优势：\n"
        for pro in results[top_tech]["tech_info"].pros[:3]:
            summary += f"- {pro}\n"

        summary += "\n需要考虑的因素：\n"
        for con in results[top_tech]["tech_info"].cons[:3]:
            summary += f"- {con}\n"

        return summary

def main():
    """命令行接口"""
    import sys
    import json

    if len(sys.argv) < 3:
        print("用法: python tech_selector.py <技术栈名称> <项目数据JSON文件>")
        print("示例: python tech_selector.py java_spring project_data.json")
        sys.exit(1)

    tech_name = sys.argv[1]
    project_file = sys.argv[2]

    selector = TechSelector()

    try:
        # 读取项目数据
        with open(project_file, 'r', encoding='utf-8') as f:
            project_data = json.load(f)

        # 分析需求
        requirements = selector.analyze_requirements(project_data)

        # 评估技术栈
        if tech_name == "all":
            result = selector.compare_tech_stacks(requirements)
        else:
            result = selector.evaluate_tech_stack(tech_name, requirements)

        print(json.dumps(result, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"分析失败: {str(e)}")

if __name__ == "__main__":
    main()