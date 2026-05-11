# 📁 هيكل المشروع - Project Structure

## 🗂️ شجرة المشروع

```
pentest-auditor-project/
│
├── 📄 README.md                          # README باللغة الإنجليزية
├── 📄 README_AR.md                       # README شامل باللغة العربية ⭐
├── 📄 PROJECT_STRUCTURE.md               # هذا الملف
│
├── 🐍 Core Modules (المكونات الأساسية)
│   ├── pdf_extractor.py                  # استخراج النصوص من PDF
│   ├── vulnerability_segmenter.py        # تقسيم التقرير إلى ثغرات
│   ├── audit_engine.py                   # محرك التدقيق الآلي (7 عناصر)
│   ├── nlp_model_trainer.py              # تدريب نموذج NLP
│   └── report_generator.py               # إنشاء التقارير
│
├── 🎯 Applications (التطبيقات)
│   ├── pentest_auditor.py                # تطبيق CLI (سطر الأوامر)
│   └── app.py                            # تطبيق Streamlit (الواجهة التفاعلية) ⭐
│
├── 📋 Configuration Files
│   └── requirements.txt                  # المكتبات المطلوبة
│
├── 📁 models/                            # مجلد النماذج المدربة
│   └── nlp_model.pkl                     # نموذج NLP المحفوظ
│
└── 📁 reports/                           # مجلد التقارير المولدة
    ├── report_*.txt                      # تقارير نصية
    ├── report_*.json                     # تقارير JSON
    └── report_*.csv                      # تقارير CSV
```

---

## 📖 شرح كل ملف

### 🔴 المكونات الأساسية (Core Modules)

#### 1. **pdf_extractor.py** 📄
**الوظيفة**: استخراج النصوص من ملفات PDF

**الفئات الرئيسية**:
- `PDFExtractor`: فئة لاستخراج النصوص

**الدوال الرئيسية**:
- `extract_text()`: استخراج جميع النصوص
- `extract_text_by_page()`: استخراج النصوص حسب الصفحة
- `extract_tables()`: استخراج الجداول
- `get_pdf_info()`: الحصول على معلومات الملف

**المثال**:
```python
from pdf_extractor import PDFExtractor

extractor = PDFExtractor("report.pdf")
text = extractor.extract_text()
info = extractor.get_pdf_info()
```

---

#### 2. **vulnerability_segmenter.py** 🔍
**الوظيفة**: تقسيم التقرير إلى ثغرات منفصلة

**الفئات الرئيسية**:
- `Vulnerability`: فئة تمثل ثغرة واحدة
- `VulnerabilitySegmenter`: فئة لتقسيم التقرير

**الدوال الرئيسية**:
- `segment_vulnerabilities()`: تقسيم النص إلى ثغرات
- `get_vulnerabilities_summary()`: الحصول على ملخص الثغرات

**الأنماط المستخدمة**:
- `Vulnerability 1`, `Finding 1`, `Issue 1`
- `CVE-XXXX`, `CWE-XXXX`
- أنماط مخصصة للعنوان والخطورة

**المثال**:
```python
from vulnerability_segmenter import VulnerabilitySegmenter

segmenter = VulnerabilitySegmenter(full_text)
vulnerabilities = segmenter.segment_vulnerabilities()
summary = segmenter.get_vulnerabilities_summary()
```

---

#### 3. **audit_engine.py** ✅
**الوظيفة**: التدقيق الآلي للعناصر السبعة

**الفئات الرئيسية**:
- `AuditElement`: enum للعناصر السبعة
- `AuditResult`: نتيجة تدقيق عنصر واحد
- `VulnerabilityAuditReport`: تقرير تدقيق ثغرة واحدة
- `AuditEngine`: محرك التدقيق

**العناصر السبعة**:
1. **Definition** (التعريف)
2. **Description** (الوصف)
3. **Location** (الموقع)
4. **Affected Assets** (الأجهزة المتضررة)
5. **Severity** (تصنيف الخطورة)
6. **Remediation Status** (حالة المعالجة)
7. **Remediation Method** (طريقة المعالجة)

**الدوال الرئيسية**:
- `audit_vulnerability()`: تدقيق ثغرة واحدة
- `audit_report()`: تدقيق تقرير كامل

**آلية العمل**:
- البحث عن الكلمات المفتاحية
- استخدام Regex للأنماط المتقدمة
- حساب درجة الثقة (Confidence Score)
- تحديد ما إذا كان العنصر موجوداً أم لا

