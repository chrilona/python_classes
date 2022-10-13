


class Student:
    school="Akirachix"
    
    def __init__(self,f_name,l_name,current_year,age):
        self.f_name=f_name
        self.l_name=l_name
        self.current_year=current_year
        self.age=age

    def full_name(self):
        return f"Hello {self.f_name} {self.l_name} is your full name"

    def initials(self):
        return f"Your initials are {self.f_name[0]} {self.l_name[0]}"

    def y_o_b(self):
        y_o_b=self.current_year-self.age
        return f" You were born in {y_o_b}"
# On the terminal
#from student import Student
#  >>> student=Student("Mollen","Wambui",2022,21)
# >>> student.full_name()
# 'Hello Mollen Wambui is your full name'
# >>> student.initials()
# 'Your initials are M W'  




      