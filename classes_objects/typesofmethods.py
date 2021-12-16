class Student:
    school = "abc"
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("static method")
    
s1 = Student(24,12,44)
s2 = Student(34,59,38)

print(s1.avg())
print(Student.getSchool())
Student.info()
print(s2.avg())
