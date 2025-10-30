#!/usr/bin/env python3
"""
License Analyzer Script
Identify and analyze project licenses
"""

import re
from pathlib import Path
from typing import Dict, Optional

class LicenseAnalyzer:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.license_patterns = {
            "MIT": [
                r"MIT\s+License",
                r"Permission\s+is\s+hereby\s+granted.*free\s+of\s+charge",
                r"THE\s+SOFTWARE\s+IS\s+PROVIDED\s+\"AS\s+IS\""
            ],
            "Apache 2.0": [
                r"Apache\s+License.*Version\s+2\.0",
                r"Licensed\s+under\s+the\s+Apache\s+License",
                r"www\.apache\.org/licenses/LICENSE-2\.0"
            ],
            "GPL-3.0": [
                r"GNU\s+GENERAL\s+PUBLIC\s+LICENSE.*Version\s+3",
                r"This\s+program\s+is\s+free\s+software.*GPL",
                r"www\.gnu\.org/licenses/gpl-3\.0"
            ],
            "GPL-2.0": [
                r"GNU\s+GENERAL\s+PUBLIC\s+LICENSE.*Version\s+2",
                r"GPL.*version\s+2"
            ],
            "BSD-3-Clause": [
                r"BSD\s+3-Clause\s+License",
                r"Redistribution\s+and\s+use\s+in\s+source\s+and\s+binary\s+forms",
                r"Neither\s+the\s+name\s+of.*nor\s+the\s+names\s+of\s+its\s+contributors"
            ],
            "ISC": [
                r"ISC\s+License",
                r"Permission\s+to\s+use.*copy.*modify.*distribute"
            ]
        }

        self.license_summaries = {
            "MIT": {
                "commercial_use": "允许",
                "distribution": "允许",
                "modification": "允许",
                "patent_use": "允许",
                "private_use": "允许",
                "liability": "不承担责任",
                "warranty": "无担保",
                "summary": "允许商用、修改和分发，但必须保留原始版权声明。"
            },
            "Apache 2.0": {
                "commercial_use": "允许",
                "distribution": "允许",
                "modification": "允许",
                "patent_use": "明确授予",
                "private_use": "允许",
                "liability": "不承担责任",
                "warranty": "无担保",
                "summary": "允许商用、修改和分发，需保留版权声明和许可证文本，提供专利授权。"
            },
            "GPL-3.0": {
                "commercial_use": "允许",
                "distribution": "允许（必须开源）",
                "modification": "允许（必须开源）",
                "patent_use": "明确授予",
                "private_use": "允许",
                "liability": "不承担责任",
                "warranty": "无担保",
                "summary": "允许商用和修改，但修改后的代码也必须使用GPL-3.0许可证开源（传染性）。"
            },
            "GPL-2.0": {
                "commercial_use": "允许",
                "distribution": "允许（必须开源）",
                "modification": "允许（必须开源）",
                "patent_use": "未明确",
                "private_use": "允许",
                "liability": "不承担责任",
                "warranty": "无担保",
                "summary": "允许商用和修改，但修改后的代码也必须使用GPL-2.0许可证开源（传染性）。"
            },
            "BSD-3-Clause": {
                "commercial_use": "允许",
                "distribution": "允许",
                "modification": "允许",
                "patent_use": "未明确",
                "private_use": "允许",
                "liability": "不承担责任",
                "warranty": "无担保",
                "summary": "允许商用、修改和分发，但不能使用作者名义进行推广，需包含许可证文本。"
            },
            "ISC": {
                "commercial_use": "允许",
                "distribution": "允许",
                "modification": "允许",
                "patent_use": "未明确",
                "private_use": "允许",
                "liability": "不承担责任",
                "warranty": "无担保",
                "summary": "类似MIT的宽松许可证，允许商用、修改和分发，只需保留版权声明。"
            }
        }

    def find_license_file(self) -> Optional[Path]:
        """Find license file in project directory"""
        license_files = [
            "LICENSE", "LICENSE.md", "LICENSE.txt",
            "COPYING", "COPYRIGHT",
            "license", "license.md", "license.txt"
        ]

        for license_file in license_files:
            license_path = self.project_path / license_file
            if license_path.exists():
                return license_path

        return None

    def analyze_license_content(self, content: str) -> Dict:
        """Analyze license file content to identify license type"""
        content_lower = content.lower()

        for license_type, patterns in self.license_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
                    return {
                        "type": license_type,
                        "confidence": "high",
                        "details": self.license_summaries.get(license_type, {})
                    }

        # Check for proprietary or custom licenses
        proprietary_indicators = [
            r"proprietary",
            r"confidential",
            r"trade\s+secret",
            r"all\s+rights\s+reserved"
        ]

        for pattern in proprietary_indicators:
            if re.search(pattern, content, re.IGNORECASE):
                return {
                    "type": "专有许可证",
                    "confidence": "medium",
                    "summary": "专有许可证，可能限制商用、修改或分发。需要仔细阅读条款。"
                }

        return {
            "type": "未知许可证",
            "confidence": "low",
            "summary": "许可证类型未知，需要人工审查许可证条款。"
        }

    def check_readme_license_mention(self) -> Optional[str]:
        """Check if README mentions license type"""
        readme_files = ["README.md", "README.txt", "README"]

        for readme_file in readme_files:
            readme_path = self.project_path / readme_file
            if readme_path.exists():
                try:
                    with open(readme_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Look for license mentions
                    license_mentions = re.findall(
                        r'(?:license|licensed?\s+under)[:\s]+([^.\n]+)',
                        content,
                        re.IGNORECASE
                    )

                    if license_mentions:
                        return license_mentions[0].strip()
                except Exception:
                    continue

        return None

    def generate_license_analysis(self) -> Dict:
        """Generate comprehensive license analysis"""
        license_file = self.find_license_file()

        if not license_file:
            # Check README for license mention
            readme_mention = self.check_readme_license_mention()
            if readme_mention:
                return {
                    "status": "readme_mention",
                    "license_file": None,
                    "mention": readme_mention,
                    "analysis": {
                        "type": "README提及许可证",
                        "confidence": "low",
                        "summary": f"README中提到许可证：{readme_mention}，但未找到完整的许可证文件。"
                    }
                }

            return {
                "status": "no_license",
                "license_file": None,
                "analysis": {
                    "type": "无许可证",
                    "confidence": "high",
                    "summary": "未找到许可证文件，默认版权所有，商用风险较高。"
                }
            }

        try:
            with open(license_file, 'r', encoding='utf-8') as f:
                content = f.read()

            analysis = self.analyze_license_content(content)

            return {
                "status": "found",
                "license_file": str(license_file),
                "analysis": analysis
            }

        except Exception as e:
            return {
                "status": "错误",
                "license_file": str(license_file),
                "error": str(e),
                "analysis": {
                    "type": "错误",
                    "confidence": "none",
                    "summary": f"读取许可证文件时出错：{str(e)}"
                }
            }

if __name__ == "__main__":
    import sys
    import json
    if len(sys.argv) != 2:
        print("Usage: python license_analyzer.py <project_path>")
        sys.exit(1)

    analyzer = LicenseAnalyzer(sys.argv[1])
    result = analyzer.generate_license_analysis()
    print(json.dumps(result, indent=2))