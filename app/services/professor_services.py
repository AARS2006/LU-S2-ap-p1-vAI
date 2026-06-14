from app.models.professor import Professor
from app.data import storage
from app.data.storage import save_all
from app.exceptions.custom_exceptions import (
    ProfessorNotFoundException,
    ProfessorAlreadyExistsException
)

#ایجاد استاد جدید
def create_professor(first_name, last_name, personnel_code, department):
    # بررسی کن استاد با این کد پرسنلی از قبل وجود نداشته باشه
    for p in storage.professors:
        if p["personnel_code"] == personnel_code:
            raise ProfessorAlreadyExistsException("استاد با این کد پرسنلی قبلاً ثبت شده است")

    # ساخت شیء استاد
    professor = Professor(
        id = storage.professor_id_counter,
        first_name = first_name,
        last_name = last_name,
        personnel_code = personnel_code,
        department = department
    )

    # یکی به شمارنده اضافه کن
    storage.professor_id_counter += 1

    # تبدیل شیء به دیکشنری و اضافه کردن به لیست
    storage.professors.append(professor.to_dict())

    # ذخیره در فایل
    save_all()

    return professor.to_dict()

#لیست همه اساتید ثبت شده
def get_all_professors():
    return storage.professors

#جستجو استاد با کد پرسنلی
def get_professor_by_id(personnel_code):
    for p in storage.professors:
        if p["personnel_code"] == personnel_code:
            return p

    raise ProfessorNotFoundException("استاد با این کد پرسنلی پیدا نشد")

#بروزرسانی اطلاعات اساتید
def update_professor(personnel_code, data):
    for p in storage.professors:
        if p["personnel_code"] == personnel_code:

            # اگه کد پرسنلی جدید داده شده، بررسی کن تکراری نباشه
            if data.personnel_code is not None:
                for other in storage.professors:
                    if other["personnel_code"] == data.personnel_code and other["personnel_code"] != personnel_code:
                        raise ProfessorAlreadyExistsException("این کد پرسنلی قبلاً ثبت شده است")

            # فقط فیلدهایی که None نیستن رو آپدیت کن
            if data.first_name is not None:
                p["first_name"] = data.first_name
            if data.last_name is not None:
                p["last_name"] = data.last_name
            if data.personnel_code is not None:
                p["personnel_code"] = data.personnel_code
            if data.department is not None:
                p["department"] = data.department

            save_all()
            return p

    raise ProfessorNotFoundException("استاد با این کد پرسنلی پیدا نشد")

#حذف استاد
def delete_professor(personnel_code):
    for p in storage.professors:
        if p["personnel_code"] == personnel_code:
            storage.professors.remove(p)
            save_all()
            return "استاد با موفقیت حذف شد"

    raise ProfessorNotFoundException("استاد با این کد پرسنلی پیدا نشد")