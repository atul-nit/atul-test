class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def showEmployeeCount(self):
        print("total employees: {}".format(Employee.empCount))

    def showEmployee(self):
        print("name: {}  salary: {}".format(self.name, self.salary))

class Student:
    pass

e1 = Employee("john", 20000)
# e1.showEmployeeCount()
e2 = Employee("Peter", 10000)
print(e1.empCount)
# e1.showEmployeeCount()
# e1.showEmployee()
# e2.showEmployee()

s1 = Student()


# print(isinstance(e1, Employee))
# print(isinstance(e1, Student))

# get class atributes from class
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee)



# get class name using object
# print(type(e1))
# print(e1.__class__.__name__)
# print(e1.__class__.empCount)



"""
Employee:
empCount = 2
"""

"""
name = john
salary = 20000

"""
