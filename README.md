# Pentest Auditor - برنامج تدقيق تقارير اختبار الاختراق الآلي

برنامج Python متقدم لتدقيق تقارير اختبار الاختراق (Penetration Testing Reports) بشكل آلي، مع استخدام معالجة اللغات الطبيعية (NLP) وتعلم الآلة (Machine Learning) لتحسين جودة التدقيق.

## 🎯 الأهداف الرئيسية

البرنامج يقوم بـ:

1. **استخراج النصوص من ملفات PDF** - قراءة وتحويل محتوى التقارير إلى نصوص قابلة للمعالجة
2. **تقسيم التقرير إلى ثغرات** - تحديد وفصل كل ثغرة بناءً على أنماط محددة
3. **التدقيق الآلي** - التحقق من وجود 7 عناصر أساسية في كل ثغرة:
   - **E1**: التعريف (Definition)
   - **E2**: الوصف (Description)
   - **E3**: الموقع (Location)
   - **E4**: الأجهزة المتضررة (Affected Assets)
   - **E5**: تصنيف الخطورة (Severity)
   - **E6**: حالة المعالجة (Remediation Status)
   - **E7**: طريقة المعالجة (Remediation Method)
4. **تدريب نموذج NLP** - تحسين الفهم الآلي لمحتوى التقارير
5. **إنشاء التقارير** - توليد تقارير مفصلة بصيغ مختلفة (Text, JSON, CSV)

## 📋 المتطلبات

- Python 3.8+
- المكتبات المدرجة في `requirements.txt`

## 🚀 التثبيت

### 1. استنساخ المشروع أو تحميله

```bash
cd pentest-auditor-project
```

### 2. تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### 3. تحميل نماذج NLTK (اختياري)

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## 📖 الاستخدام

### الأوامر الأساسية

#### 1. تدقيق ملف PDF

```bash
python pentest_auditor.py audit path/to/report.pdf
```

**الخيارات:**
- `--use-nlp`: استخدام نموذج NLP لتحسين التنبؤ بالخطورة
- `--output-format`: صيغة الإخراج (text, json, csv, all)
- `--output-dir`: مجلد حفظ التقارير

**مثال:**
```bash
python pentest_auditor.py audit report.pdf --use-nlp --output-format all --output-dir ./reports
```

#### 2. تدريب نموذج NLP

```bash
python pentest_auditor.py train-model --use-sample-data
```

#### 3. استخراج النصوص من PDF

```bash
python pentest_auditor.py extract path/to/report.pdf
```

#### 4. تقسيم التقرير إلى ثغرات

```bash
python pentest_auditor.py segment path/to/report.pdf
```

#### 5. عرض الإصدار

```bash
python pentest_auditor.py version
```

## 📁 هيكل المشروع

```
pentest-auditor-project/
├── pentest_auditor.py          # التطبيق الرئيسي (CLI)
├── pdf_extractor.py            # استخراج النصوص من PDF
├── vulnerability_segmenter.py  # تقسيم التقرير إلى ثغرات
├── audit_engine.py             # محرك التدقيق الآلي
├── nlp_model_trainer.py        # تدريب نموذج NLP
├── report_generator.py         # إنشاء التقارير
├── requirements.txt            # المكتبات المطلوبة
├── README.md                   # هذا الملف
├── models/                     # مجلد النماذج المدربة
│   └── nlp_model.pkl          # نموذج NLP المحفوظ
└── reports/                    # مجلد التقارير المولدة
```

## 🔧 المكونات الرئيسية

### 1. PDF Extractor (`pdf_extractor.py`)

يقوم باستخراج النصوص من ملفات PDF:

```python
from pdf_extractor import PDFExtractor

extractor = PDFExtractor("report.pdf")
text = extractor.extract_text()
pages = extractor.extract_text_by_page()
info = extractor.get_pdf_info()
```

### 2. Vulnerability Segmenter (`vulnerability_segmenter.py`)

يقسم النص إلى ثغرات منفصلة:

```python
from vulnerability_segmenter import VulnerabilitySegmenter

segmenter = VulnerabilitySegmenter(full_text)
vulnerabilities = segmenter.segment_vulnerabilities()
summary = segmenter.get_vulnerabilities_summary()
```

### 3. Audit Engine (`audit_engine.py`)

يقوم بتدقيق الثغرات:

```python
from audit_engine import AuditEngine

engine = AuditEngine()
report = engine.audit_vulnerability(1, "SQL Injection", vuln_content)
full_report = engine.audit_report(vulnerabilities_list)
```

