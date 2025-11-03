#!/usr/bin/env python3
"""
简化的技能打包脚本
"""

import os
import zipfile
from pathlib import Path

def package_skill(skill_path: str, output_path: str):
    """打包技能"""
    skill_path = Path(skill_path)
    skill_name = skill_path.name

    # 创建输出目录
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 创建zip文件
    zip_path = output_dir / f"{skill_name}.zip"

    print(f"正在打包技能: {skill_name}")
    print(f"输出路径: {zip_path}")

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(skill_path):
            # 跳过隐藏目录和文件
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [f for f in files if not f.startswith('.')]

            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(skill_path)
                zipf.write(file_path, arcname)
                print(f"  添加文件: {arcname}")

    # 计算文件大小
    file_size = zip_path.stat().st_size
    print(f"打包完成! 文件大小: {file_size / 1024:.1f} KB")
    print(f"输出文件: {zip_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        skill_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else "output"
        package_skill(skill_path, output_path)
    else:
        print("用法: python simple_package.py <技能路径> [输出目录]")