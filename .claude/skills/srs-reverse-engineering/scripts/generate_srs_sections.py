#!/usr/bin/env python3
"""
SRS章节生成脚本
用于根据分析结果生成SRS文档的各个章节
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime
import sys

class SRSSectionGenerator:
    def __init__(self, template_path: str = None):
        self.template_path = template_path or "assets/srs-markdown-template.md"
        self.srs_content = {
            "project_info": {},
            "introduction": "",
            "functional_requirements": "",
            "non_functional_requirements": "",
            "interface_requirements": "",
            "data_requirements": "",
            "system_architecture": "",
            "appendix": ""
        }

    def generate_srs(self, project_analysis: Dict, api_analysis: Dict, db_analysis: Dict) -> str:
        """生成完整的SRS文档"""
        self._extract_project_info(project_analysis)
        self._generate_introduction(project_analysis)
        self._generate_functional_requirements(project_analysis, api_analysis)
        self._generate_non_functional_requirements(project_analysis)
        self._generate_interface_requirements(api_analysis)
        self._generate_data_requirements(db_analysis)
        self._generate_system_architecture(project_analysis)
        self._generate_appendix()

        return self._compile_srs_document()

    def _extract_project_info(self, project_analysis: Dict):
        """提取项目基本信息"""
        project_info = project_analysis.get("project_info", {})
        self.srs_content["project_info"] = {
            "name": project_info.get("name", "Unknown Project"),
            "version": project_info.get("version", "1.0.0"),
            "description": project_info.get("description", ""),
            "tech_stack": project_analysis.get("tech_stack", {}),
            "creation_date": datetime.now().strftime("%Y-%m-%d")
        }

    def _generate_introduction(self, project_analysis: Dict):
        """生成引言章节"""
        project_info = self.srs_content["project_info"]
        tech_stack = project_analysis.get("tech_stack", {})

        introduction = f"""## 1. 引言

### 1.1 文档目的
本文档旨在详细描述 {project_info['name']} 的软件需求规格，作为开发、测试、验收的最终依据。通过明确的功能性和非功能性需求定义，确保项目各相关方对需求有一致的理解，为项目成功实施奠定基础。

### 1.2 项目背景
本项目基于现有代码库进行反向工程分析，技术栈包括：
"""

        # 添加技术栈信息
        for category, technologies in tech_stack.items():
            if technologies:
                introduction += f"- **{category}**: {', '.join(technologies)}\n"

        introduction += f"""
### 1.3 项目范围
本SRS文档基于对项目代码的深入分析生成，涵盖以下内容：
- 系统功能性需求分析
- 非功能性需求定义
- 接口规范说明
- 数据模型设计
- 系统架构描述

### 1.4 术语定义
| 术语 | 定义 |
|------|------|
| SRS | Software Requirements Specification (软件需求规格说明书) |
| API | Application Programming Interface (应用程序编程接口) |
| {project_info['name'].upper()} | {project_info['description']} |

### 1.5 参考文档
- 项目源代码分析报告
- API接口分析报告
- 数据库模式分析报告
"""

        self.srs_content["introduction"] = introduction

    def _generate_functional_requirements(self, project_analysis: Dict, api_analysis: Dict):
        """生成功能性需求章节"""
        functional_requirements = "## 3. 功能性需求\n\n"

        # 从API分析中提取功能需求
        rest_apis = api_analysis.get("rest_apis", [])
        if rest_apis:
            functional_requirements += "### 3.1 API功能需求\n\n"

            # 按路径分组API
            api_groups = {}
            for api in rest_apis:
                path = api['path']
                base_path = '/'.join(path.split('/')[:3]) if '/' in path else path
                if base_path not in api_groups:
                    api_groups[base_path] = []
                api_groups[base_path].append(api)

            for base_path, apis in api_groups.items():
                functional_requirements += f"#### 3.1.{list(api_groups.keys()).index(base_path) + 1} {base_path} 模块\n\n"

                for api in apis:
                    functional_requirements += f"""**{api['method']} {api['path']}**
- **功能描述**: 基于路径推断的{api['method'].lower()}操作
- **所在文件**: {api['file']}
- **实现框架**: {api['framework']}
- **输入参数**: 需要根据具体业务逻辑定义
- **输出格式**: JSON格式响应
- **异常处理**: 标准HTTP状态码和错误信息