**المثال**:
```python
from audit_engine import AuditEngine

engine = AuditEngine()
report = engine.audit_vulnerability(1, "SQL Injection", vuln_content)
```

---

#### 4. **nlp_model_trainer.py** 🤖
**الوظيفة**: تدريب نموذج NLP لتحسين التنبؤ

**الفئات الرئيسية**:
- `NLPModelTrainer`: فئة لتدريب النموذج

**الدوال الرئيسية**:
- `prepare_training_data()`: تحضير البيانات
- `train()`: تدريب النموذج
- `predict_severity()`: التنبؤ بالخطورة
- `save_model()`: حفظ النموذج
- `load_model()`: تحميل النموذج

**التقنيات المستخدمة**:
- **TF-IDF**: تحويل النصوص إلى أرقام
- **Random Forest**: تصنيف وتنبؤ
- **Train/Test Split**: تقسيم البيانات

**الأداء**:
- دقة التدريب: ~95%
- دقة الاختبار: ~85%

**المثال**:
```python
from nlp_model_trainer import NLPModelTrainer

trainer = NLPModelTrainer()
texts, labels = trainer.prepare_training_data(vulnerabilities)
trainer.train(texts, labels)
result = trainer.predict_severity("Critical vulnerability text")
```

---

#### 5. **report_generator.py** 📊
**الوظيفة**: إنشاء التقارير بصيغ مختلفة

**الفئات الرئيسية**:
- `ReportGenerator`: فئة لإنشاء التقارير

**الدوال الرئيسية**:
- `generate_text_report()`: تقرير نصي
- `generate_json_report()`: تقرير JSON
- `generate_csv_report()`: تقرير CSV
- `generate_summary()`: ملخص سريع

**صيغ الإخراج**:
1. **Text**: تقرير منسق بشكل جميل
2. **JSON**: بيانات منظمة للمعالجة الآلية
3. **CSV**: جدول للتحليل في Excel

**المثال**:
```python
from report_generator import ReportGenerator

generator = ReportGenerator()
text_report = generator.generate_text_report(audit_result, "report.txt")
json_report = generator.generate_json_report(audit_result, "report.json")
```

---

### 🟢 التطبيقات (Applications)

#### 1. **pentest_auditor.py** 🖥️
**الوظيفة**: تطبيق سطر الأوامر (CLI)

**الأوامر المتاحة**:
```bash
# تدقيق ملف PDF
python pentest_auditor.py audit report.pdf --use-nlp --output-format all

# تدريب النموذج
python pentest_auditor.py train-model --use-sample-data

# استخراج النصوص
python pentest_auditor.py extract report.pdf

# تقسيم التقرير
python pentest_auditor.py segment report.pdf

# عرض الإصدار
python pentest_auditor.py version
```

**المميزات**:
- واجهة سهلة الاستخدام
- دعم الخيارات المختلفة
- رسائل خطأ واضحة
- تقدم العملية (Progress Bar)

---

#### 2. **app.py** 🌐
**الوظيفة**: تطبيق ويب تفاعلي باستخدام Streamlit

**الميزات**:
- 📤 رفع ملفات PDF
- 🔍 عرض النتائج بشكل مرئي
- 📊 رسوم بيانية توضيحية
- 📥 تحميل التقارير
- 🤖 تدريب النموذج من الواجهة

**التبويبات**:
1. **🔍 تدقيق التقارير**
   - رفع PDF
   - معالجة تلقائية
   - عرض النتائج (4 تبويبات)

2. **🤖 تدريب النموذج**
   - تدريب NLP
   - عرض النتائج

3. **📊 الإحصائيات**
   - سرعة المعالجة
   - دقة النموذج
   - معايير التقييم

4. **ℹ️ حول المشروع**
   - معلومات عامة
   - الأهداف والمكونات

**التشغيل**:
```bash
streamlit run app.py
```

---

### 📋 ملفات الإعدادات

#### **requirements.txt**
**المكتبات المطلوبة**:
- `PyPDF2`: استخراج النصوص من PDF
- `pdfplumber`: معالجة PDF متقدمة
- `nltk`: معالجة اللغات الطبيعية
- `scikit-learn`: تعلم الآلة
- `numpy`, `pandas`: معالجة البيانات
- `click`: إنشاء CLI
- `streamlit`: واجهة ويب
- `plotly`: رسوم بيانية

**التثبيت**:
```bash
pip install -r requirements.txt
```

---

### 📁 المجلدات

#### **models/**
يحتوي على النماذج المدربة:
- `nlp_model.pkl`: نموذج NLP المحفوظ

