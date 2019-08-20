class A:
    def __init__(self, firstname, lastname, s):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = s


    def show_data(self):
        return "name: {}  salary: {}".format(self.fullname(), self.salary)
        # print("name: {}  salary: {}".format(self.name, self.salary))

    # @property
    def fullname(self):
        return self.firstname + " " + self.lastname

a1 = A("John", "Cena", 20000)
a2 = A("Peter", "Makkin", 21000)
# print(a1.firstname)
# print(a2.firstname)
# a1.age = 39
# print(a1.__dict__)
# print(a2.__dict__)
# del a1.age
# print(a1.__dict__)
# print(a1.show_data())
# a1.firstname = "Rock"
# print(a1.__dict__)
# print(a2.show_data())
# # a2.show_data()


# print(a1.salary)
# del a1.salary
# print(a1.__dict__)

# """
# mem = "ADF3343"
# __init__(mem, "john", 200000)
# """

"""
a1: 

firstname = john
lastname = Cena
salary = 20000
"""

"""
a2:

firstname = Peter
lastname = Makkin
salary = 21000
"""