"""

        # 从项目结构中提取功能模块
        key_files = project_analysis.get("key_files", [])
        functional_modules = [f for f in key_files if "src" in f.get("path", "").lower() or "app" in f.get("path", "").lower()]

        if functional_modules:
            functional_requirements += "### 3.2 核心功能模块\n\n"
            for i, module in enumerate(functional_modules[:5], 1):  # 限制显示前5个
                functional_requirements += f"""#### 3.2.{i} {module['description']}
- **文件路径**: {module['path']}
- **功能说明**: 基于文件名推断的核心业务功能
- **主要职责**: 处理相关的业务逻辑和数据操作

"""

        self.srs_content["functional_requirements"] = functional_requirements

    def _generate_non_functional_requirements(self, project_analysis: Dict):
        """生成非功能性需求章节"""
        non_functional_requirements = """## 4. 非功能性需求

### 4.1 性能需求
#### 4.1.1 响应时间要求
| 操作类型 | 响应时间要求 | 说明 |
|----------|--------------|------|
| 页面加载 | < 3秒 | 正常网络条件下 |
| API接口调用 | < 500ms | 单用户请求 |
| 数据查询 | < 2秒 | 复杂查询条件 |
| 文件上传 | < 30秒 | 10MB以内文件 |

#### 4.1.2 并发处理能力
| 指标 | 要求 | 测试方法 |
|------|------|----------|
| 同时在线用户 | > 1,000 | 压力测试 |
| 每秒请求数(RPS) | > 500 | 性能测试 |
| 数据库连接池 | > 50 | 连接池监控 |

### 4.2 安全性需求
#### 4.2.1 身份认证与授权
- 支持用户名密码认证
- 实施基于角色的访问控制(RBAC)
- 会话管理：超时时间30分钟
- 敏感操作需要二次验证

#### 4.2.2 数据安全
- 传输层加密：HTTPS/TLS 1.3
- 敏感数据存储加密
- 定期安全审计和漏洞扫描
- 访问日志记录和监控

### 4.3 可靠性需求
- 系统可用性：99.5% (每月宕机时间 < 3.6小时)
- 故障恢复时间：< 1小时
- 数据备份：每日自动备份，保留30天
- 监控告警：7x24小时监控

### 4.4 可用性需求
- 支持现代浏览器（Chrome 90+, Firefox 88+, Safari 14+）
- 响应式设计，支持桌面端和移动端
- 界面语言：中文
- 操作引导和帮助文档

### 4.5 兼容性需求
#### 4.5.1 浏览器兼容性
| 浏览器 | 最低版本 | 支持状态 |
|--------|----------|----------|
| Chrome | 90+ | 完全支持 |
| Firefox | 88+ | 完全支持 |
| Safari | 14+ | 完全支持 |
| Edge | 90+ | 完全支持 |

#### 4.5.2 移动端兼容性
| 平台 | 最低版本 | 支持状态 |
|------|----------|----------|
| iOS | 13.0+ | 完全支持 |
| Android | 8.0+ | 完全支持 |

