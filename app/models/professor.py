from app.models.person import Person

#ساخت کلاس استاد که از کلاس پرسن ارث بری میکند
class Professor(Person):
    def __init__(self , id , first_name , last_name , personnel_code , department , courses = None):
        super().__init__(id , first_name , last_name)
        self.personnel_code = personnel_code
        self.department = department
        self.courses = courses if courses is not None else []

        #تخصیص درس به استاد
    def assign_course(self, course):
            if course not in self.courses:
                self.courses.append(course)

        #برگرداندن دروس ارائه شده استاد
    def get_courses(self):
            return self.courses

        #تبدیل ویژگی های شی به دیکشنری برای تبدیل به جیسون
    def to_dict(self):
            return {
                'id' : self.id,
                'first_name' : self.first_name,
                'last_name' : self.last_name,
                'personnel_code' : self.personnel_code,
                'department' : self.department,
                'courses' : self.courses
            }