""""""
"""
String leterals are either surrounded by single or double quotes.
strings in Python are arrays of bytes representing unicode characters
"""
"""Accessing a string"""
s = "Hello World"
# print(s[1])   # gets value at index 1

# for i in s:
#     print(i)

"""Get substring from position 2 to 5"""
# b = "Hello, World!"
# print(b[2:5])   # llo

"""Remove whitespace from the begining or the end"""
# a = " Hello, World! "
# a = "'',,, this is me,,.. n n n   "
# a = "  ,,, this is me,,..   "
# print(a)
# print(len(a))
# b = a.strip()
# b = a.strip(' ')
# b = a.strip(' n.')
# b = a.strip(' ,')
# b = a.strip(' ,.')
# b = a.strip("'")
# print(b) # returns "Hello, World!"
# print(len(b))

"""Get length of the string"""
# a = "Hello, World!"
# print(len(a))

# s1 = "this is my home"
# parts = s1.split()
# print(parts)

# str1 = '12,34,78'
# nums = str1.split(",")
# print(nums)
# b = []
# for i in nums:
#     b.append(int(i))
# print(b)

# b = list(map(int, nums))
# print(b)

# take multiple int inputs
# nums = list(map(int, input("enter [numbers comma separated: ").strip().split(",")))
# print(nums)