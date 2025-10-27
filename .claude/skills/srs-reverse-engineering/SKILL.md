---
name: srs-reverse-engineering
description: This skill automatically analyzes existing codebases through reverse engineering to generate detailed Software Requirements Specification (SRS) documents following IEEE 830 standards. It should be used when projects lack technical documentation, need requirements analysis for legacy systems, or require requirement documents for refactoring and upgrades.
---

# SRS Reverse Engineering Skill

## Purpose

Analyze existing codebases through reverse engineering to generate comprehensive Software Requirements Specification (SRS) documents following IEEE 830 standards.

## When to Use

Use this skill when:
- Projects lack comprehensive technical documentation
- Legacy systems require requirements analysis documentation
- System refactoring or upgrades need formal requirement specifications
- Onboarding new team members requires system understanding documentation

## Core Workflow

Execute this multi-stage analysis process sequentially, updating progress after each stage:

### Analysis Progress:
- [ ] **Stage 1**: Project overview and preparation
- [ ] **Stage 2**: Database reverse engineering analysis
- [ ] **Stage 3**: API interface discovery
- [ ] **Stage 4**: Code structure and business logic analysis
- [ ] **Stage 5**: SRS document generation
- [ ] **Stage 6**: Quality assurance and documentation refinement

## Execution Steps

### Stage 1: Project Overview and Preparation

**Objective**: Understand project basics and prepare analysis environment

**Steps**:
1. **Project Path Confirmation**: Obtain absolute project path from user
2. **Output Directory Setup**: Create dedicated analysis output directory
3. **Project Type Identification**: Detect main technology stack and frameworks
4. **Analysis Scope Confirmation**: Define code scope for analysis

**Tools**: Manual project structure examination (no scripts required)

**Output**: Analysis readiness confirmation

### Stage 2: Database Reverse Engineering Analysis

**Objective**: Extract data models and business rules

**Steps**:
1. **Execute database analysis script**:
   ```bash
   python scripts/analyze_database.py [PROJECT_PATH] --output [OUTPUT_DIR]/database_analysis
   ```

2. **Analysis result verification**:
   - Check `database_analysis.json` generation
   - Confirm complete table and field identification
   - Validate ERD diagram correctness

3. **Result interpretation**:
   - Review generated `erd.md` file
   - Verify `data_dictionary.md` completeness
   - Identify core business entities and relationships

**Output**: Data model analysis report

### Stage 3: API Interface Discovery

**Objective**: Identify and document all API endpoints

**Steps**:
1. **Execute API discovery script**:
   ```bash
   python scripts/discover_apis.py [PROJECT_PATH] --output [OUTPUT_DIR]/api_analysis
   ```

2. **API endpoint validation**:
   - Verify discovered API count is reasonable
   - Group APIs by functional modules
   - Identify core business and auxiliary APIs

3. **External dependency analysis**:
   - Review external API call lists
   - Analyze system dependencies on external services
   - Assess business impact of third-party integrations

**Output**: API documentation and external dependency analysis

### Stage 4: Code Structure and Business Logic Analysis

**Objective**: Understand system architecture and core business rules

**Steps**:
1. **Execute code structure analysis**:
   ```bash
   python scripts/analyze_code_structure.py [PROJECT_PATH] --output [OUTPUT_DIR]/code_analysis
   ```

2. **Architecture pattern identification**:
   - Analyze overall project architecture patterns
   - Identify controller, service, and data access layers
   - Understand component dependencies

3. **Business rule extraction**:
   - Review extracted business rules list
   - Categorize rules by type
   - Analyze rule interrelationships

**Output**: Code structure analysis report and business rules inventory

### Stage 5: SRS Document Generation

**Objective**: Generate standardized SRS document based on analysis results

**Steps**:
1. **Integrate analysis results**: Ensure all analysis scripts executed successfully
2. **Execute SRS generation script**:
   ```bash
   python scripts/generate_srs_template.py --analysis [OUTPUT_DIR] --output [OUTPUT_DIR]/SRS_DOCUMENT.md
   ```

3. **Document structure verification**:
   - Confirm SRS document contains all required sections
   - Verify functional requirements cover major APIs
   - Validate data requirements consistency with database analysis

**Output**: Complete SRS document draft

### Stage 6: Quality Assurance and Documentation Refinement

**Objective**: Ensure generated SRS document meets quality standards

**Steps**:
1. **Quality checklist review**: Use `assets/srs_checklist.md` for comprehensive review
2. **Content enhancement**: Supplement missing information based on review results
3. **Format optimization**: Adjust document formatting and language clarity
4. **Accuracy validation**: Cross-verify consistency between different analysis results

**Output**: Final version SRS document

## Key Considerations

### Analysis Depth Control
- Prioritize core business modules and critical code paths
- Simplify analysis of test files, configuration files, and auxiliary code
- Focus on business logic-related code analysis

### Result Credibility
- Clearly mark content inferred from code analysis
- Mark uncertain information as "requires confirmation"
- Recommend validation with project stakeholders for key requirements

### Tool Usage Principles
- Execute scripts with exact parameter formats
- Review script execution outputs for potential errors
- Adjust analysis strategies based on execution results

### Documentation Quality Standards
- Requirement descriptions must be clear and unambiguous
- Functional requirements must include acceptance criteria
- Non-functional requirements must be based on code evidence

## Bundled Resources Usage

### Reference Materials
- `references/analysis_guidelines.md`: Detailed reverse engineering methodologies
- `references/business_rules_extraction.md`: Business rules extraction techniques
- `references/nfr_identification.md`: Non-functional requirements identification guide

### Quality Control Tools
- `assets/srs_checklist.md`: Comprehensive quality review checklist
- `references/srs_template.md`: Standard SRS document template

## Troubleshooting

### Script Execution Failures
1. Check Python environment and dependencies
2. Confirm project path correctness
3. Review error logs and adjust parameters

### Incomplete Analysis Results
1. Expand analysis scope to include more code files
2. Manually supplement critical analysis results
3. Cross-validate using multiple analysis methods

### Documentation Quality Issues
1. Use quality checklist for systematic review
2. Reference standard templates for document structure
3. Add specific business scenarios and user stories

## Success Criteria

### Technical Standards
- All analysis scripts execute successfully
- Generated documents have complete structure
- Analysis results maintain logical consistency

### Quality Standards
- Functional requirements cover major business scenarios
- Non-functional requirements have code evidence support
- Documentation is clear, well-formatted, and professional

### Utility Standards
- Documents support project handover processes
- Provide accurate basis for system refactoring
- Enable rapid team member onboarding

---

**Important Note**: This skill generates SRS documents based on code reverse engineering analysis, reflecting system currently implemented functionality. Validate with project stakeholders before use to ensure accuracy and completeness.