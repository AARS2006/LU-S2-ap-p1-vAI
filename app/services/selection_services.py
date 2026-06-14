from app.data import storage
from app.data.storage import save_all
from app.exceptions.custom_exceptions import (
    StudentNotFoundException,
    CourseNotFoundException,
    ProfessorNotFoundException,
    CourseCapacityFullException,
    CourseAlreadySelectedException
)

#اضافه کردن دانشجو
def select_course_for_student(student_number, course_code):
    # دنبال دانشجو بگرد
    student = None
    for s in storage.students:
        if s["student_number"] == student_number:
            student = s
            break

    if student is None:
        raise StudentNotFoundException("دانشجو پیدا نشد")

    # دنبال درس بگرد
    course = None
    for c in storage.courses:
        if c["code"] == course_code:
            course = c
            break

    if course is None:
        raise CourseNotFoundException("درس پیدا نشد")

    # بررسی کن ظرفیت پر نباشه
    if len(course["students"]) >= course["capacity"]:
        raise CourseCapacityFullException("ظرفیت این درس پر شده است")

    # بررسی کن دانشجو این درس رو قبلاً انتخاب نکرده باشه
    if course_code in student["selected_courses"]:
        raise CourseAlreadySelectedException("این درس قبلاً توسط این دانشجو انتخاب شده است")

    # درس رو به لیست دانشجو اضافه کن
    student["selected_courses"].append(course_code)

    # دانشجو رو به لیست درس اضافه کن
    course["students"].append(student_number)

    save_all()
    return "درس با موفقیت انتخاب شد"

#حذف دانشجو
def drop_course_for_student(student_number, course_code):
    # دنبال دانشجو بگرد
    student = None
    for s in storage.students:
        if s["student_number"] == student_number:
            student = s
            break

    if student is None:
        raise StudentNotFoundException("دانشجو پیدا نشد")

    # دنبال درس بگرد
    course = None
    for c in storage.courses:
        if c["code"] == course_code:
            course = c
            break

    if course is None:
        raise CourseNotFoundException("درس پیدا نشد")

    # بررسی کن دانشجو این درس رو انتخاب کرده باشه
    if course_code not in student["selected_courses"]:
        raise CourseNotFoundException("این درس در لیست دروس دانشجو نیست")

    # درس رو از لیست دانشجو حذف کن
    student["selected_courses"].remove(course_code)

    # دانشجو رو از لیست درس حذف کن
    course["students"].remove(student_number)

    save_all()
    return "درس با موفقیت حذف شد"

#دروس یک دانشجو
def get_student_courses(student_number):
    # دنبال دانشجو بگرد
    for s in storage.students:
        if s["student_number"] == student_number:
            return s["selected_courses"]

    raise StudentNotFoundException("دانشجو پیدا نشد")

#تخصیص درس به استاد
def assign_professor_to_course(personnel_code, course_code):
    # دنبال استاد بگرد
    professor = None
    for p in storage.professors:
        if p["personnel_code"] == personnel_code:
            professor = p
            break

    if professor is None:
        raise ProfessorNotFoundException("استاد پیدا نشد")

    # دنبال درس بگرد
    course = None
    for c in storage.courses:
        if c["code"] == course_code:
            course = c
            break

    if course is None:
        raise CourseNotFoundException("درس پیدا نشد")

    # درس رو به استاد تخصیص بده
    course["professor"] = personnel_code
    professor["courses"].append(course_code)

    save_all()
    return "درس با موفقیت به استاد تخصیص داده شد"