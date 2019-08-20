# class Test:
#
#     # Cosntructor
#     def __init__(self, limit):
#         self.limit = limit
#
#         # Called when iteration is initialized
#
#     def __iter__(self):
#         self.x = 10
#         return self
#
#     # To move to next element. In Python 3,
#     # we should replace next with __next__
#     def __next__(self):
#         # Store current value ofx
#         a = self.x
#
#         # Stop iteration if limit is reached
#         if a > self.limit:
#             raise StopIteration
#
#             # Else increment and return old value
#         self.x = a + 1
#         return a

    # Prints numbers from 10 to 15

# t = Test(14)
# iter(t)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))

# for i in Test(15):
#     print(i)

# Prints nothing
# for i in Test(5):
#     print(i)


"---------------------------------------------------"

# class myfib:
#
#     # Cosntructor
#     def __init__(self, limit):
#         self.limit = limit
#
#
#         # Called when iteration is initialized
#
#     def __iter__(self):
#         self.a = 0
#         self.b = 1
#         self.count = 0
#         return self
#
#     # To move to next element. In Python 3,
#     # we should replace next with __next__
#     def __next__(self):
#         # Store current value of a,b
#         a = self.a
#         b = self.b
#         val = a
#
#         # Stop iteration if limit is reached
#         if self.count > self.limit:
#             raise StopIteration
#
#         # Else compute next value
#         self.count += 1
#         r = a + b
#         # modify existing values
#         self.a, self.b = b, r
#         return val
#
# for i in myfib(9):
#     print(i)