# def show():
#     print("from show message")
# #
# show()
# hello = show
# hello()

# def find_sum(a, b):
#     "returns sum of two numbers"
#     return a+b

# print(show.__doc__)
# print(find_sum.__doc__)
# print(str.split.__doc__)
#
# def get_abs_val(n):
#     if n < 0:
#         return -n
#     else:
#         return n

# r = find_sum(4,6)
# print(r)
# print(r**2)
# print(find_sum(4,6))
# print(find_sum(get_abs_val(-4),6))
# print(get_abs_val(-7))

# print(show())


# def show(s1, s2="world"):
#     return s1 + " " + s2

# print(show("hello", "there"))
# print(show("hello"))
# print(show(s2="hi", s1="hello"))

# def show_msg(msg):
#     print_hello()
#     print(msg)
#
# def print_hello():
#     print("it will print hello")
# #
# show_msg("some message")
# print("after show message")

# def inc(n):
#     return n + 1
#
#
# def dec( n ):
#     return n - 1
#
#
# def operation(func, x):
#     r = func(x)  # dec(9)
#     return r
#
# print(operation(inc, 5))
# print(operation(dec, 9))

# def get_message(func, n):
#     def new_func():
#         print("before show func")
#         func(n) # show(3)
#         print("after show func")
#     return new_func
#
# def show(n):
#     print("this is show message")
#     print(n*5)
#
#
# r = get_message(show, 3)
# r()


# def get_message(func):
#     def new_func(n):
#         print("before {}".format(func.__doc__))
#         func(n)
#         print("after {}".format(func.__doc__))
#     return new_func
#
# @get_message   # get_message(show)(6)
# def show(n):
#     "show function"
#     print("this is show message")
#     print(n*5)
#
#
# @get_message
# def print_hello(msg):
#     "print hello function"
#     print("hello {}".format(msg))
#
#
# show(6)
# print_hello("this")


# a = "hello"
# b = "there"
# c = 5
# d = 3
# # print(a+" "+b+" how are you?")
# # print("%s %s how are you?" %(a,b))
#
# print("sum of {} and {} is {}".format("5",d, c+d))

