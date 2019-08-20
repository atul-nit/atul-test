# function without arguments
# def show_message():
#     print("this is message from show message")
# #
# show_message()

# function with arguments
def absolute_value(num):
    """This function returns the absolute
	value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num

# help(absolute_value)
# print(absolute_value.__doc__)
#
# Output: 2
# print(absolute_value(2))
# #
# Output: 4
# print(absolute_value(-4))

# function with multiple arguments
# def find_sum(num1, num2):
#     return num1+num2
# # #
# s = find_sum(5,9)
# print("sum is {}".format(s))

# def show(s1, s2="world"):
#     print(s1+s2)
#
# show("hello", "arjun")
# show("hello")
# show(s2="hi", s1="there")

# def show(s1="Hi", s2="world"):
#     print(s1,s2, end="\t", sep="----")
# #
# show("hello", "arjun")
# show("hello")
# show(s2="hhhh")  # positional parameter
# show()
# non-default parameters can't follow default parameters
"""following function is not valid
def show(s1="ddd", s2):
    print(s1+s2)"""

# def list_square(l2):
#     result = []
#     for ele in l2:
#         result.append(ele**2)
#
#     return result

# def modify_ele(l2):
#     l2.append(10)
#     return l2
# #
# l1 = [1,2,3,4,5]
# print(l1)
# print("after square:")
# print(list_square(l1))
# print(modify_ele(l1))
# print(modify_ele(l1[:]))
# print(l1)

# changes in l2 will reflect in l1 also
# def list_reverse(l2):
#     l2.reverse()
#     return l2
#
# l1 = [1,2,3,4,5]
# print("l1:   ",l1)
# print("reverse list:   ",list_reverse(l1))
# print("l1 after reverse call:     ",l1)


# to overcome above problem
# print("l1:   ",l1)
# print("reverse list:   ",list_reverse(l1[:]))
# print("l1 after reverse call:     ",l1)

# l1 = [1,2,3]
# l2 = l1
# l2[1] = 10
# print(l1) # [1,10,3]
# print(l2) # [1,10,3]