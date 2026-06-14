#کلاس پایه دوره
class Course:
    def __init__(self, course_id, title, code, unit, capacity, major, professor=None, students=None):
        self.course_id = course_id
        self.title = title
        self.code = code
        self.unit = unit
        self.capacity = capacity
        self.major = major
        self.professor = professor
        self.students = students if students is not None else []
#چک کردن ظرفیت
    def is_full(self):
        return len(self.students) >= self.capacity
#اضافه کردن دانشجو جدید
    def add_students(self, student):
        if student not in self.students:
            self.students.append(student)
#حذف دانشجو
    def remove_students(self, student):
        if student in self.students:
            self.students.remove(student)
#تخصیص دوره به استاد
    def assign_professor(self, professor):
        self.professor = professor
#ذخیره اطلاعات دوره به صورت دیکشنری برای ذخیره در جیسون
    def to_dict(self):
        return {
            'course_id': self.course_id,
            'title': self.title,
            'code': self.code,
            'unit': self.unit,
            'capacity': self.capacity,
            'major': self.major,
            'professor': self.professor,
            'students': self.students
        }