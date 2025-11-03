---
name: srs-reverse-engineering
description: This skill should be used when users need to reverse-engineer existing projects (from GitHub URLs or local files) and generate comprehensive Software Requirements Specification (SRS) documents that serve as development contracts. It analyzes codebases, extracts technical requirements, and converts PRDs into detailed technical specifications.
license: MIT
---

# SRS Reverse Engineering

This skill reverse-engineers existing projects to generate comprehensive Software Requirements Specification (SRS) documents that serve as development contracts between technical teams and stakeholders.

## What This Skill Provides

1. **Project Analysis** - Automated analysis of GitHub repositories or local codebases
2. **Technical Requirements Extraction** - Extract functional and non-functional requirements from existing code
3. **SRS Document Generation** - Generate IEEE 830-compliant SRS documents
4. **Architecture Documentation** - Document system architecture, APIs, and data models
5. **Development Contract Creation** - Create precise specifications that serve as binding development agreements

## When to Use This Skill

Use this skill when users request any of the following:

- "Analyze this GitHub project and generate an SRS document"
- "Reverse-engineer this codebase to create technical specifications"
- "Convert our PRD into a detailed SRS document"
- "Document the requirements for this existing system"
- "Create a development contract based on current implementation"
- "Generate technical specifications from project files"

## How to Use This Skill

### 🚀 Quick Start (Recommended)

**分析GitHub项目并生成SRS文档：**
```bash
# 1. 分析项目结构
python scripts/analyze_project_structure.py <项目路径> --output project_analysis.json

# 2. 提取API端点
python scripts/extract_api_endpoints.py <项目路径> --output api_analysis.json

# 3. 分析数据库模式
python scripts/analyze_database_schema.py <项目路径> --output database_analysis.json

# 4. 生成SRS文档（自动命名和定位）
python scripts/generate_srs_sections.py \
    --project project_analysis.json \
    --api api_analysis.json \
    --database database_analysis.json \
    --project-path <项目路径>
```

### 📝 输出格式
- **文件名**: `项目名_SRS.md` (自动从项目路径提取)
- **输出位置**: skill目录外，便于用户访问
- **文档格式**: 完整的IEEE 830标准SRS文档

### 🔧 详细使用步骤

#### Step 1: Project Input Analysis
To analyze a project, obtain the project source code either from:
- GitHub repository URL (需要先克隆到本地)
- Local project directory path
- Existing PRD document (if available)

#### Step 2: Execute Analysis Scripts
Run the bundled analysis scripts in sequence:

1. **Project Structure Analysis** (`scripts/analyze_project_structure.py`)
   - Analyzes directory structure and identifies technology stack
   - Extracts build configuration and dependencies
   - Identifies key files and components
   - Output: `project_analysis.json`

2. **API Endpoint Extraction** (`scripts/extract_api_endpoints.py`)
   - Scans source code for REST API endpoints
   - Identifies GraphQL schemas and WebSocket connections
   - Extracts external API integrations
   - Output: `api_analysis.json`

3. **Database Schema Analysis** (`scripts/analyze_database_schema.py`)
   - Analyzes database models and schemas
   - Extracts entity relationships and constraints
   - Identifies data types and validation rules
   - Output: `database_analysis.json`

#### Step 3: Generate SRS Document
Use the SRS generation script with project name extraction:

```bash
python scripts/generate_srs_sections.py \
    --project project_analysis.json \
    --api api_analysis.json \
    --database database_analysis.json \
    --project-path <项目路径>
```

**参数说明**:
- `--project`: 项目分析结果JSON文件
- `--api`: API分析结果JSON文件
- `--database`: 数据库分析结果JSON文件
- `--project-path`: 原始项目路径（用于提取项目名）
- `--output`: 自定义输出文件名（可选）
- `--template`: 自定义模板文件（可选）

#### Step 4: Review and Refine
Review the generated SRS document and:
- Validate extracted requirements against actual business needs
- Add missing business logic and user stories
- Refine non-functional requirements based on project context
- Ensure compliance with organizational standards

### 📋 实际使用示例

#### 示例1: 分析Cognee项目
```bash
# 进入技能目录
cd .claude/skills/srs-reverse-engineering

# 分析Cognee项目
python scripts/analyze_project_structure.py ../../cognee --output cognee_project.json
python scripts/extract_api_endpoints.py ../../cognee --output cognee_api.json
python scripts/analyze_database_schema.py ../../cognee --output cognee_database.json

# 生成SRS文档
python scripts/generate_srs_sections.py \
    --project cognee_project.json \
    --api cognee_api.json \
    --database cognee_database.json \
    --project-path ../../cognee

# 输出: ../../cognee_SRS.md
```

#### 示例2: 本地项目分析
```bash
# 分析本地项目
python scripts/analyze_project_structure.py /path/to/my-project --output project.json
python scripts/extract_api_endpoints.py /path/to/my-project --output api.json
python scripts/analyze_database_schema.py /path/to/my-project --output db.json

# 生成SRS文档
python scripts/generate_srs_sections.py \
    --project project.json \
    --api api.json \
    --database db.json \
    --project-path /path/to/my-project

# 输出: ../my-project_SRS.md
```

### ⚙️ 高级功能

#### 自定义模板
```bash
python scripts/generate_srs_sections.py \
    --project project.json \
    --api api.json \
    --database db.json \
    --template assets/custom-template.md \
    --project-path ./my-project
```

#### 批量处理多个项目
```bash
for project in project1 project2 project3; do
    python scripts/analyze_project_structure.py $project --output ${project}_project.json
    python scripts/extract_api_endpoints.py $project --output ${project}_api.json
    python scripts/analyze_database_schema.py $project --output ${project}_db.json

    python scripts/generate_srs_sections.py \
        --project ${project}_project.json \
        --api ${project}_api.json \
        --database ${project}_db.json \
        --project-path $project
done
```