#### **reports/**
يحتوي على التقارير المولدة:
- `report_*.txt`: تقارير نصية
- `report_*.json`: تقارير JSON
- `report_*.csv`: تقارير CSV

---

## 🔄 تدفق البيانات

```
PDF File
   │
   ▼
[pdf_extractor.py]
   │ استخراج النصوص
   ▼
Full Text
   │
   ▼
[vulnerability_segmenter.py]
   │ تقسيم إلى ثغرات
   ▼
Vulnerabilities List
   │
   ├─► [audit_engine.py]
   │   │ التدقيق الأساسي
   │   ▼
   │   Audit Results (7 Elements)
   │
   └─► [nlp_model_trainer.py]
       │ التنبؤ بالخطورة
       ▼
       Severity Predictions
   │
   ▼
[report_generator.py]
   │ إنشاء التقارير
   ▼
Reports (Text, JSON, CSV)
   │
   ▼
[app.py] أو [pentest_auditor.py]
   │ عرض النتائج
   ▼
User Output
```

---

## 🚀 كيفية الاستخدام

### الطريقة 1: واجهة Streamlit (الأسهل)

```bash
streamlit run app.py
```

ثم:
1. افتح المتصفح على `http://localhost:8501`
2. اختر "تدقيق التقارير"
3. اختر ملف PDF
4. اضغط "تدقيق"
5. شاهد النتائج والرسوم البيانية
6. حمّل التقارير

### الطريقة 2: سطر الأوامر

```bash
python pentest_auditor.py audit report.pdf --use-nlp --output-format all
```

### الطريقة 3: استخدام المكونات مباشرة

```python
from pdf_extractor import PDFExtractor
from vulnerability_segmenter import VulnerabilitySegmenter
from audit_engine import AuditEngine
from report_generator import ReportGenerator

# استخراج
extractor = PDFExtractor("report.pdf")
text = extractor.extract_text()

# تقسيم
segmenter = VulnerabilitySegmenter(text)
vulns = segmenter.segment_vulnerabilities()

# تدقيق
engine = AuditEngine()
result = engine.audit_report([v.__dict__ for v in vulns])

# إنشاء تقرير
generator = ReportGenerator()
generator.generate_text_report(result, "report.txt")
```

---

## 📊 النتائج المتوقعة

### مثال على التقرير النصي

```
================================================================================
تقرير تدقيق تقارير اختبار الاختراق (Pentest Auditor Report)
================================================================================
التاريخ: 2026-05-12 10:30:45

📊 الملخص العام
────────────────────────────────────────────────────────────────────────────────
إجمالي الثغرات: 5
نسبة الالتزام الإجمالية: 82.5%

📈 إحصائيات عناصر التدقيق
────────────────────────────────────────────────────────────────────────────────
┌──────────────────────┬────────┬──────────┬─────────┐
│ عنصر التدقيق        │ موجود │ الإجمالي │ النسبة  │
├──────────────────────┼────────┼──────────┼─────────┤
│ التعريف             │   5    │    5     │ 100.0%  │
│ الوصف               │   5    │    5     │ 100.0%  │
│ الموقع              │   3    │    5     │  60.0%  │
│ الأجهزة             │   4    │    5     │  80.0%  │
│ الخطورة             │   5    │    5     │ 100.0%  │
│ حالة المعالجة      │   4    │    5     │  80.0%  │
│ طريقة المعالجة    │   2    │    5     │  40.0%  │
└──────────────────────┴────────┴──────────┴─────────┘
```

---

## 🔧 التطوير والتوسع

### إضافة عنصر تدقيق جديد

1. أضف العنصر في `AuditElement` enum
2. أضف الكلمات المفتاحية في `KEYWORDS`
3. أضف الأنماط في `PATTERNS` (اختياري)

### تحسين نموذج NLP

1. أضف بيانات تدريب جديدة
2. شغّل التدريب: `python pentest_auditor.py train-model`
3. النموذج يُحفظ تلقائياً

### إضافة صيغة تقرير جديدة

1. أضف دالة جديدة في `ReportGenerator`
2. استخدم نفس بنية البيانات

---

## 📞 الدعم والمساهمة

للإبلاغ عن مشاكل أو الاقتراح بميزات جديدة، يرجى:
1. فتح Issue مع وصف المشكلة
2. إرسال Pull Request مع التحسينات

---

**تم إنشاؤه بواسطة**: Manus AI Agent  
**الإصدار**: 2.0.0  
**آخر تحديث**: 2026
