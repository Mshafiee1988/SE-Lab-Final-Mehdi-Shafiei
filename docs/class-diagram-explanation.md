# Class Diagram Relationship Explanation

## Student — Enrollment
Type: Composition

Reason:
هر Enrollment متعلق به یک Student است و بدون وجود دانشجو معنا ندارد. اگر دانشجو از سیستم حذف شود، تمام رکوردهای ثبت‌نام او نیز حذف خواهند شد؛ بنابراین رابطه Composition مناسب است.

---

## Enrollment — Course
Type: Aggregation

Reason:
یک Course می‌تواند حتی بدون هیچ دانشجویی وجود داشته باشد. Enrollment ها به Course مرتبط هستند اما مالک Course نیستند؛ بنابراین رابطه Aggregation انتخاب شده است.

---

## Course — Professor
Type: Association

Reason:
یک Professor می‌تواند چندین Course را تدریس کند و یک Course نیز می‌تواند در ترم‌های مختلف به اساتید متفاوت اختصاص یابد. هر دو موجودیت مستقل از یکدیگر وجود دارند، بنابراین Association مناسب است.
