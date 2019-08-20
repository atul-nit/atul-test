# def show(num):
#     if num == 0:
#         return 1
#     return 2 * show(num - 1)
# #
# r = show(5)
# print(r)
#
# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * fact(num-1)
#
# print(fact(5))

"""
2 * show(4) => 2 * 16 = 32
2 * show(3) => 2 * 8 = 16
2 * show(2) => 2 * 4 = 8
2 * show(1) => 2 * 2 = 4
2 * show(0) => 2 * 1 = 2


"""

# Print all characters one by one using recursion
def print_char(s):
    if len(s) != 0:
        print(s[0])
        print_char(s[1:])
    else:
        return


s = "hello"
# print_char(s)
#
# """output:
# h
# e
# l
# l
# o
# """