"""

        self.srs_content["non_functional_requirements"] = non_functional_requirements

    def _generate_interface_requirements(self, api_analysis: Dict):
        """生成接口需求章节"""
        interface_requirements = "## 5. 接口需求\n\n"

        rest_apis = api_analysis.get("rest_apis", [])
        if rest_apis:
            interface_requirements += "### 5.1 REST API接口\n\n"
            interface_requirements += "#### 5.1.1 API设计规范\n"
            interface_requirements += "- 遵循RESTful设计原则\n"
            interface_requirements += "- 使用JSON格式进行数据交换\n"
            interface_requirements += "- 统一的错误响应格式\n"
            interface_requirements += "- API版本控制：/api/v1/\n\n"

            interface_requirements += "#### 5.1.2 已识别的API端点\n\n"

            # 按HTTP方法分组
            api_by_method = {}
            for api in rest_apis:
                method = api['method']
                if method not in api_by_method:
                    api_by_method[method] = []
                api_by_method[method].append(api)

            for method in ['GET', 'POST', 'PUT', 'DELETE']:
                if method in api_by_method:
                    interface_requirements += f"**{method} 方法端点：**\n\n"
                    for api in api_by_method[method]:
                        interface_requirements += f"- `{method} {api['path']}` - 所在文件: {api['file']}\n"
                    interface_requirements += "\n"

        # WebSocket接口
        websocket_endpoints = api_analysis.get("websocket_endpoints", [])
        if websocket_endpoints:
            interface_requirements += "### 5.2 WebSocket接口\n\n"
            for ws in websocket_endpoints:
                interface_requirements += f"**文件**: {ws['file']}\n"
                interface_requirements += "**端点**:\n"
                for endpoint in ws['endpoints']:
                    interface_requirements += f"- `{endpoint}`\n"
                interface_requirements += "\n"

        # 外部API调用
        external_apis = api_analysis.get("external_apis", [])
        if external_apis:
            interface_requirements += "### 5.3 外部API集成\n\n"
            interface_requirements += "系统需要与以下外部服务集成：\n\n"
            for api in external_apis:
                interface_requirements += f"- **{api}**: 用于外部数据交换和服务调用\n"
            interface_requirements += "\n"

        self.srs_content["interface_requirements"] = interface_requirements

    def _generate_data_requirements(self, db_analysis: Dict):
        """生成数据需求章节"""
        data_requirements = "## 6. 数据需求\n\n"

        # 数据库类型
        db_type = db_analysis.get("database_type", [])
        if db_type:
            data_requirements += "### 6.1 数据库技术栈\n\n"
            data_requirements += "**数据库类型**: " + ", ".join(db_type) + "\n\n"

        # 数据模型
        models = db_analysis.get("models", [])
        if models:
            data_requirements += "### 6.2 数据模型\n\n"

            model_count = 0
            for model_group in models:
                if "models" in model_group:
                    for model in model_group["models"]:
                        if model_count >= 5:  # 限制显示前5个模型
                            break

                        model_name = model.get("name", "Unknown")
                        table_name = model.get("table_name", model_name.lower())
                        file_path = model.get("file", "")

                        data_requirements += f"#### 6.2.{model_count + 1} {model_name}\n\n"
                        data_requirements += f"- **表名**: {table_name}\n"
                        data_requirements += f"- **定义文件**: {file_path}\n"

                        # 添加字段信息
                        if "columns" in model:
                            data_requirements += "- **字段**:\n"
                            for col in model["columns"][:5]:  # 限制显示前5个字段
                                col_name = col.get("name", "")
                                col_def = col.get("definition", "")
                                data_requirements += f"  - `{col_name}`: {col_def}\n"

                        # 添加字段信息
                        if "fields" in model:
                            data_requirements += "- **字段**:\n"
                            for field in model["fields"][:5]:  # 限制显示前5个字段
                                field_name = field.get("name", "")
                                field_type = field.get("type", "")
                                data_requirements += f"  - `{field_name}`: {field_type}\n"

                        data_requirements += "\n"
                        model_count += 1

        # 数据关系
        relationships = db_analysis.get("relationships", [])
        if relationships:
            data_requirements += "### 6.3 数据关系\n\n"
            data_requirements += "识别到以下数据关系：\n\n"

            rel_types = {}
            for rel in relationships:
                rel_type = rel.get("type", "")
                if rel_type not in rel_types:
                    rel_types[rel_type] = []
                rel_types[rel_type].append(rel)

            for rel_type, rels in rel_types.items():
                data_requirements += f"**{rel_type}**:\n"
                for rel in rels[:3]:  # 限制显示前3个关系
                    target = rel.get("target", "")
                    file_path = rel.get("file", "")
                    data_requirements += f"- 与 `{target}` 的关系 - 定义在 {file_path}\n"
                data_requirements += "\n"

        # 数据约束
        constraints = db_analysis.get("constraints", [])
        if constraints:
            data_requirements += "### 6.4 数据约束\n\n"
            data_requirements += "**数据库约束**:\n\n"

            constraint_types = {}
            for constraint in constraints:
                c_type = constraint.get("type", "")
                if c_type not in constraint_types:
                    constraint_types[c_type] = []
                constraint_types[c_type].append(constraint)

            for c_type, constraints_list in constraint_types.items():
                data_requirements += f"- **{c_type}**: 在以下文件中定义\n"
                for constraint in constraints_list[:3]:  # 限制显示前3个约束
                    file_path = constraint.get("file", "")
                    data_requirements += f"  - {file_path}\n"
                data_requirements += "\n"

        self.srs_content["data_requirements"] = data_requirements

    def _generate_system_architecture(self, project_analysis: Dict):
        """生成系统架构章节"""
        architecture = "## 7. 系统架构\n\n"

        tech_stack = project_analysis.get("tech_stack", {})

        architecture += "### 7.1 技术架构\n\n"
        architecture += "基于代码分析，系统采用以下技术架构：\n\n"

        # 前端技术
        frontend = tech_stack.get("frontend", [])
        if frontend:
            architecture += f"#### 7.1.1 前端架构\n"
            architecture += f"- **前端框架**: {', '.join(frontend)}\n"
            architecture += "- **架构模式**: 组件化开发\n"
            architecture += "- **状态管理**: 根据框架特性选择\n"
            architecture += "- **构建工具**: Webpack/Vite等现代构建工具\n\n"

        # 后端技术
        backend = tech_stack.get("backend", [])
        if backend:
            architecture += f"#### 7.1.2 后端架构\n"
            architecture += f"- **后端框架**: {', '.join(backend)}\n"
            architecture += "- **架构模式**: MVC/MVVM等设计模式\n"
            architecture += "- **API设计**: RESTful API风格\n"
            architecture += "- **数据处理**: 分层架构设计\n\n"

        # 数据库技术
        database = tech_stack.get("database", [])
        if database:
            architecture += f"#### 7.1.3 数据架构\n"
            architecture += f"- **数据库**: {', '.join(database)}\n"
            architecture += "- **数据访问**: ORM框架支持\n"
            architecture += "- **缓存策略**: Redis等缓存技术\n"
            architecture += "- **数据备份**: 定期备份策略\n\n"

        # 架构图描述
        architecture += "### 7.2 系统架构图\n\n"
        architecture += "```\n"
        architecture += "┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐\n"
        architecture += "│   前端应用      │    │   移动端应用    │    │   管理后台      │\n"
        architecture += "└─────────────────┘    └─────────────────┘    └─────────────────┘\n"
        architecture += "         │                       │                       │\n"
        architecture += "         └───────────────────────┼───────────────────────┘\n"
        architecture += "                                 │\n"
        architecture += "                    ┌─────────────────┐\n"
        architecture += "                    │   API网关       │\n"
        architecture += "                    └─────────────────┘\n"
        architecture += "                                 │\n"
        architecture += "                    ┌─────────────────┐\n"
        architecture += "                    │   业务服务层    │\n"
        architecture += "                    └─────────────────┘\n"
        architecture += "                                 │\n"
        architecture += "         ┌───────────────────────┼───────────────────────┐\n"
        architecture += "         │                       │                       │\n"
        architecture += "┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐\n"
        architecture += "│   缓存服务      │    │   数据库        │    │   消息队列      │\n"
        architecture += "└─────────────────┘    └─────────────────┘    └─────────────────┘\n"
        architecture += "```\n\n"

        architecture += "### 7.3 部署架构\n\n"
        architecture += "- **部署方式**: 容器化部署 (Docker)\n"
        architecture += "- **负载均衡**: Nginx反向代理\n"
        architecture += "- **服务发现**: 基于配置的服务注册\n"
        architecture += "- **监控告警**: 应用性能监控和日志收集\n\n"

        self.srs_content["system_architecture"] = architecture

    def _generate_appendix(self):
        """生成附录章节"""
        appendix = """## 10. 附录

