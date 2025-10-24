#!/usr/bin/env python3
"""
SRS逆向工程技能包打包脚本
"""

import os
import zipfile
import shutil
from pathlib import Path

def create_skill_package():
    """创建技能包zip文件"""
    skill_name = "srs-reverse-engineering"

    # 确认当前目录结构
    required_files = [
        "SKILL.md",
        "README.md",
        "scripts/analyze_database.py",
        "scripts/discover_apis.py",
        "scripts/analyze_code_structure.py",
        "scripts/generate_srs_template.py",
        "references/srs_template.md",
        "references/analysis_guidelines.md",
        "references/business_rules_extraction.md",
        "references/nfr_identification.md",
        "assets/srs_checklist.md"
    ]

    # 检查必需文件是否存在
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)

    if missing_files:
        print("❌ 缺少必需文件:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False

    print("✅ 所有必需文件检查通过")

    # 创建zip包
    zip_filename = f"{skill_name}.zip"

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 添加所有文件到zip包
        for root, dirs, files in os.walk('.'):
            # 跳过.git等目录
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']

            for file in files:
                if file.endswith('.py') and file == 'package.py':
                    continue  # 跳过打包脚本本身

                file_path = os.path.join(root, file)
                arcname = os.path.join(skill_name, file_path)
                zipf.write(file_path, arcname)

    print(f"✅ 技能包已创建: {zip_filename}")

    # 显示包内容
    print(f"\n📦 技能包内容:")
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        for file_info in zipf.filelist:
            print(f"   {file_info.filename}")

    print(f"\n🎉 SRS逆向工程技能包创建完成!")
    print(f"📁 包大小: {os.path.getsize(zip_filename)} 字节")

    return True

if __name__ == "__main__":
    create_skill_package()