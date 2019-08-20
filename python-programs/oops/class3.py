class Student:
    active_student = 0
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        Student.active_student += 1

    def show(self):
        print("name: {}  roll: {}".format(self.name, self.roll))

    @classmethod
    def myfun(cls, p, ob):
        print(cls)
        print("myfun",p)
        print("name: {}".format(ob.name))


s1 = Student("Atul", 12)
s2 = Student("Raj", 120)
# print(s1.active_student)
# print(Student.active_student)
Student.myfun(56, s1)
Student.myfun(56, s2)