### 10.1 文档信息
- **文档版本**: 1.0
- **创建日期**: {date}
- **生成方式**: 基于代码自动分析生成
- **分析工具**: SRS Generator v1.0

### 10.2 分析说明
本SRS文档通过以下步骤自动生成：
1. 项目结构分析 - 识别技术栈和项目架构
2. API端点提取 - 分析REST API和WebSocket接口
3. 数据库模式分析 - 提取数据模型和关系
4. 需求综合整理 - 生成完整的需求规格说明

### 10.3 注意事项
- 本文档基于代码静态分析生成，部分业务逻辑需要人工补充
- 建议结合PRD文档和用户访谈进行需求验证
- 技术细节需要根据实际实现情况进行调整
- 非功能性需求需要根据具体业务场景定制

### 10.4 后续工作
- 与产品经理确认业务需求
- 与技术团队确认技术方案
- 制定详细的开发计划和测试策略
- 定期更新和维护SRS文档
""".format(date=datetime.now().strftime("%Y-%m-%d"))

        self.srs_content["appendix"] = appendix

    def _compile_srs_document(self) -> str:
        """编译完整的SRS文档"""
        project_info = self.srs_content["project_info"]

        # 文档头部
        document = f"""# {project_info['name']} - 软件需求规格说明书

> **文档版本**: {project_info['version']}
> **创建日期**: {project_info['creation_date']}
> **生成方式**: 基于代码自动分析

