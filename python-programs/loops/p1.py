# l1 = [12,4,6,8]
# s = 0
# for i in l1:
#     s += i
# print("sum is %d" % s)


# l1 = [1,9,4,5,7,2,22]
# c_odd = 0
# c_even = 0
# for ele in l1:
#     if ele%2 == 0:
#         c_even += 1
#     else:
#         c_odd += 1
# print("odd count: %d" % c_odd)
# print("even count: %d" % c_even)


# s1 = "Hello there. How are you?"
# v = 'aeiou'
# count = 0
# new_arr = []
# for c in s1:
#     if c.lower() in v:
#         c = '*'
#         count += 1
#     new_arr.append(c)
#
# replaced_str = ''.join(new_arr)
# print(new_arr)
# print(replaced_str)
# print("vowel count: %d" % count)



def check_prime( num ):
    is_prime = 1  # value is one if number is prime
    for ele in range(2, num):
        if num%ele == 0:
            is_prime = 0
            break

    if is_prime:
        print("%d is prime" % num)
    else:
        print("%d is not prime" % num)


l1 = [12,15,43,97,141]
for ele in l1:
    check_prime( ele )

