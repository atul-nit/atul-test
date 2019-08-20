# i = 1
# while i <= 10:
#     print(i)
#     i += 1  # i = i + 1
# print("while loop ended")
# print("i is %d" %i)

# infinite loop
# i = 1
# while i <= 10:
#     print(i)
# print("while loop ended")

# Using else with while
# n1 = int(input("enter even number: "))
# limit = 100
# while n1 <= limit:
#     print(n1)
#     n1 += 2
# else:
#     print(n1,"is greater than limit 100")

# while n1 <= limit:
#     print(n1)
#     n1 += 2
# else:
#     pass
# print("while loop ends")

# Use of infinite loop. Use of break and continue statements
# while True:
#     name = input("enter name: ")
#     print("hello "+name)
#     ch = input("do you wish to continue(y/n):")
#     if ch=='N' or ch=='n':
#         print("thank you!")
#         break
# print("after loop")

# i = 1
# while i <= 50:
#     if i%3==0 and i%5==0:
#         print(i)
#     i += 1

# i = 1
# while i <= 20:
#     if i%3 == 0:
#         if i%5 != 0:
#             print(i)
#     i += 1

# i = 1
# while i < 20:
#     a = i
#     i += 1
#     if a%4 == 0:
#         continue
#     if a%2 == 0:
#         print(a)
# print("after loop")

# i = 0
# while i < 2:
#     j = 1
#     while j <= 3:
#         if j == 2:
#             print(j**3)
#             break
#         print(j**2)
#         j += 1
#     i += 1

# Nested while loops with break condition
# i = 1
# while i <= 4:
#     j = 5
#     print("i is", i)
#     while j < 20:
#         if j%i == 0:
#             break
#         print (j)
#         j += 1
#     i += 1

# while 0:
#     print("hi")
# else:
#     print("hello")