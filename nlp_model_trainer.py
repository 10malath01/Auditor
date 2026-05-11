"""
NLP Model Trainer Module
تدريب نموذج NLP لتحسين فهم محتوى التقارير
"""

import re
import pickle
import numpy as np
from typing import List, Tuple, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from pathlib import Path


class NLPModelTrainer:
    """فئة لتدريب نموذج NLP"""
    
    def __init__(self, model_path: str = "models/nlp_model.pkl"):
        """
        تهيئة المدرب
        
        Args:
            model_path: مسار حفظ النموذج
        """
        self.model_path = Path(model_path)
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        self.pipeline = None
        self.is_trained = False
    
    def prepare_training_data(self, vulnerabilities: List[Dict]) -> Tuple[List[str], List[int]]:
        """
        تحضير بيانات التدريب من الثغرات
        
        Args:
            vulnerabilities: قائمة الثغرات
            
        Returns:
            (النصوص، التصنيفات)
        """
        texts = []
        labels = []
        
        severity_mapping = {
            'critical': 4,
            'high': 3,
            'medium': 2,
            'low': 1,
            'info': 0,
            'unknown': 0
        }
        
        for vuln in vulnerabilities:
            text = vuln.get('content', '')
            severity = vuln.get('severity', 'unknown').lower()
            label = severity_mapping.get(severity, 0)
            
            if text:
                # تنظيف النص
                cleaned_text = self._preprocess_text(text)
                texts.append(cleaned_text)
                labels.append(label)
        
        return texts, labels
    
    def _preprocess_text(self, text: str) -> str:
        """
        معالجة النص مسبقاً
        
        Args:
            text: النص المراد معالجته
            
        Returns:
            النص المعالج
        """
        # تحويل إلى أحرف صغيرة
        text = text.lower()
        
        # إزالة الأحرف الخاصة
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        
        # إزالة المسافات الزائدة
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def train(self, texts: List[str], labels: List[int], test_size: float = 0.2):
        """
        تدريب النموذج
        
        Args:
            texts: قائمة النصوص
            labels: قائمة التصنيفات
            test_size: نسبة بيانات الاختبار
        """
        if len(texts) < 2:
            print("⚠️  عدد النصوص غير كافي للتدريب (يجب أن يكون على الأقل 2)")
            return False
        
        # تقسيم البيانات
        X_train, X_test, y_train, y_test = train_test_split(
            texts, labels, test_size=test_size, random_state=42
        )
        
        # بناء Pipeline
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=1000, ngram_range=(1, 2))),
            ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
        ])
        
        # التدريب
        self.pipeline.fit(X_train, y_train)
        
        # حساب الدقة
        train_score = self.pipeline.score(X_train, y_train)
        test_score = self.pipeline.score(X_test, y_test)
        
        self.is_trained = True
        
        print(f"✓ تم تدريب النموذج بنجاح")
        print(f"   دقة التدريب: {train_score*100:.2f}%")
        print(f"   دقة الاختبار: {test_score*100:.2f}%")
        
        return True
    
    def predict_severity(self, text: str) -> Dict:
        """
        التنبؤ بتصنيف الخطورة
        
        Args:
            text: نص الثغرة
            
        Returns:
            قاموس يحتوي على التنبؤ والثقة
        """
        if not self.is_trained:
            return {'error': 'النموذج لم يتم تدريبه بعد'}
        
        # معالجة النص
        cleaned_text = self._preprocess_text(text)
        
        # التنبؤ
        prediction = self.pipeline.predict([cleaned_text])[0]
        probabilities = self.pipeline.predict_proba([cleaned_text])[0]
        confidence = max(probabilities)
        
        # تحويل التنبؤ إلى اسم
        severity_names = ['info', 'low', 'medium', 'high', 'critical']
        predicted_severity = severity_names[prediction]
        
        return {
            'predicted_severity': predicted_severity,
            'confidence': float(confidence),
            'probabilities': {
                name: float(prob)
                for name, prob in zip(severity_names, probabilities)
            }
        }
    
    def save_model(self):
        """حفظ النموذج"""
        if self.pipeline:
            with open(self.model_path, 'wb') as f:
                pickle.dump(self.pipeline, f)
            print(f"✓ تم حفظ النموذج في: {self.model_path}")
            return True
        return False
    
    def load_model(self) -> bool:
        """تحميل النموذج"""
        if self.model_path.exists():
            with open(self.model_path, 'rb') as f:
                self.pipeline = pickle.load(f)
            self.is_trained = True
            print(f"✓ تم تحميل النموذج من: {self.model_path}")
            return True
        return False
    
    @staticmethod
    def create_sample_training_data() -> List[Dict]:
        """
        إنشاء بيانات تدريب عينة
        
        Returns:
            قائمة الثغرات العينة
        """
        sample_data = [
            {
                'id': 1,
                'title': 'SQL Injection',
                'severity': 'critical',
                'content': 'SQL injection vulnerability found in login form. Attackers can execute arbitrary SQL queries.'
            },
            {
                'id': 2,
                'title': 'Cross-Site Scripting',
                'severity': 'high',
                'content': 'XSS vulnerability in user profile page. User input is not properly sanitized.'
            },
            {
                'id': 3,
                'title': 'Weak Password Policy',
                'severity': 'medium',
                'content': 'Password policy does not enforce complexity requirements.'
            },
            {
                'id': 4,
                'title': 'Missing Security Headers',
                'severity': 'medium',
                'content': 'Security headers like CSP and X-Frame-Options are missing.'
            },
            {
                'id': 5,
                'title': 'Outdated Dependencies',
                'severity': 'high',
                'content': 'Several dependencies have known vulnerabilities.'
            },
            {
                'id': 6,
                'title': 'Unencrypted Data Transmission',
                'severity': 'critical',
                'content': 'Sensitive data is transmitted over unencrypted HTTP connections.'
            },
            {
                'id': 7,
                'title': 'Broken Authentication',
                'severity': 'critical',
                'content': 'Authentication mechanism is broken and can be bypassed.'
            },
            {
                'id': 8,
                'title': 'Information Disclosure',
                'severity': 'low',
                'content': 'Application reveals sensitive information in error messages.'
            },
        ]
        
        return sample_data


if __name__ == "__main__":
    # اختبار المدرب
    trainer = NLPModelTrainer()
    
    # إنشاء بيانات تدريب عينة
    sample_data = trainer.create_sample_training_data()
    
    # تحضير البيانات
    texts, labels = trainer.prepare_training_data(sample_data)
    
    print(f"📊 بيانات التدريب:")
    print(f"   عدد النصوص: {len(texts)}")
    print(f"   عدد التصنيفات: {len(labels)}")
    
    # التدريب
    print(f"\n🤖 جاري التدريب...")
    trainer.train(texts, labels)
    
    # الحفظ
    trainer.save_model()
    
    # اختبار التنبؤ
    print(f"\n🔮 اختبار التنبؤ:")
    test_text = "Critical vulnerability in authentication system allows attackers to bypass login"
    result = trainer.predict_severity(test_text)
    print(f"   النص: {test_text}")
    print(f"   التنبؤ: {result['predicted_severity']}")
    print(f"   الثقة: {result['confidence']*100:.2f}%")
