#کلاس کورس برای اظلاعات درس
class Course:
    def __init__(self , course_id , title , code , unit , capacity , professor = None , students = None ):
        self.course_id = course_id
        self.title = title
        self.code = code
        self.unit = unit
        self.capacity = capacity
        self.professor = professor
        self.students = students if students is not None else []

        #بررسی پر یا خالی بودن ظرفیت به صورت بولین
    def is_full(self):
            return len(self.students) >= self.capacity

        #افزودن دانشجو به کلاس درس
    def add_students(self , student):
            if student not in self.students:
                self.students.append(student)

        #حذف دانشجو از کلاس درس
    def remove_students(self , student):
            if student in self.students:
                self.students.remove(student)

        #تخصیص استاد به درس
    def assign_professor(self , professor):
            self.professor = professor

        #تبدیل ویژگی های شی به دیکشنری برای ذخیره در جییسون
    def to_dict(self):
            return {
                'course_id' : self.course_id,
                'title' : self.title,
                'code' : self.code,
                'unit' : self.unit,
                'capacity' : self.capacity,
                'professor' : self.professor,
                'students' : self.students
            }