---

## 📋 项目信息

| 项目 | 内容 |
|------|------|
| **项目名称** | {project_info['name']} |
| **项目描述** | {project_info['description']} |
| **文档版本** | {project_info['version']} |
| **技术栈** | {', '.join([f'{k}: {v}' for k, v in project_info['tech_stack'].items() if v])} |

---

"""

        # 添加各个章节
        sections = [
            ("introduction", "引言"),
            ("functional_requirements", "功能性需求"),
            ("non_functional_requirements", "非功能性需求"),
            ("interface_requirements", "接口需求"),
            ("data_requirements", "数据需求"),
            ("system_architecture", "系统架构"),
            ("appendix", "附录")
        ]

        for section_key, section_title in sections:
            content = self.srs_content.get(section_key, "")
            if content:
                document += content + "\n"

        # 文档尾部
        document += """
---

> **文档说明**: 本文档由SRS Generator自动生成，基于对项目代码的深入分析。建议结合人工审核和业务需求确认来完善最终的需求规格说明。
"""

        return document

    def extract_project_name_from_path(self, project_path: str) -> str:
        """从项目路径提取项目名"""
        path = Path(project_path)
        return path.name

    def save_srs(self, content: str, output_path: str, project_name: str = None):
        """保存SRS文档"""
        # 如果没有指定项目名，尝试从内容中提取
        if not project_name:
            # 尝试从文档标题中提取项目名
            lines = content.split('\n')
            for line in lines:
                if line.startswith('# '):
                    project_name = line[2:].split(' - ')[0].strip()
                    break

        if project_name:
            # 清理项目名，移除特殊字符
            clean_name = ''.join(c for c in project_name if c.isalnum() or c in ('-', '_'))
            if clean_name:
                # 构造新的文件名
                new_filename = f"{clean_name}_SRS.md"
                output_dir = Path(output_path).parent
                output_path = output_dir / new_filename
                print(f"使用项目名命名: {new_filename}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SRS文档已保存到: {output_path}")
        return output_path

def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description="生成SRS文档")
    parser.add_argument("--project", required=True, help="项目分析结果JSON文件")
    parser.add_argument("--api", required=True, help="API分析结果JSON文件")
    parser.add_argument("--database", required=True, help="数据库分析结果JSON文件")
    parser.add_argument("--output", "-o", default="srs-document.md", help="输出SRS文档路径")
    parser.add_argument("--template", help="SRS模板文件路径")
    parser.add_argument("--project-path", help="原始项目路径，用于提取项目名")

    args = parser.parse_args()

    # 读取分析结果
    with open(args.project, 'r', encoding='utf-8') as f:
        project_analysis = json.load(f)

    with open(args.api, 'r', encoding='utf-8') as f:
        api_analysis = json.load(f)

    with open(args.database, 'r', encoding='utf-8') as f:
        db_analysis = json.load(f)

    # 生成SRS文档
    generator = SRSSectionGenerator(args.template)
    srs_content = generator.generate_srs(project_analysis, api_analysis, db_analysis)

    # 提取项目名
    project_name = None
    if args.project_path:
        project_name = generator.extract_project_name_from_path(args.project_path)

    # 计算输出到skill目录外的路径
    skill_dir = Path(__file__).parent.parent
    output_dir = skill_dir.parent

    # 构造最终输出路径
    output_path = output_dir / Path(args.output).name

    # 保存文档
    final_path = generator.save_srs(srs_content, str(output_path), project_name)
    print(f"最终文件位置: {final_path}")

if __name__ == "__main__":
    main()