#کلاس پایه پرسن
class Person:
    def __init__(self , id , first_name , last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    #برگرداندن نام کامل
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    #ویژگی های شی در دیکشنری برای ذخیره در جیسون
    def to_dict(self):
        return {
            "id" : self.id,
            "first_name" : self.first_name,
            "last_name" : self.last_name
        }