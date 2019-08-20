"""to find the prime numbers between 1 and 100"""
import math
# num = int(input("Enter the number till which you want prime numbers: "))
# l1 = list(range(2,num))
# print(l1)
#
# print("The prime numbers are ")
# for ele1 in l1:
#     c = 0
#     l2 = list(range(1, ele1 + 1))
#     for ele2 in l2:
#         if(ele2 <= ele1):
#             if(ele1 % ele2 == 0):
#                 c += 1
#     if(c == 2):
#         print(ele1)



# n = int(input("enter number: "))
# is_prime = 1
# c = 0
# for i in range(2, int(math.sqrt(n)) + 1):
#     c += 1
#     if n%i == 0:
#         is_prime = 0
#         break
#
# if is_prime:
#     print("%d is prime" %n)
# else:
#     print("%d is not prime" %n)
# print("loops: %d" %c)


def check_prime(n):
    is_prime = 1
    c = 0
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        c += 1
        if n % i == 0:
            is_prime = 0
            break
    if is_prime:
        return True
    else:
        return False



prime_counter = 0
for i in range(1,101):
    is_prime = check_prime(i)
    if is_prime:
        print("%d is prime" % i)
        prime_counter += 1
    else:
        print("%d is not prime" % i)
print("prime number count: %d" % prime_counter)