### 🐛 故障排除

**常见问题解决**:
- **项目名提取失败**: 确保使用正确的 `--project-path` 参数
- **输出路径错误**: 确保在正确的技能目录中运行脚本
- **编码问题**: 确保使用UTF-8编码和正确的Python环境
- **权限问题**: 检查文件读写权限和目录访问权限

**项目名提取优先级**:
1. **高优先级**: `--project-path` 参数
2. **中优先级**: 从文档标题自动提取
3. **低优先级**: 默认名称处理

## Bundled Resources

### Scripts (`scripts/`)

- **analyze_project_structure.py** - Analyzes project structure, technology stack, and configuration files
- **extract_api_endpoints.py** - Extracts REST API, GraphQL, and WebSocket endpoints from source code
- **analyze_database_schema.py** - Analyzes database models, relationships, and constraints
- **generate_srs_sections.py** - Generates complete SRS document from analysis results
- **package_skill.py** - Validates and packages the skill for distribution

### References (`references/`)

- **srs-template.md** - IEEE 830-compliant SRS template with comprehensive section structure
- **functional-requirements-guide.md** - Guidelines for writing clear, testable functional requirements
- **non-functional-requirements-checklist.md** - Comprehensive checklist for performance, security, and reliability requirements

### Assets (`assets/`)

- **srs-markdown-template.md** - Complete Markdown template with formatting, examples, and placeholders
- **example-srs-output.md** - Sample generated SRS document showing expected output format and quality

## Output Quality Standards

The generated SRS documents must meet these quality criteria:

### Functional Requirements
- Clear, unambiguous descriptions of system behavior
- Input/output specifications for each function
- Business rules and validation criteria
- Error handling and exception scenarios
- Testable acceptance criteria

### Non-Functional Requirements
- Performance metrics (response time, throughput, concurrency)
- Security requirements (authentication, authorization, data protection)
- Reliability and availability specifications
- Usability and accessibility requirements
- Compatibility and interoperability constraints

### Technical Specifications
- System architecture documentation
- API interface specifications
- Data model and entity relationship diagrams
- Integration requirements with external systems
- Deployment and infrastructure requirements

## Supported Technologies

### Frontend Frameworks
- React, Vue.js, Angular, Svelte
- Build tools: Webpack, Vite, Rollup
- CSS frameworks: Bootstrap, Tailwind CSS, Material-UI

### Backend Frameworks
- Node.js: Express, Fastify, NestJS
- Python: Django, Flask, FastAPI
- Java: Spring Boot, Jakarta EE
- Other: .NET Core, Ruby on Rails, PHP Laravel

### Databases
- Relational: MySQL, PostgreSQL, SQL Server, Oracle
- NoSQL: MongoDB, Redis, Cassandra, Elasticsearch
- Cloud: AWS RDS, Google Cloud SQL, Azure Database

### Project Types
- Web applications (SPA, MPA, PWA)
- Mobile applications (React Native, Flutter, native)
- Microservices and distributed systems
- APIs and backend services
- Data processing and analytics systems

## Usage Examples

### Example 1: GitHub Repository Analysis
```
User: "Analyze https://github.com/company/ecommerce-platform and generate an SRS document"

Process:
1. Clone or analyze the GitHub repository
2. Execute all analysis scripts
3. Generate comprehensive SRS document
4. Review and validate technical requirements
```

### Example 2: Local Project Documentation
```
User: "Document requirements for our existing inventory management system"

Process:
1. Analyze local project directory
2. Extract current implementation details
3. Compare with existing business requirements
4. Generate updated SRS document
```

### Example 3: PRD to SRS Conversion
```
User: "Convert our product requirements document into technical specifications"

Process:
1. Analyze existing codebase implementation
2. Map PRD features to technical requirements
3. Identify gaps between PRD and implementation
4. Generate comprehensive SRS with both functional and technical specifications
```

## Quality Assurance

### Validation Checklist
- [ ] All functional requirements are testable
- [ ] Non-functional requirements are measurable
- [ ] API specifications are complete and accurate
- [ ] Data models reflect actual implementation
- [ ] Architecture documentation is consistent with code
- [ ] Security requirements address identified risks
- [ ] Performance requirements are realistic and measurable

### Review Process
1. **Technical Review** - Validate technical accuracy with development team
2. **Business Review** - Ensure business requirements are properly captured
3. **Architecture Review** - Verify system architecture documentation
4. **Security Review** - Assess security requirements and implementation
5. **Final Approval** - Stakeholder sign-off on development contract

## Limitations and Considerations

### Analysis Limitations
- Cannot extract business logic not implemented in code
- May miss requirements handled by third-party services
- Limited to analyzing committed code changes
- Cannot infer user experience requirements from code alone

### Quality Dependencies
- Code quality and documentation affect analysis accuracy
- Complex architectures may require manual intervention
- Business context may need to be provided separately
- Generated requirements require human validation and refinement

### Best Practices
- Always validate generated SRS against business requirements
- Supplement analysis with stakeholder interviews
- Use generated SRS as baseline, not final specification
- Keep SRS document updated as system evolves

## Integration with Development Workflow

### Pre-Development
- Use SRS as basis for technical design and architecture
- Define development milestones and deliverables
- Establish testing criteria and acceptance standards

### During Development
- Reference SRS for implementation guidance
- Track requirement coverage and progress
- Manage changes through formal change control process

### Post-Development
- Use SRS for testing and quality assurance
- Validate system meets all specified requirements
- Document deviations and change approvals