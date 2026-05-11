# 🚀 البدء السريع - Quick Start Guide

## ⚡ التثبيت في 3 خطوات

### 1️⃣ استنساخ أو تحميل المشروع

```bash
cd pentest-auditor-project
```

### 2️⃣ تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### 3️⃣ تشغيل التطبيق

اختر أحد الخيارات:

#### **الخيار A: واجهة Streamlit (الأسهل والأفضل)** 🌐

```bash
streamlit run app.py
```

ثم افتح المتصفح على: `http://localhost:8501`

#### **الخيار B: سطر الأوامر** 🖥️

```bash
python pentest_auditor.py audit report.pdf --use-nlp --output-format all
```

---

## 📖 الاستخدام الأساسي

### مع Streamlit (الواجهة التفاعلية)

1. **افتح التطبيق**:
   ```bash
   streamlit run app.py
   ```

2. **اختر "تدقيق التقارير"** من القائمة الجانبية

3. **اختر ملف PDF** من جهازك

4. **اضغط "تدقيق"** وانتظر النتائج

5. **شاهد النتائج** في 4 تبويبات:
   - 📊 **النتائج**: ملخص سريع
   - 🔍 **التفاصيل**: تفاصيل كل ثغرة
   - 📈 **الرسوم البيانية**: رسوم توضيحية
   - 📥 **التقارير**: تحميل بصيغ مختلفة

### مع سطر الأوامر

#### تدقيق ملف PDF

```bash
python pentest_auditor.py audit report.pdf
```

#### مع خيارات متقدمة

```bash
python pentest_auditor.py audit report.pdf \
  --use-nlp \
  --output-format all \
  --output-dir ./reports
```

#### استخراج النصوص فقط

```bash
python pentest_auditor.py extract report.pdf
```

#### تقسيم التقرير إلى ثغرات

```bash
python pentest_auditor.py segment report.pdf
```

#### تدريب النموذج

```bash
python pentest_auditor.py train-model --use-sample-data
```

---

## 📊 مثال عملي

### السيناريو: تدقيق تقرير Pentest

```bash
# 1. تشغيل التطبيق
streamlit run app.py

# 2. في الواجهة:
#    - اختر "تدقيق التقارير"
#    - اختر ملف PDF (مثلاً: security_report.pdf)
#    - اضغط "تدقيق"

# 3. شاهد النتائج:
#    - عدد الثغرات المكتشفة
#    - نسبة الالتزام الإجمالية
#    - تفاصيل كل ثغرة
#    - الرسوم البيانية

# 4. حمّل التقرير:
#    - اختر صيغة (Text, JSON, CSV)
#    - اضغط "تحميل"
```

---

## 🎯 الخيارات المتاحة

### أوامر CLI

| الأمر | الوصف | المثال |
|-------|-------|--------|
| `audit` | تدقيق ملف PDF | `python pentest_auditor.py audit report.pdf` |
| `extract` | استخراج النصوص | `python pentest_auditor.py extract report.pdf` |
| `segment` | تقسيم إلى ثغرات | `python pentest_auditor.py segment report.pdf` |
| `train-model` | تدريب النموذج | `python pentest_auditor.py train-model` |
| `version` | عرض الإصدار | `python pentest_auditor.py version` |

### خيارات audit

```bash
python pentest_auditor.py audit report.pdf \
  --use-nlp                    # استخدام NLP
  --output-format all          # صيغة الإخراج (text, json, csv, all)
  --output-dir ./reports       # مجلد الإخراج
```

---

## 📁 الملفات المهمة

| الملف | الوصف |
|------|-------|
| `app.py` | تطبيق Streamlit (الواجهة التفاعلية) |
| `pentest_auditor.py` | تطبيق CLI (سطر الأوامر) |
| `README_AR.md` | شرح شامل للمشروع |
| `PROJECT_STRUCTURE.md` | هيكل المشروع التفصيلي |
| `requirements.txt` | المكتبات المطلوبة |

---

## ⚙️ الإعدادات الأساسية

### تغيير مجلد الإخراج

```bash
python pentest_auditor.py audit report.pdf --output-dir ./my_reports
```

### استخدام صيغة معينة

```bash
# نصي فقط
python pentest_auditor.py audit report.pdf --output-format text

# JSON فقط
python pentest_auditor.py audit report.pdf --output-format json

# CSV فقط
python pentest_auditor.py audit report.pdf --output-format csv

# جميع الصيغ
python pentest_auditor.py audit report.pdf --output-format all
```

---

## 🔧 استكشاف الأخطاء

### المشكلة: "ModuleNotFoundError"

**الحل**: تأكد من تثبيت المكتبات:
```bash
pip install -r requirements.txt
```

### المشكلة: لا يتم استخراج النصوص

**الحل**: تأكد من أن الملف ليس محمياً بكلمة مرور

### المشكلة: Streamlit لا يعمل

**الحل**: أعد تثبيت Streamlit:
```bash
pip install --upgrade streamlit
```

### المشكلة: بطء المعالجة

**الحل**: تأكد من أن الملف ليس كبير جداً (> 100 MB)

---

## 📊 النتائج المتوقعة

### ملخص التدقيق

```
📋 ملخص التدقيق السريع
============================================================
إجمالي الثغرات: 5
نسبة الالتزام: 82.5%
التقييم: جيد جداً ✓✓
============================================================
```

### جدول النتائج

| العنصر | الحالة | الثقة |
|--------|--------|-------|
| التعريف | ✓ | 95% |
| الوصف | ✓ | 90% |
| الموقع | ✗ | 20% |
| الأجهزة | ✓ | 85% |
| الخطورة | ✓ | 100% |
| حالة المعالجة | ✓ | 80% |
| طريقة المعالجة | ✓ | 75% |

---

## 🎓 أمثلة متقدمة

### استخدام المكونات مباشرة

```python
from pdf_extractor import PDFExtractor
from vulnerability_segmenter import VulnerabilitySegmenter
from audit_engine import AuditEngine

# استخراج النصوص
extractor = PDFExtractor("report.pdf")
text = extractor.extract_text()

# تقسيم إلى ثغرات
segmenter = VulnerabilitySegmenter(text)
vulnerabilities = segmenter.segment_vulnerabilities()

# تدقيق
engine = AuditEngine()
for vuln in vulnerabilities:
    report = engine.audit_vulnerability(
        vuln.id,
        vuln.title,
        vuln.content
    )
    print(f"Compliance: {report.compliance_percentage:.1f}%")
```

### تدريب النموذج

```python
from nlp_model_trainer import NLPModelTrainer

trainer = NLPModelTrainer()
sample_data = trainer.create_sample_training_data()
texts, labels = trainer.prepare_training_data(sample_data)
trainer.train(texts, labels)
trainer.save_model()
```

---

## 📞 الدعم

للمزيد من المعلومات، راجع:
- 📄 `README_AR.md` - شرح شامل
- 📁 `PROJECT_STRUCTURE.md` - هيكل المشروع
- 🐍 ملفات `.py` - الكود المصدري

---

**استمتع باستخدام برنامج تدقيق تقارير اختبار الاختراق! 🎉**

تم إنشاؤه بواسطة: **Manus AI Agent**  
الإصدار: **2.0.0**
