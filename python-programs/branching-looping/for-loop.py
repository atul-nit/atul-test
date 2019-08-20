# For loop to print all elements in a list
# l1 = [2,4,6,8,10]
# for ele in l1:
#     print(ele)

# Print square of each element in a list
# l1 = [2,4,6,8,10]
# for ele in l1:
#     print(ele*ele, ele**2)

# Find odd and even numbers in a list
# values = [5,7,24,13,56,14,97]
# odd_count = 0
# even_count = 0
# for val in values:
#     if val%2 == 0:
#         print(val,"is even")
#         even_count += 1
#     else:
#         print(val,"is odd")
#         odd_count += 1
# print("there are",odd_count,"odd numbers")
# print("there are",even_count,"even numbers")

# Find the sum of numbers from 10 to 20
# s = 0
# for n in range(10,21):
#     s += n
# print("sum is",s)

# Find sum of all multilples of 7 starting from 14 to 77
# s = 0
# for ele in range(14,78,7):
#     s += ele
# print(s)

# for loop with else
# for i in range(5):
#     print(i)
# else:
#     print("else part")
# print("for ended")

# for i in []:
#     print(i)
# else:
#     print("else part")

# for i in range(0):
#     print(i)
# else:
#     print("else part")

# for i in (3,7):
#     print(i)
# else:
#     print("else part")

# use of break and continue
"""print squares of numbers from 1 to 20. Continue of the number is multiple of 5, break if multiple of 13"""
# for ele in range(1,20):
#     if ele%13 == 0:
#         print("multiple of 13, breaking the loop")
#         break
#     if ele%5 == 0:
#         print(ele,"is multiple of 5, continuing the loop")
#         continue
#     print(ele*ele)


# Find factorial of a number n
# n = int(input("enter any positive integer: "))
# f = 1
"""use this"""
# for i in range(2,n+1):
#     f *= i
# """OR this"""
# for i in range(n,1,-1):
#     f *= i
# print(f)



# i = 4
# k = 0
# while i >= 0:
#     j = 0
#     while j < i:
#         print("_", end='')
#         j += 1
#     v = 0
#
#     while v <= k:
#         print("*", end='')
#         v += 1
#     print()
#     i -= 1
#     k += 2
# i = 4
# k =0
# while i-1 >= 0:
#     v = 0
#     while v <= k:
#         print("_", end='')
#         v += 1
#     k += 1
#     j = i
#     while j >= 0:
#         print("*", end='')
#         j -= 1
#     print()
#     i -= 1


# l1 = [1,2,3,4,5]
# l2 = [1,4,9,16,25]
# print(list(zip(l1,l2)))
# print()
# for e1,e2 in zip(l1,l2):
#     print("{} + {} = {}".format(e1,e2,e1+e2))