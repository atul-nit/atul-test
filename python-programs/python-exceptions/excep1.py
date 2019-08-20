import sys
import logging


# n = int(input("enter any number: "))
# print("result is: {}".format(10/n))
# print("after operation")


# try:
#     n = int(input("enter divisor: "))
#     num = 10
#     r = num/n
#     print(r)
# except:
#     print("some exception")
# print("after try-except block")


# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename='debug.log', filemode='a', level=logging.WARNING, format='%(name)s - %(levelname)s - %(message)s')
# logging.info('This will get logged to a file')

# nums = [2,0,'a',4]
# n = 5
# for ele in nums:
#     print(n/ele)

# it will handle exception for loop and come out and will not iterate further
# nums = [2,0,'a', 4]
# a = 5
# try:
#     for ele in nums:
#         print(a/ele)
# except:
#     print("division by {} not possible".format(ele))
# print("after exception")

# nums = [2,0,'a', 4]
# a = 5
# for ele in nums:
#     try:
#         print(a/ele)
#     except:
#         print("division by {} not possible".format(ele))
        # logging.info("division by {} not possible".format(ele))
        # logging.warning("some warning")
        # print(sys.exc_info())
# print("after exception")

# a,b = 12,0
# print(a/b)  # The program will halt. Not handling exception
# print("after ------") # This message not printed
#
# try:
#     print(a/b)
# except:
#     print("from ecxept")
# print("last message")  # This message will be printed

# try:
#     print(5/0)
# except:
#     print("some exception occurred")
#     print(sys.exc_info()[1])
# print("after exception")

# Handling with Exception class
# try:
#     print(5/0)
# except Exception as e:
#     print("some exception {}".format(str(e)))
#     print(type(e))
#     print(e.__class__)

# try:
#     # print(5/0)
#     # print(a/3)
#     l1 = [2,4]
#     print(l1[2])
# except ZeroDivisionError:
#     print("division by zero occurred")
# except NameError:
#     print("some undefined name occurred")
# except Exception as e:
#     print("some exception occurred")
#     print(str(e))
# print("after exception")

# The order of the exception matters
# try:
#     print(5/0)
#     # print(a/3)
#     # l1 = [2,4]
#     # print(l1[2])
# except Exception as e:
#     print("some exception occurred")
#     print(str(e))
# except ZeroDivisionError:
#     print("division by zero occurred")
# except NameError:
#     print("some undefined name occurred")
#
# print("after exception")

# raising own exceptions
# try:
#    height = float(input("enter height in metres: "))
#    mass = float(input("enter weight in kg: "))
#    if height <= 0 or mass <= 0:
#        # raise Exception("please enter values greater than 0")
#        raise NameError("please enter values greater than 0")
#    bmi = mass/(height**2)
#    print("your BMI is {}".format(bmi))
# except NameError as e:
#     print("from name error")
#     print(e)
# except Exception as e:
#     print(e)
# print("after exception")

# Use of finally
# try:
#     print(5/10)
#     print(5/0)
# except:
#     print("some exception")
# finally:
#     print("from finally")

# try:
#     n = int(input("enter any number: "))
#     print(10/n)
#     print("aa ")
# except:
#     print("some exception")
# finally:
#     print("finally block message")
#
# try with only finally without except
# try:
#     n = int(input("enter any number: "))
#     print(10/n)
# finally:
#     print("finally block message")


