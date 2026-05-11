# 📦 دليل التثبيت التفصيلي - Installation Guide

## 🖥️ المتطلبات

- **Python**: 3.8 أو أحدث
- **pip**: مدير الحزم
- **RAM**: 2GB على الأقل
- **مساحة**: 500MB على الأقل

---

## 🐧 Linux / macOS

### الخطوة 1: تحديث النظام

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get upgrade

# macOS
brew update
```

### الخطوة 2: التحقق من Python

```bash
python3 --version
```

يجب أن تكون النتيجة 3.8 أو أحدث.

### الخطوة 3: إنشاء Virtual Environment (اختياري لكن موصى به)

```bash
cd pentest-auditor-project
python3 -m venv venv
source venv/bin/activate
```

### الخطوة 4: تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### الخطوة 5: التحقق من التثبيت

```bash
python3 -c "import streamlit; print('✓ Streamlit installed')"
python3 -c "import pdfplumber; print('✓ pdfplumber installed')"
python3 -c "import sklearn; print('✓ scikit-learn installed')"
```

---

## 🪟 Windows

### الخطوة 1: التحقق من Python

```cmd
python --version
```

إذا لم يكن Python مثبتاً، حمّله من: https://www.python.org/

### الخطوة 2: فتح Command Prompt

اضغط `Win + R` واكتب `cmd` ثم Enter

### الخطوة 3: الانتقال إلى مجلد المشروع

```cmd
cd C:\path\to\pentest-auditor-project
```

### الخطوة 4: إنشاء Virtual Environment (اختياري)

```cmd
python -m venv venv
venv\Scripts\activate
```

### الخطوة 5: تثبيت المكتبات

```cmd
pip install -r requirements.txt
```

### الخطوة 6: التحقق من التثبيت

```cmd
python -c "import streamlit; print('✓ Streamlit installed')"
```

---

## 🐳 Docker (اختياري)

### إنشاء Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

### البناء والتشغيل

```bash
docker build -t pentest-auditor .
docker run -p 8501:8501 pentest-auditor
```

---

## 🔧 استكشاف مشاكل التثبيت

### المشكلة 1: "command not found: python3"

**الحل**: تثبيت Python من https://www.python.org/

### المشكلة 2: "Permission denied"

**الحل**:
```bash
chmod +x pentest_auditor.py
```

### المشكلة 3: "pip: command not found"

**الحل**:
```bash
python3 -m pip install -r requirements.txt
```

### المشكلة 4: "ModuleNotFoundError"

**الحل**: تأكد من تثبيت جميع المكتبات:
```bash
pip install -r requirements.txt --upgrade
```

### المشكلة 5: مشاكل مع pdfplumber

**الحل**:
```bash
pip install pdfplumber --upgrade
```

---

## ✅ التحقق من التثبيت الناجح

### اختبار سريع

```bash
python3 pentest_auditor.py version
```

يجب أن تظهر: `Pentest Auditor v1.0.0`

### اختبار استخراج PDF

```bash
python3 pentest_auditor.py extract sample_report.pdf
```

يجب أن يظهر محتوى الملف

### اختبار Streamlit

```bash
streamlit run app.py
```

يجب أن يفتح المتصفح تلقائياً على `http://localhost:8501`

---

## 📋 قائمة المكتبات

| المكتبة | الإصدار | الوصف |
|--------|---------|-------|
| PyPDF2 | 3.0.1 | استخراج النصوص من PDF |
| pdfplumber | 0.10.3 | معالجة PDF متقدمة |
| nltk | 3.8.1 | معالجة اللغات الطبيعية |
| scikit-learn | 1.3.2 | تعلم الآلة |
| numpy | 1.24.3 | معالجة البيانات |
| pandas | 2.0.3 | تحليل البيانات |
| spacy | 3.7.2 | NLP متقدمة |
| textblob | 0.17.1 | معالجة النصوص |
| python-dotenv | 1.0.0 | إدارة المتغيرات |
| click | 8.1.7 | إنشاء CLI |
| tabulate | 0.9.0 | طباعة الجداول |
| tqdm | 4.66.1 | شريط التقدم |
| streamlit | 1.28.1 | واجهة ويب |
| plotly | 5.17.0 | رسوم بيانية |

---

## 🔄 تحديث المكتبات

```bash
pip install -r requirements.txt --upgrade
```

---

## 🗑️ إزالة التثبيت

### حذف Virtual Environment

```bash
# Linux/macOS
rm -rf venv

# Windows
rmdir /s venv
```

### حذف المكتبات

```bash
pip uninstall -r requirements.txt -y
```

---

## 🌍 التثبيت بدون اتصال إنترنت

### 1. تحميل المكتبات على جهاز متصل

```bash
pip download -r requirements.txt -d ./packages
```

### 2. نسخ مجلد packages إلى الجهاز غير المتصل

### 3. التثبيت من المجلد

```bash
pip install --no-index --find-links ./packages -r requirements.txt
```

---

## 🚀 الخطوات التالية

بعد التثبيت الناجح:

1. اقرأ `QUICK_START.md` للبدء السريع
2. اقرأ `README_AR.md` للشرح الشامل
3. شغّل `streamlit run app.py`
4. جرّب مع ملف PDF

---

## 📞 الدعم

إذا واجهت مشاكل:

1. تحقق من متطلبات Python (3.8+)
2. أعد تثبيت المكتبات: `pip install -r requirements.txt --upgrade`
3. جرّب في Virtual Environment جديد
4. تحقق من مساحة التخزين المتاحة

---

**تم إنشاؤه بواسطة**: Manus AI Agent  
**الإصدار**: 2.0.0