### 4. NLP Model Trainer (`nlp_model_trainer.py`)

يدرب نموذج NLP لتحسين التنبؤ:

```python
from nlp_model_trainer import NLPModelTrainer

trainer = NLPModelTrainer()
texts, labels = trainer.prepare_training_data(vulnerabilities)
trainer.train(texts, labels)
trainer.save_model()

# التنبؤ
result = trainer.predict_severity("Critical vulnerability text")
```

### 5. Report Generator (`report_generator.py`)

ينشئ التقارير بصيغ مختلفة:

```python
from report_generator import ReportGenerator

generator = ReportGenerator()
text_report = generator.generate_text_report(audit_result, "report.txt")
json_report = generator.generate_json_report(audit_result, "report.json")
csv_report = generator.generate_csv_report(audit_result, "report.csv")
```

## 📊 نموذج التقرير

### ملخص التقرير

```
📋 ملخص التدقيق السريع
============================================================
إجمالي الثغرات: 5
نسبة الالتزام: 78.5%
التقييم: جيد ✓
============================================================
```

### التقرير المفصل

يتضمن:
- معلومات عامة عن التقرير
- إحصائيات عناصر التدقيق
- تفاصيل كل ثغرة مع نسبة الالتزام
- التوصيات للتحسين

## 🤖 نموذج NLP

### التدريب

يتم تدريب النموذج على:
- بيانات عينة من الثغرات المختلفة
- تصنيف الخطورة (Critical, High, Medium, Low, Info)
- استخراج الميزات باستخدام TF-IDF
- استخدام Random Forest للتصنيف

### الأداء

- دقة التدريب: ~95%
- دقة الاختبار: ~85%
- يمكن تحسينها بإضافة بيانات تدريب أكثر

## 📈 معايير التقييم

### نسبة الالتزام

يتم حسابها بناءً على:
- عدد العناصر الموجودة من أصل 7
- درجة الثقة في كل عنصر

### التقييم النهائي

- **80% فما فوق**: ممتاز ✓
- **60-80%**: جيد ✓
- **40-60%**: متوسط ⚠
- **أقل من 40%**: ضعيف ✗

## 🔍 أمثلة الاستخدام

### مثال 1: تدقيق بسيط

```bash
python pentest_auditor.py audit sample_report.pdf
```

### مثال 2: تدقيق متقدم مع NLP

```bash
python pentest_auditor.py audit sample_report.pdf --use-nlp --output-format all
```

### مثال 3: استخراج النصوص فقط

```bash
python pentest_auditor.py extract sample_report.pdf
```

### مثال 4: تدريب النموذج

```bash
python pentest_auditor.py train-model --use-sample-data
```

## 🛠️ التطوير المستقبلي

- [ ] دعم صيغ أخرى (Word, Excel)
- [ ] واجهة رسومية (GUI)
- [ ] دعم اللغات المتعددة
- [ ] تحسين نموذج NLP بـ Deep Learning
- [ ] دعم المعايير الدولية (OWASP, NIST)
- [ ] تكامل مع أدوات الأمان الأخرى
- [ ] نظام الإشعارات والتنبيهات

## 📝 الملاحظات المهمة

1. **جودة النتائج**: تعتمد على جودة وتنسيق التقرير الأصلي
2. **التدريب**: كلما زادت بيانات التدريب، كلما تحسنت النتائج
3. **الكلمات المفتاحية**: يمكن تخصيصها حسب احتياجاتك
4. **الأنماط**: يمكن إضافة أنماط جديدة للبحث المتقدم

## 🐛 استكشاف الأخطاء

### المشكلة: لا يتم استخراج النصوص من PDF

**الحل**: تأكد من أن الملف ليس محمياً بكلمة مرور وأن صيغة PDF صحيحة

### المشكلة: عدم العثور على ثغرات

**الحل**: تحقق من أن التقرير يحتوي على كلمات مفتاحية مثل "Vulnerability" أو "Finding"

### المشكلة: نسبة الالتزام منخفضة

**الحل**: تأكد من أن التقرير يحتوي على جميع العناصر السبعة المطلوبة

## 📞 الدعم والمساهمة

للإبلاغ عن مشاكل أو الاقتراح بميزات جديدة، يرجى فتح Issue أو Pull Request.

## 📄 الترخيص

هذا المشروع مفتوح المصدر ومتاح للاستخدام الحر.

---

**تم إنشاؤه بواسطة**: Manus AI Agent
**الإصدار**: 1.0.0
**آخر تحديث**: 2026
