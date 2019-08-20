# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length - 1,-1,-1):
#         yield my_str[i]
#
#
# for ch in rev_str("hello"):
#     print(ch)

# length = 5
# l = range(length - 1,-1,-1)
# print(list(l))

# def multiples(num, limit):
#     i = 1
#     while i <= limit:
#         yield num * i
#         i += 1
#
# for e in multiples(3, 10):
#     print(e)


# def fibonacci(limit):
#     a = 0
#     b = 1
#     for i in range(limit):
#         yield a
#         r = a + b
#         a = b
#         b = r
#
#
# for e in fibonacci(10):
#     print(e)