# class A:
#     def __init__(self, fname, lname):
#         print("init AAAA")
#         self.first_name = fname
#         self.last_name = lname
#
#     def fullname(self):
#         return self.first_name + ' ' +self.last_name
#
# class B(A):
#     def __init__(self, fn, ln, sal):
#         print("init BBBB")
#         super().__init__(fn, ln) # A.__init__(fn ,ln)
#         self.salary = sal
#
#     def show_data(self):
#         return super().fullname() + ' ' + str(self.salary)

# class C(A):
#     def __init__(self, fn, ln, age):
#         super().__init__(fn, ln)
#         self.age = age


# b1 = B("Raj", "kapoor", 20000)
# print(b1.fullname())
# print(b1.show_data())



# class A:
#     def __init__(self, fname, lname):
#         print("init AAAA")
#         self.first_name = fname
#         self.last_name = lname
#
#     def fullname(self):
#         return self.first_name + ' ' +self.last_name
#
#     def show(self):
#         print("from show AAAA")
#
# class B(A):
#     def __init__(self, fn, ln, sal):
#         print("init BBBB")
#         super().__init__(fn, ln)
#         self.salary = sal
#
#     def show_data(self):
#         return super().fullname() + ' ' + str(self.salary)
#
#     def show(self):
#         print("from show BBBB")
#         super().show()
#
#
# b1 = B("Raj", "kapoor", 20000)
# # print(b1.show_data())
# b1.show()