import json
import os

# مسیر فایل ها
STUDENTS_FILE = "app/data/students.json"
PROFESSORS_FILE = "app/data/professors.json"
COURSES_FILE = "app/data/courses.json"

# شمارنده ها
student_id_counter = 1
professor_id_counter = 1
course_id_counter = 1

# لیست داده ها
students = []
professors = []
courses = []


def _read_json(path):
    if not os.path.exists(path):
        return []
    file = open(path, "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    return data


def _write_json(path, data):
    file = open(path, "w", encoding="utf-8")
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.close()


def save_all():
    _write_json(STUDENTS_FILE, students)
    _write_json(PROFESSORS_FILE, professors)
    _write_json(COURSES_FILE, courses)


def load_all():
    global students, professors, courses
    global student_id_counter, professor_id_counter, course_id_counter

    students = _read_json(STUDENTS_FILE)
    professors = _read_json(PROFESSORS_FILE)
    courses = _read_json(COURSES_FILE)

    # بالاترین ID موجود رو پیدا کن و یکی اضافه کن
    if students:
        student_id_counter = max(s["id"] for s in students) + 1
    else:
        student_id_counter = 1

    if professors:
        professor_id_counter = max(p["id"] for p in professors) + 1
    else:
        professor_id_counter = 1

    if courses:
        course_id_counter = max(c["id"] for c in courses) + 1
    else:
        course_id_counter = 1


def reset_storage():
    global students, professors, courses
    global student_id_counter, professor_id_counter, course_id_counter

    students = []
    professors = []
    courses = []

    student_id_counter = 1
    professor_id_counter = 1
    course_id_counter = 1

    save_all()