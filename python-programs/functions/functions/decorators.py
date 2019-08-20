# def myfun():
#     print("this is from myfun")
#
# myfun()
# newfun = myfun
# newfun()


# passing function as an argument
# def show(func1):
#     print(func1.__doc__)
#     func1()
# #
# def print_hello():
#     """it will print hello"""
#     print("message from print hello")
#
#
# show(print_hello)
# print(print_hello())
# print(print_hello.__doc__)
# print_hello()



# def inc(x):
#     return x + 1
#
# def dec(x):
#     return x - 1
#
# def operate(func, x):
#     result = func(x)  # dec(7)
#     return result
# #
#
# print(operate(inc, 3))
# print(operate(dec, 7))

# Returning a function from another function
# def ferrari( n ):
#     def inner_ferrari():
#         print("inner ferrari")
#         print(n*n)
#     return inner_ferrari

# a = ferrari(3)
# a()
# ferrari(3)()

# passing function as an argument
# def show(func1):
#     def new_func():
#         print("before print hello")
#         func1() # print_hello()
#         print("after print hello")
#     return new_func
# #
# #
# def print_hello():
#     """it will print hello"""
#     print("hello")
# #
# show(print_hello)()

# # decorators
def show(func1):
    def new_func():
        print("before print hello")
        func1()
        print("after print hello")
    return new_func

@show
def print_hello():
    """it will print hello"""
    print("hello")

print_hello()
# show(print_hello)()


# calculate the function execution time
# import
# #
# @exec_time_func
# def f2():
#     s = 0
#     for n in range(10, 20000):
#         s += n
#     print("sum is", s)
#
# f1()
# f2()

