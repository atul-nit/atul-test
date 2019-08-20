import re


txt = "The rain in Spain"
# txt = """
# This is me.
# The rain in Spain
# The weather is very good in Spain
# """
x = re.search("^The.*Spain$", txt, re.M)
# print(x)
# # print(x.string)
# if (x):
#   print("YES! We have a match!")
#   print(x.string)
# else:
#   print("No match")

# line = 'cats are smarter than dogs'
# pat = r'(.*) are (.*) .*'
# # # #
# matchObj = re.match(pat, line, re.M|re.I)
# # # #
# if matchObj:
#     print("matchObj group(): ", matchObj.group())
#     print("matchObj group(1): ", matchObj.group(1))
#     print("matchObj group(2): ", matchObj.group(2))
#     print("matchObj groups(): ", matchObj.groups())
# else:
#     print("no match!!")
"""-------------------------------------------------"""
# line = 'A cat and rat cannot be friends. kkr_123'
# x = re.search('cat', line)
# y = re.search(r'[a-z]+_[0-9]+', line)
# z = re.search('pill', line)
# print(x)
# print(y)
# print(z)

"""-------------------------------------------------------"""
# pat = r"M[ae][iy]er"
# line = "He is a German called Meyer"
# if re.search(pat, line):
#     print("name found")
# else:
#     print("name not found")

"""
Mayer
Maier
Meyer
Meier
"""
"""---------------------------------------------"""
# Find all occurrences of any pattern
# s1 = """
# John is 20 years old, Daniel is 15 years old.
# Their father is 46 years old and their grandfather is 80
# years old.
# """
# ages = re.findall(r'\d+', s1)
# print(ages)
# #
# get all spaces in the line
# spaces = re.findall(r" ", s1)
# print(len(spaces))
#
# get all the words in a string
# words = re.findall(r"\w+", s1)
# print(words)
# print(len(words))
# r = re.findall(r"\w+ther\b", s1)
# print(r)

"""------------------------------"""
# Splitting with regex
# s1 = """
# John is 20 years old, Daniel is 15 years old.
# Their father is 46 years old and their grandfather is 80
# years old.
# """
#
# s2 = "John is 20 and Daniel is 30"
# l1 = re.split(r"\d+", s1)
# print(l1)
#split
# l1 = re.split(r"\d+", s2)
# print(l1)

s2 = """
[sections:A]
name=101
[sections:B]
var1=123
var2=hello
"""
# r = re.sub(r"\[sections", "[headers", s2)
# r = re.sub(r"\[.+\]", "[headers]", s2)
# print(r)

pat1 = r'\[.+\]'
result = re.findall(pat1, s2)
print(result)

