"""
Audit Engine Module
نظام التدقيق الآلي للثغرات بناءً على 7 عناصر أساسية
"""

import re
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict
from enum import Enum


class AuditElement(Enum):
    """عناصر التدقيق السبعة"""
    DEFINITION = "Definition"
    DESCRIPTION = "Description"
    LOCATION = "Location"
    AFFECTED_ASSETS = "Affected Assets"
    SEVERITY = "Severity"
    REMEDIATION_STATUS = "Remediation Status"
    REMEDIATION_METHOD = "Remediation Method"


@dataclass
class AuditResult:
    """نتيجة تدقيق عنصر واحد"""
    element: str
    present: bool
    confidence: float
    keywords_found: List[str]
    evidence: str = ""
    
    def __repr__(self) -> str:
        status = "✓" if self.present else "✗"
        return f"{status} {self.element}: {self.confidence*100:.0f}%"


@dataclass
class VulnerabilityAuditReport:
    """تقرير تدقيق ثغرة واحدة"""
    vulnerability_id: int
    vulnerability_title: str
    audit_results: List[AuditResult]
    overall_compliance: float
    compliance_percentage: float
    
    def __repr__(self) -> str:
        return f"Vulnerability #{self.vulnerability_id}: {self.compliance_percentage:.1f}% compliant"


