# نظام إدارة الشهادات

نظام لعرض وإدارة شهادات الموظفين باستخدام Flask و Supabase.

## المميزات
- عرض قائمة الشهادات
- عرض أفضل 3 موظفين حاصلين على شهادات
- تصفية حسب القسم
- واجهة مستخدم عربية

## المتطلبات
- Python 3.8+
- Flask
- Supabase
- متطلبات أخرى في `requirements.txt`

## التثبيت والإعداد

1. استنساخ المشروع:
```bash
git clone [رابط-المستودع]
cd supabase-demo
```

2. إنشاء بيئة افتراضية وتفعيلها:
```bash
python -m venv venv
source venv/bin/activate  # لينكس/ماك
# أو
venv\Scripts\activate  # ويندوز
```

3. تثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

4. إعداد متغيرات البيئة:
- قم بتعيين `SUPABASE_URL` و `SUPABASE_KEY` في متغيرات البيئة
- أو قم بتعديل القيم في `config.py`

5. تشغيل التطبيق:
```bash
python app.py
```

## هيكل المشروع
```
supabase-demo/
├── app.py              # تطبيق Flask الرئيسي
├── config.py           # إعدادات التطبيق
├── requirements.txt    # متطلبات Python
└── templates/         
    └── index.html      # قالب الصفحة الرئيسية
```

## الأمان
- تأكد من عدم مشاركة مفاتيح API في التعليمات البرمجية
- استخدم متغيرات البيئة للإعدادات الحساسة
- قم بتعيين `FLASK_ENV=production` في بيئة الإنتاج

## المساهمة
نرحب بالمساهمات! يرجى اتباع هذه الخطوات:
1. Fork المشروع
2. إنشاء فرع للميزة (`git checkout -b feature/amazing-feature`)
3. Commit التغييرات (`git commit -m 'إضافة ميزة رائعة'`)
4. Push إلى الفرع (`git push origin feature/amazing-feature`)
5. فتح Pull Request
