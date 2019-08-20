# a,b,c = 10,20,30
# print(a,b,c, sep="--") # 10--20--30

# print("hello", end=" ")
# print("there", end=" ")
# print("how are you?")

# a, b = '10', '3'
# print("the sum of", a , "and" , b, "is" , a+b)
# print("the sum of " + str(a) + " and " + str(b) + " is " + str(a+b))
# print("the sum of %d and %d is %d" %(a,b,a+b))
# print("the sum of {0} and {2} is {1}".format(a,b,a+b))
# print("the sum of {} and {} is {}".format(a,b,a+b))


# s = input("enter message: ")
# print(s)
# print(type(s))

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# print(a+b)

# Arithmetic Operators
# a, b = 10, 3
# print("a/b: ", a/b)
# print("a//b: ", a//b)
# print("a%b: ", a%b)
# print("a**b: ", a**b)

# n = 345
# to get the last digit
# ld = n % 10
# print("last digit: ", ld)

# remove last digit from integer
# n2 = n // 10
# print("n2: ", n2)

"""
a, b are two 4 digit numbers
a = 2367  => 3369
b = 9873  => 7872

la = a%10   => 7
lb = b%10   => 3
fa = a//1000  => 2
fb = b//1000  => 9

t1 = lb*1000 + (a%1000 - la + fb) => 3000 + (367 - 7 + 9)


"""

# logical and and or not
# print(4 or 5)
# print(4 and 5)
# print(not 6)

# Bitwise operator
# """
# 4 = 0000 0100
# 4>>2 = 0000 00 01
# 4<<2 = 0001 0000
#
# 4 = 100
# 1 = 001
# & = 000
# | = 101
# ^ = 101
# """
# print(4 & 1)
# print(4 | 1)
# print(4 ^ 1)
# print(~4)
# print(4>>2)
# print(4<<2)



# a = 5
# b = 14
# if a > b:
#     print("%d is greater than %d" %(a,b))
# else:
#     print("%d is not greater than %d" % (a, b))
# print("after if")


"""
if marks greater than 90 then grade A
if marks between 75 to 90 then grade B
if marks between 60 to 75 then grade C
else grade D
"""
# marks = int(input("enter marks: "))
# if marks > 90:
#     print("Grade A")
# elif marks > 75:
#     print("Grade B")
# elif marks > 65:
#     print("Grade C")
# else:
#     print("Grade D")

# name = input("Enter your name: ")
# city = input("Enter your city: ")
# age = int(input("Enter your age: "))
# if city == "berlin":
#     if age > 60:
#         print("Hello {} you are a senior citizen".format(name))
#     else:
#         print("Hello {} you can still work".format(name))
# else:
#     if age > 60:
#         print("Hello {} you are a senior citizen "
#               "but city does not match".format(name))
#     else:
#         print("go to work")

# num = int(input("Enter any number: "))
# if num % 3 == 0:
#     if num % 5 == 0:
#         print("%d is divisible by both 3 and 5" %num)
#     else:
#         print("%d is divisible by only 3" % num)
# else:
#     if num % 5 == 0:
#         print("%d is divisible by only 5" % num)
#     else:
#         print("%d is NOT divisible by both 3 and 5" % num)

# num = int(input("Enter any number: "))
# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd")
#
# if num&1:
#     print(num, "is odd")
# else:
#     print(num, "is even")

# print(num, "is odd") if num&1 else print(num, "is even")
# a,b,c = 4,11,17
# r = a if a>b else b
# print(r)

# r = (a if a>c else c) if a>b else (b if b>c else c)
# print(r)

# Taking multiple integer inputs

s = list(map(int, input("enters numbers comma separated: ").strip().split(",")))
print(s)