class AuditEngine:
    """محرك التدقيق الآلي"""
    
    # الكلمات المفتاحية لكل عنصر تدقيق
    KEYWORDS = {
        AuditElement.DEFINITION: [
            'definition', 'defined', 'is', 'refers to', 'means',
            'تعريف', 'معرف', 'يشير إلى', 'يعني'
        ],
        AuditElement.DESCRIPTION: [
            'description', 'details', 'explains', 'details', 'background',
            'وصف', 'تفاصيل', 'يشرح', 'خلفية'
        ],
        AuditElement.LOCATION: [
            'location', 'located', 'url', 'ip', 'port', 'endpoint', 'path',
            'address', 'server', 'host', 'domain',
            'الموقع', 'عنوان', 'خادم', 'نطاق'
        ],
        AuditElement.AFFECTED_ASSETS: [
            'affected', 'impact', 'system', 'application', 'server', 'database',
            'asset', 'component', 'module', 'service',
            'متأثر', 'تأثير', 'نظام', 'تطبيق', 'خادم', 'قاعدة بيانات'
        ],
        AuditElement.SEVERITY: [
            'severity', 'critical', 'high', 'medium', 'low', 'info',
            'risk', 'cvss', 'score',
            'خطورة', 'حرج', 'عالي', 'متوسط', 'منخفض', 'معلومة'
        ],
        AuditElement.REMEDIATION_STATUS: [
            'status', 'fixed', 'resolved', 'closed', 'open', 'pending',
            'remediated', 'patched', 'addressed',
            'الحالة', 'معالج', 'مغلق', 'قيد الانتظار', 'مفتوح'
        ],
        AuditElement.REMEDIATION_METHOD: [
            'remediation', 'recommendation', 'solution', 'fix', 'patch',
            'mitigation', 'action', 'steps', 'procedure',
            'معالجة', 'توصية', 'حل', 'إصلاح', 'تصحيح'
        ]
    }
    
    # أنماط Regex متقدمة
    PATTERNS = {
        AuditElement.LOCATION: [
            r'(?:https?://)?[\w\-\.]+(?:\.\w+)+(?:/[\w\-\./?%&=]*)?',  # URLs
            r'\b(?:\d{1,3}\.){3}\d{1,3}(?::\d+)?\b',  # IP addresses
            r'(?:port|port\s*[:=])\s*\d+',  # Ports
            r'(?:path|endpoint|uri)\s*[:=]\s*[/\w\-\.]+',  # Paths
        ],
        AuditElement.SEVERITY: [
            r'(?:cvss|cvss\s*score)\s*[:=]?\s*[\d.]+',  # CVSS scores
            r'(?:severity|risk\s*level)\s*[:=]?\s*(?:critical|high|medium|low|info)',
        ],
        AuditElement.REMEDIATION_STATUS: [
            r'(?:status|state)\s*[:=]?\s*(?:fixed|resolved|closed|open|pending)',
            r'(?:was|has\s*been)\s*(?:fixed|patched|remediated)',
        ]
    }
    
    def __init__(self):
        """تهيئة محرك التدقيق"""
        pass
    
    def audit_vulnerability(self, vuln_id: int, vuln_title: str, vuln_content: str) -> VulnerabilityAuditReport:
        """
        تدقيق ثغرة واحدة
        
        Args:
            vuln_id: معرف الثغرة
            vuln_title: عنوان الثغرة
            vuln_content: محتوى الثغرة
            
        Returns:
            تقرير التدقيق
        """
        audit_results = []
        
        # تدقيق كل عنصر
        for element in AuditElement:
            result = self._audit_element(element, vuln_content)
            audit_results.append(result)
        
        # حساب نسبة الالتزام
        present_count = sum(1 for r in audit_results if r.present)
        compliance_percentage = (present_count / len(audit_results)) * 100
        overall_compliance = sum(r.confidence for r in audit_results) / len(audit_results)
        
        report = VulnerabilityAuditReport(
            vulnerability_id=vuln_id,
            vulnerability_title=vuln_title,
            audit_results=audit_results,
            overall_compliance=overall_compliance,
            compliance_percentage=compliance_percentage
        )
        
        return report
    
    def _audit_element(self, element: AuditElement, text: str) -> AuditResult:
        """
        تدقيق عنصر واحد
        
        Args:
            element: العنصر المراد تدقيقه
            text: النص المراد البحث فيه
            
        Returns:
            نتيجة التدقيق
        """
        text_lower = text.lower()
        keywords_found = []
        confidence = 0.0
        evidence = ""
        
        # البحث عن الكلمات المفتاحية
        if element in self.KEYWORDS:
            for keyword in self.KEYWORDS[element]:
                if keyword.lower() in text_lower:
                    keywords_found.append(keyword)
                    confidence += 0.15  # كل كلمة مفتاحية تزيد الثقة بـ 15%
        
        # البحث عن الأنماط المتقدمة
        if element in self.PATTERNS:
            for pattern in self.PATTERNS[element]:
                matches = re.findall(pattern, text, re.IGNORECASE)
                if matches:
                    keywords_found.extend(matches[:3])  # أول 3 نتائج
                    confidence += 0.25  # الأنماط لها وزن أكبر
        
        # تحديد الحد الأقصى للثقة
        confidence = min(confidence, 1.0)
        
        # تحديد ما إذا كان العنصر موجوداً
        present = confidence >= 0.3
        
        # استخراج دليل (أول 100 حرف من النص الذي يحتوي على الكلمات المفتاحية)
        if keywords_found:
            for keyword in keywords_found:
                idx = text_lower.find(keyword.lower())
                if idx != -1:
                    start = max(0, idx - 20)
                    end = min(len(text), idx + 80)
                    evidence = text[start:end].strip()
                    break
        
        return AuditResult(
            element=element.value,
            present=present,
            confidence=confidence,
            keywords_found=list(set(keywords_found))[:5],  # أول 5 كلمات فقط
            evidence=evidence
        )
    
    def audit_report(self, vulnerabilities: List[Dict]) -> Dict:
        """
        تدقيق تقرير كامل
        
        Args:
            vulnerabilities: قائمة الثغرات
            
        Returns:
            تقرير التدقيق الكامل
        """
        reports = []
        
        for vuln in vulnerabilities:
            report = self.audit_vulnerability(
                vuln.get('id', 0),
                vuln.get('title', 'Unknown'),
                vuln.get('content', '')
            )
            reports.append(report)
        
        # حساب الإحصائيات العامة
        total_compliance = sum(r.compliance_percentage for r in reports) / len(reports) if reports else 0
        
        element_stats = {}
        for element in AuditElement:
            present_count = sum(1 for r in reports for ar in r.audit_results if ar.element == element.value and ar.present)
            element_stats[element.value] = {
                'total': len(reports),
                'present': present_count,
                'percentage': (present_count / len(reports) * 100) if reports else 0
            }
        
        return {
            'total_vulnerabilities': len(reports),
            'overall_compliance_percentage': total_compliance,
            'vulnerability_reports': reports,
            'element_statistics': element_stats
        }


if __name__ == "__main__":
    # اختبار محرك التدقيق
    sample_vuln = {
        'id': 1,
        'title': 'SQL Injection',
        'content': """
        Definition: SQL Injection is a code injection technique used to attack data-driven applications.
        
        Description: The application is vulnerable to SQL injection attacks through the login form.
        
        Location: https://example.com/login.php
        
        Affected Assets: Web Application Server, Database Server
        
        Severity: High (CVSS Score: 8.5)
        
        Remediation Status: Fixed
        
        Remediation Method: Input validation and parameterized queries were implemented.
        """
    }
    
    engine = AuditEngine()
    report = engine.audit_vulnerability(
        sample_vuln['id'],
        sample_vuln['title'],
        sample_vuln['content']
    )
    
    print(f"\n🔍 تقرير التدقيق: {report.vulnerability_title}")
    print(f"   نسبة الالتزام: {report.compliance_percentage:.1f}%\n")
    
    for result in report.audit_results:
        print(f"   {result}")
