"""
Report Generator Module
إنشاء تقارير التدقيق بصيغ مختلفة
"""

import json
from datetime import datetime
from typing import Dict, List
from pathlib import Path
from tabulate import tabulate


class ReportGenerator:
    """فئة لإنشاء التقارير"""
    
    def __init__(self, output_dir: str = "reports"):
        """
        تهيئة منشئ التقارير
        
        Args:
            output_dir: مجلد الإخراج
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_text_report(self, audit_result: Dict, filename: str = None) -> str:
        """
        إنشاء تقرير نصي
        
        Args:
            audit_result: نتيجة التدقيق
            filename: اسم الملف (اختياري)
            
        Returns:
            محتوى التقرير
        """
        report = []
        report.append("=" * 80)
        report.append("تقرير تدقيق تقارير اختبار الاختراق (Pentest Auditor Report)")
        report.append("=" * 80)
        report.append(f"التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # الملخص العام
        report.append("📊 الملخص العام")
        report.append("-" * 80)
        report.append(f"إجمالي الثغرات: {audit_result.get('total_vulnerabilities', 0)}")
        report.append(f"نسبة الالتزام الإجمالية: {audit_result.get('overall_compliance_percentage', 0):.1f}%")
        report.append("")
        
        # إحصائيات العناصر
        report.append("📈 إحصائيات عناصر التدقيق")
        report.append("-" * 80)
        
        element_stats = audit_result.get('element_statistics', {})
        table_data = []
        for element, stats in element_stats.items():
            table_data.append([
                element,
                stats.get('present', 0),
                stats.get('total', 0),
                f"{stats.get('percentage', 0):.1f}%"
            ])
        
        report.append(tabulate(
            table_data,
            headers=['عنصر التدقيق', 'موجود', 'الإجمالي', 'النسبة'],
            tablefmt='grid'
        ))
        report.append("")
        
        # تفاصيل كل ثغرة
        report.append("🔍 تفاصيل الثغرات")
        report.append("=" * 80)
        
        for vuln_report in audit_result.get('vulnerability_reports', []):
            report.append(f"\nالثغرة #{vuln_report.vulnerability_id}: {vuln_report.vulnerability_title}")
            report.append("-" * 80)
            report.append(f"نسبة الالتزام: {vuln_report.compliance_percentage:.1f}%")
            report.append("")
            
            # جدول نتائج التدقيق
            audit_table = []
            for result in vuln_report.audit_results:
                status = "✓ موجود" if result.present else "✗ غير موجود"
                audit_table.append([
                    result.element,
                    status,
                    f"{result.confidence*100:.0f}%",
                    ", ".join(result.keywords_found[:2]) if result.keywords_found else "—"
                ])
            
            report.append(tabulate(
                audit_table,
                headers=['العنصر', 'الحالة', 'الثقة', 'الكلمات المفتاحية'],
                tablefmt='grid'
            ))
            report.append("")
        
        # الخلاصة والتوصيات
        report.append("=" * 80)
        report.append("💡 التوصيات")
        report.append("-" * 80)
        
        missing_elements = []
        for element, stats in element_stats.items():
            if stats.get('percentage', 0) < 50:
                missing_elements.append(element)
        
        if missing_elements:
            report.append(f"العناصر التي تحتاج إلى تحسين:")
            for element in missing_elements:
                report.append(f"  • {element}")
        else:
            report.append("✓ جميع العناصر موجودة في معظم الثغرات")
        
        report.append("")
        report.append("=" * 80)
        
        report_text = "\n".join(report)
        
        # حفظ الملف إذا تم تحديد اسم
        if filename:
            filepath = self.output_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report_text)
            print(f"✓ تم حفظ التقرير: {filepath}")
        
        return report_text
    
    def generate_json_report(self, audit_result: Dict, filename: str = None) -> str:
        """
        إنشاء تقرير JSON
        
        Args:
            audit_result: نتيجة التدقيق
            filename: اسم الملف (اختياري)
            
        Returns:
            محتوى التقرير
        """
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_vulnerabilities': audit_result.get('total_vulnerabilities', 0),
                'overall_compliance_percentage': audit_result.get('overall_compliance_percentage', 0),
            },
            'element_statistics': audit_result.get('element_statistics', {}),
            'vulnerabilities': []
        }
        
        # تحويل تقارير الثغرات
        for vuln_report in audit_result.get('vulnerability_reports', []):
            vuln_data = {
                'id': vuln_report.vulnerability_id,
                'title': vuln_report.vulnerability_title,
                'compliance_percentage': vuln_report.compliance_percentage,
                'audit_results': []
            }
            
            for result in vuln_report.audit_results:
                vuln_data['audit_results'].append({
                    'element': result.element,
                    'present': result.present,
                    'confidence': result.confidence,
                    'keywords_found': result.keywords_found,
                    'evidence': result.evidence
                })
            
            report_data['vulnerabilities'].append(vuln_data)
        
        report_json = json.dumps(report_data, ensure_ascii=False, indent=2)
        
        # حفظ الملف إذا تم تحديد اسم
        if filename:
            filepath = self.output_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report_json)
            print(f"✓ تم حفظ التقرير: {filepath}")
        
        return report_json
    
    def generate_csv_report(self, audit_result: Dict, filename: str = None) -> str:
        """
        إنشاء تقرير CSV
        
        Args:
            audit_result: نتيجة التدقيق
            filename: اسم الملف (اختياري)
            
        Returns:
            محتوى التقرير
        """
        lines = []
        lines.append("Vulnerability ID,Title,Compliance %,Element,Status,Confidence,Keywords")
        
        for vuln_report in audit_result.get('vulnerability_reports', []):
            for result in vuln_report.audit_results:
                status = "Present" if result.present else "Missing"
                keywords = ";".join(result.keywords_found)
                line = f'{vuln_report.vulnerability_id},"{vuln_report.vulnerability_title}",{vuln_report.compliance_percentage:.1f},"{result.element}",{status},{result.confidence*100:.0f},"{keywords}"'
                lines.append(line)
        
        report_csv = "\n".join(lines)
        
        # حفظ الملف إذا تم تحديد اسم
        if filename:
            filepath = self.output_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report_csv)
            print(f"✓ تم حفظ التقرير: {filepath}")
        
        return report_csv
    
    def generate_summary(self, audit_result: Dict) -> str:
        """
        إنشاء ملخص سريع
        
        Args:
            audit_result: نتيجة التدقيق
            
        Returns:
            الملخص
        """
        summary = []
        summary.append("\n📋 ملخص التدقيق السريع")
        summary.append("=" * 60)
        
        total_vulns = audit_result.get('total_vulnerabilities', 0)
        compliance = audit_result.get('overall_compliance_percentage', 0)
        
        summary.append(f"إجمالي الثغرات: {total_vulns}")
        summary.append(f"نسبة الالتزام: {compliance:.1f}%")
        
        # تقييم الجودة
        if compliance >= 80:
            rating = "ممتاز ✓"
        elif compliance >= 60:
            rating = "جيد ✓"
        elif compliance >= 40:
            rating = "متوسط ⚠"
        else:
            rating = "ضعيف ✗"
        
        summary.append(f"التقييم: {rating}")
        summary.append("=" * 60)
        
        return "\n".join(summary)


if __name__ == "__main__":
    # اختبار منشئ التقارير
    sample_result = {
        'total_vulnerabilities': 3,
        'overall_compliance_percentage': 75.5,
        'element_statistics': {
            'Definition': {'total': 3, 'present': 3, 'percentage': 100},
            'Description': {'total': 3, 'present': 3, 'percentage': 100},
            'Location': {'total': 3, 'present': 2, 'percentage': 66.7},
            'Affected Assets': {'total': 3, 'present': 2, 'percentage': 66.7},
            'Severity': {'total': 3, 'present': 3, 'percentage': 100},
            'Remediation Status': {'total': 3, 'present': 2, 'percentage': 66.7},
            'Remediation Method': {'total': 3, 'present': 1, 'percentage': 33.3},
        },
        'vulnerability_reports': []
    }
    
    generator = ReportGenerator()
    
    # إنشاء التقارير
    text_report = generator.generate_text_report(sample_result, "sample_report.txt")
    json_report = generator.generate_json_report(sample_result, "sample_report.json")
    csv_report = generator.generate_csv_report(sample_result, "sample_report.csv")
    
    # طباعة الملخص
    summary = generator.generate_summary(sample_result)
    print(summary)
