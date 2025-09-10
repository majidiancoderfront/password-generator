# سازنده پسورد Django

یک برنامه وب برای تولید پسوردهای امن و قوی با استفاده از Django.

## ویژگی‌ها

- تولید پسوردهای قابل تنظیم با طول 4 تا 128 کاراکتر
- انتخاب نوع کاراکترها (حروف بزرگ، کوچک، اعداد، نمادها)
- رابط کاربری زیبا و ریسپانسیو
- تاریخچه پسوردهای تولید شده
- قابلیت کپی کردن پسوردها
- طراحی فارسی و RTL

## نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.8 یا بالاتر
- pip

### مراحل نصب

1. کلون کردن پروژه:
```bash
git clone <repository-url>
cd pass_genator
```

2. ایجاد محیط مجازی:
```bash
python -m venv venv
```

3. فعال‌سازی محیط مجازی:
```bash
# در Windows
venv\Scripts\activate

# در Linux/Mac
source venv/bin/activate
```

4. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

5. اجرای مایگریشن‌ها:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. ایجاد ابرکاربر (اختیاری):
```bash
python manage.py createsuperuser
```

7. اجرای سرور:
```bash
python manage.py runserver
```

8. باز کردن مرورگر و رفتن به:
```
http://127.0.0.1:8000
```

## استفاده

1. **تولید پسورد جدید:**
   - طول پسورد را با اسلایدر تنظیم کنید
   - نوع کاراکترهای مورد نظر را انتخاب کنید
   - روی دکمه "تولید پسورد" کلیک کنید

2. **کپی کردن پسورد:**
   - پس از تولید پسورد، روی دکمه "کپی" کلیک کنید

3. **مشاهده تاریخچه:**
   - از منوی بالا روی "تاریخچه" کلیک کنید
   - تمام پسوردهای تولید شده را مشاهده کنید

## ساختار پروژه

```
pass_genator/
├── manage.py
├── requirements.txt
├── README.md
├── pass_generator/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── generator/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── templates/
    ├── base.html
    └── generator/
        ├── home.html
        └── history.html
```

## مدل‌ها

### GeneratedPassword
- `password`: پسورد تولید شده
- `length`: طول پسورد
- `include_uppercase`: شامل حروف بزرگ
- `include_lowercase`: شامل حروف کوچک
- `include_numbers`: شامل اعداد
- `include_symbols`: شامل نمادها
- `created_at`: تاریخ تولید

## API

### POST /generate/
تولید پسورد جدید

**پارامترها:**
- `length`: طول پسورد (4-128)
- `include_uppercase`: شامل حروف بزرگ (true/false)
- `include_lowercase`: شامل حروف کوچک (true/false)
- `include_numbers`: شامل اعداد (true/false)
- `include_symbols`: شامل نمادها (true/false)

**پاسخ:**
```json
{
    "password": "GeneratedPassword123!",
    "length": 20,
    "include_uppercase": true,
    "include_lowercase": true,
    "include_numbers": true,
    "include_symbols": true
}
```

## نکات امنیتی

- از پسوردهای طولانی استفاده کنید (حداقل 12 کاراکتر)
- ترکیبی از حروف، اعداد و نمادها استفاده کنید
- از پسوردهای یکسان برای حساب‌های مختلف استفاده نکنید
- پسوردهای خود را به صورت منظم تغییر دهید

## توسعه

برای توسعه این پروژه:

1. Fork کنید
2. شاخه جدید ایجاد کنید
3. تغییرات خود را اعمال کنید
4. Pull Request ارسال کنید

## مجوز

این پروژه تحت مجوز MIT منتشر شده است.
