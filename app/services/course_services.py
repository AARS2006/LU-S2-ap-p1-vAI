from app.models.course import Course
from app.data import storage
from app.data.storage import save_all
from app.exceptions.custom_exceptions import (
    CourseNotFoundException,
    CourseAlreadyExistsException
)

#ساخت دوره جدید
def create_course(major, title, code, unit, capacity):
    # بررسی کن درس با این کد از قبل وجود نداشته باشه
    for c in storage.courses:
        if c["code"] == code:
            raise CourseAlreadyExistsException("درس با این کد قبلاً ثبت شده است")

    # ساخت شیء درس
    course = Course(
        course_id = storage.course_id_counter,
        title = title,
        code = code,
        unit = unit,
        capacity = capacity,
        major = major
    )

    # یکی به شمارنده اضافه کن
    storage.course_id_counter += 1

    # تبدیل شیء به دیکشنری و اضافه کردن به لیست
    storage.courses.append(course.to_dict())

    # ذخیره در فایل
    save_all()

    return course.to_dict()

#لیست همه دوره ها
def get_all_courses():
    return storage.courses

#جستجو دوره با کد درس
def get_course_by_id(code):
    for c in storage.courses:
        if c["code"] == code:
            return c

    raise CourseNotFoundException("درس با این کد پیدا نشد")

#بروزرسانی اطلاعات دوره
def update_course(code, data):
    for c in storage.courses:
        if c["code"] == code:

            # اگه کد جدید داده شده، بررسی کن تکراری نباشه
            if data.code is not None:
                for other in storage.courses:
                    if other["code"] == data.code and other["code"] != code:
                        raise CourseAlreadyExistsException("این کد درس قبلاً ثبت شده است")

            # فقط فیلدهایی که None نیستن رو آپدیت کن
            if data.major is not None:
                c["major"] = data.major
            if data.title is not None:
                c["title"] = data.title
            if data.code is not None:
                c["code"] = data.code
            if data.unit is not None:
                c["unit"] = data.unit
            if data.capacity is not None:
                c["capacity"] = data.capacity

            save_all()
            return c

    raise CourseNotFoundException("درس با این کد پیدا نشد")

#حذف دوره
def delete_course(code):
    for c in storage.courses:
        if c["code"] == code:
            storage.courses.remove(c)
            save_all()
            return "درس با موفقیت حذف شد"

    raise CourseNotFoundException("درس با این کد پیدا نشد")