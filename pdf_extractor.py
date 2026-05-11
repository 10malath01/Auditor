"""
PDF Extractor Module
استخراج النصوص من ملفات PDF وتنظيفها
"""

import pdfplumber
import re
from pathlib import Path
from typing import List, Dict, Tuple


class PDFExtractor:
    """فئة لاستخراج النصوص من ملفات PDF"""
    
    def __init__(self, pdf_path: str):
        """
        تهيئة المستخرج
        
        Args:
            pdf_path: مسار ملف PDF
        """
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"الملف {pdf_path} غير موجود")
    
    def extract_text(self) -> str:
        """
        استخراج جميع النصوص من ملف PDF
        
        Returns:
            النص الكامل للملف
        """
        full_text = []
        
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    if text:
                        full_text.append(f"--- صفحة {page_num} ---\n{text}\n")
        except Exception as e:
            raise Exception(f"خطأ في قراءة PDF: {str(e)}")
        
        return "\n".join(full_text)
    
    def extract_text_by_page(self) -> List[Dict[str, str]]:
        """
        استخراج النصوص من كل صفحة بشكل منفصل
        
        Returns:
            قائمة قواميس تحتوي على رقم الصفحة والنص
        """
        pages_data = []
        
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    if text:
                        pages_data.append({
                            'page_number': page_num,
                            'text': text,
                            'length': len(text)
                        })
        except Exception as e:
            raise Exception(f"خطأ في قراءة PDF: {str(e)}")
        
        return pages_data
    
    def extract_tables(self) -> List[Dict]:
        """
        استخراج الجداول من ملف PDF
        
        Returns:
            قائمة الجداول المستخرجة
        """
        tables = []
        
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    page_tables = page.extract_tables()
                    if page_tables:
                        for table_idx, table in enumerate(page_tables):
                            tables.append({
                                'page_number': page_num,
                                'table_index': table_idx,
                                'data': table
                            })
        except Exception as e:
            raise Exception(f"خطأ في استخراج الجداول: {str(e)}")
        
        return tables
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        تنظيف النص من الأحرف الزائدة والمسافات
        
        Args:
            text: النص المراد تنظيفه
            
        Returns:
            النص المنظف
        """
        # إزالة المسافات الزائدة
        text = re.sub(r'\s+', ' ', text)
        # إزالة الأحرف الخاصة غير المرغوبة
        text = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', text)
        # إزالة الأسطر الفارغة
        text = '\n'.join(line.strip() for line in text.split('\n') if line.strip())
        
        return text.strip()
    
    def get_pdf_info(self) -> Dict:
        """
        الحصول على معلومات عن ملف PDF
        
        Returns:
            قاموس يحتوي على معلومات الملف
        """
        info = {
            'filename': self.pdf_path.name,
            'file_size_kb': self.pdf_path.stat().st_size / 1024,
            'total_pages': 0,
            'total_text_length': 0
        }
        
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                info['total_pages'] = len(pdf.pages)
                full_text = self.extract_text()
                info['total_text_length'] = len(full_text)
        except Exception as e:
            raise Exception(f"خطأ في الحصول على معلومات PDF: {str(e)}")
        
        return info


if __name__ == "__main__":
    # اختبار المستخرج
    import sys
    
    if len(sys.argv) < 2:
        print("الاستخدام: python pdf_extractor.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    extractor = PDFExtractor(pdf_path)
    
    # طباعة معلومات الملف
    info = extractor.get_pdf_info()
    print(f"\n📄 معلومات الملف:")
    print(f"   الاسم: {info['filename']}")
    print(f"   الحجم: {info['file_size_kb']:.2f} KB")
    print(f"   عدد الصفحات: {info['total_pages']}")
    print(f"   طول النص: {info['total_text_length']} حرف")
    
    # طباعة النص المستخرج
    text = extractor.extract_text()
    print(f"\n📝 النص المستخرج (أول 500 حرف):")
    print(text[:500])
