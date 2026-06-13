from app.models.person import Person

#کلاس دانشجو که از کلاس پایه پرسن ارث بری میکنه
class Student(Person):
    def __init__(self, id, first_name, last_name, student_number , major , selected_courses = None):
        super().__init__(id, first_name, last_name)
        self.student_number = student_number
        self.major = major
        self.selected_courses = selected_courses if selected_courses is not None else []

        # انتخاب درس توسط دانشجو
    def select_course(self , course):
            if course not in self.selected_courses:
                self.selected_courses.append(course)

        # حذف درس توسط دانشجو
    def drop_course(self , course):
            if course in self.selected_courses:
                self.selected_courses.remove(course)

        # برگرداندن دروس اخذ شده
    def get_courses(self):
            return self.selected_courses

        #تبدیل ویژگی های شی به دیکشنری برای ذخیره در جیسون
    def to_dict(self):
            return {
                'id' : self.id,
                'first_name' : self.first_name,
                'last_name' : self.last_name,
                'student_number' : self.student_number,
                'major' : self.major,
                'selected_courses' : self.selected_courses

            }