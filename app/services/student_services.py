from app.models.student import Student
from app.data import storage
from app.data.storage import save_all
from app.exceptions.custom_exceptions import (
    StudentNotFoundException,
    StudentAlreadyExistsException
)

#ایجاد دانشجو جدید
def create_student(first_name, last_name, student_number, major):
    # بررسی اینکه دانشجو با این شماره دانشجویی از قبل وجود نداشته باشه
    for s in storage.students:
        if s["student_number"] == student_number:
            raise StudentAlreadyExistsException("دانشجو با این شماره دانشجویی قبلاً ثبت شده است")

    # ساخت شیء دانشجو
    student = Student(
        id = storage.student_id_counter,
        first_name = first_name,
        last_name = last_name,
        student_number = student_number,
        major = major
    )

    # یکی به شمارنده اضافه کن
    storage.student_id_counter += 1

    # تبدیل شیء به دیکشنری و اضافه کردن به لیست
    storage.students.append(student.to_dict())

    # ذخیره در فایل
    save_all()

    return student.to_dict()

#دانشجویان ثبت شده
def get_all_students():
    # برگرداندن همه دانشجویان
    return storage.students

#جستجو با شماره دانشجویی
def get_student_by_id(student_number):
    # دنبال دانشجو با این شماره دانشجویی بگرد
    for s in storage.students:
        if s["student_number"] == student_number:
            return s

    # اگه پیدا نشد خطا بده
    raise StudentNotFoundException("دانشجو با این شماره دانشجویی پیدا نشد")

#بروزرسانی اطلاعات دانشجو
def update_student(student_number, data):
    # دنبال دانشجو بگرد
    for s in storage.students:
        if s["student_number"] == student_number:

            # اگه شماره دانشجویی جدید داده شده، بررسی کن تکراری نباشه
            if data.student_number is not None:
                for other in storage.students:
                    if other["student_number"] == data.student_number and other["student_number"] != student_number:
                        raise StudentAlreadyExistsException("این شماره دانشجویی قبلاً ثبت شده است")

            # فقط فیلدهایی که None نیستن رو آپدیت کن
            if data.first_name is not None:
                s["first_name"] = data.first_name
            if data.last_name is not None:
                s["last_name"] = data.last_name
            if data.student_number is not None:
                s["student_number"] = data.student_number
            if data.major is not None:
                s["major"] = data.major

            # ذخیره در فایل
            save_all()
            return s

    raise StudentNotFoundException("دانشجو با این شماره دانشجویی پیدا نشد")

#حذف دانشجو
def delete_student(student_number):
    # سرچ دانشجو
    for s in storage.students:
        if s["student_number"] == student_number:
            storage.students.remove(s)
            save_all()
            return "دانشجو با موفقیت حذف شد"

    raise StudentNotFoundException("دانشجو با این شماره دانشجویی پیدا نشد")