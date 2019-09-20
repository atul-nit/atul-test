# Check whether given number is prime or not
import time
from math import sqrt

# l1 = [12, 2, 35, 47, 67, 91]
def check_prime( num ):
    print(sqrt(num))
    is_prime = True
    for ele in range(2, int(sqrt(num))+1):
        if num%ele == 0:
            is_prime = False
            break
    return is_prime
#
num = int(input("enter any number: "))
# # start = time.time()
# start = time.time()
is_prime = check_prime(num)
if is_prime:
    print("{} is prime".format(num))
else:
    print("{} is not prime".format(num))
# end = time.time()
# print("execution time: {}".format(end-start))


# h = 1
# i = 0
# while i < 5:
#     h = h*2
#     h += 2
#     i += 1
#     print("after year {} height of plant is {}".format(i, h))
# print(h)

#