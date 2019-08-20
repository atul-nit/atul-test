# map, filter, reduce
# l1 = [2,3,4]
# l2 = []
# for ele in l1:
#     l2.append(ele*3)
# print(l2)

# #
# def mult3(x): return x*3
# # #
# l1 = [2,3,4]
# l2 = list(map(mult3, l1))
# print(l2)

# l1 = ['1', '35', '4']
# s = 0
# for ele in l1:
#     s += int(ele)
# print(s)

# l2 = map(int, l1)
# print(list(l2))
# s = list(map(int, input('enter numbers: ').strip(', ').split(",")))
# print(s)

# y = lambda x: x*3
# l1 = [2,3,4]
# l2 = list(map(y, l1))
# l3 = map(lambda x: x*3, l1)
# print(l2)
# print(list(l3))

# nums = list(range(1,11))
# odds = filter(lambda x: x%2!=0, nums)
# odds = filter(lambda x: x%2!=0, range(1,11))
# print(list(odds))

# def check_prime(n):
#     flag = 1
#     if n == 1 or n == 0:
#         flag = 0
#     else:
#         for i in range(2, n // 2 + 1):
#             if n % i == 0:
#                 flag = 0
#                 break
#     if flag:
#         return True
#     else:
#         return False
# #
# nums = [21,13,31,49,491,149]
# primes = filter(check_prime, nums)
# print(list(primes))



# reduce function
from functools import reduce
# l1 = [3,5,1,9]
# l2 = reduce(lambda x, y: x+y, l1)
# print(l2)
#
# f = reduce(lambda x,y: x*y, range(2,6))
# print(f)
# #
# # Writing our own reduce function
# def myreduce(fnc, seq):
#     t = seq[0]
#     for n in seq[1:]:
#         t = fnc(t, n)
#     return t
#
# r = myreduce(lambda x,y: x*y, range(2,6))
# print(r)

# n = 6
# f = 1
# i = n
# while i >  0:
#     f = f*i
#     i -= 1
# print(f)
