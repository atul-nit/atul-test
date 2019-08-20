""""""
"""capitalize()   Capitalizes first letter of string"""
# str1 = "this is strinG example....wOw!!!"
# print ("str.capitalize() : ", str1.capitalize())
""""----------------------------------------------------------------------------------------"""

"""
center(width[, fillchar]))  Returns a string padded with fillchar with 
the original string centered to a total of width columns.
"""
# str2 = "this is string example....wow!!!!"
# str1 = "My Profile"
# print(len(str2))
# print ("str2.center(40, 'a') : ", str2.center(40, 'a'))
# print ("str2.center(30, 'a') : ", str2.center(30, 'a'))
# print ("str1.center(40, 'a') : ", str1.center(40, '-'))
"""---------------------------------------------------------------------------------------------"""


"""
str.count(sub, start = 0,end = len(string))
returns the number of occurrences of substring sub in the range [start, end] 
"""
# str1 = "this is string example....wow!!!"
# sub = 'i'
# print ("str1.count('i') : ", str1.count('i'))
# print ("str.count('i',10,40) : ", str1.count(sub,10,40))
# sub = 'exam'
# print ("str1.count('exam', 10, 40) : ", str1.count(sub,10,40))
# sub = 'is'
# print ("str1.count('is',10,40) : ", str1.count(sub,10,40))
# print ("str1.count('is',0,10) : ", str1.count(sub,0,10))
"""------------------------------------------------------------------------------------------------"""


"""
Str.decode(encoding = 'UTF-8',errors = 'strict')
decodes the string using the codec registered for encoding.
It defaults to the default string encoding
"""
# Str = "this is string example....wow!!!"
# Str = Str.encode('base64','strict')
# print ("Encoded String: " + Str)
# print ("Decoded String: " + Str.decode('base64','strict'))
"""---------------------------------------------------------------------------------------------------"""


"""
str.encode(encoding = 'UTF-8',errors = 'strict')
returns an encoded version of the string
"""
# import base64
# #
# Str1 = "this is string example....wow!!!"
# Str = base64.b64encode(Str1.encode('utf-8',errors = 'strict'))
# print ("Encoded String: " , Str)
# print(base64.b64decode(Str))
# a = Str1.encode('utf-8',errors = 'strict')
# print(a)
"""-----------------------------------------------------------------------------------------------------"""


"""str.endswith(suffix[, start[, end]])"""
# str1 = 'this is string example....wow!!!'
# suffix = '!!'
# print (str1.endswith(suffix))
# print (str1.endswith(suffix,20))
suffix = 'exam'
# print (str1.endswith(suffix))
# print (str1.endswith(suffix, 0, 19))

"""-------------------------------------------------------------------------------------------------------"""


"""str.startswith(str, beg = 0,end = len(string));"""
# str = "this is string example....wow!!!"
# print (str.startswith( 'this' ))
# print (str.startswith( 'string', 8 ))
# print (str.startswith( 'this', 2, 4 ))
"""--------------------------------------------------------------------------------------------------------"""


# """str.find(str, beg = 0 end = len(string)) if string str occurs in a string"""
# str1 = "this is string example....wow!!!"
# str2 = "exam"
# print (str1.find(str2))
# print (str1.find(str2, 10,20))
# print (str1.find(str2, 40))
"""--------------------------------------------------------------------------------------------------------"""


"""str.index(str, beg = 0 end = len(string)) if the string str occurs in string but raise exception if not found"""
# str1 = "this is string example....wow!!!"
# str2 = "exam"
# print (str1.index(str2))
# print (str1.index(str2, 10))
# print (str1.index(str2, 40))
"""---------------------------------------------------------------------------------------------------------"""


"""str.isa1num() checks atr is alphanumeric"""
# str1 = "this2016"  # No space in this string
# print (str1.isalnum())
# str1 = "this is string example....wow!!!"
# print (str1.isalnum())
# str1 = "this is me 1900"
# print(str1.isalnum())
"""---------------------------------------------------------------------------------------------------------"""


"""str.isalpha()  checks whether the string consists of alphabetic characters only"""
# str = "this1"  # No space & digit in this string
# print (str.isalpha())
# str2 = "this is string example....wow!!!"
# print (str2.isalpha())
"""----------------------------------------------------------------------------------------------------------"""


"""str.isdigit()  checks whether the string consists of digits only"""
# str = "123456"  # Only digit in this string
# print (str.isdigit())
# str = "this is string example....wow!!!"
# print (str.isdigit())
"""------------------------------------------------------------------------------------------------------------"""


"""str.islower()   checks whether all the case-based characters (letters) of the string are lowercase"""
# str = "THIS is string example....wow!!!"
# print (str.islower())
# str = "this is string example....wow!!!"
# print (str.islower())
"""------------------------------------------------------------------------------------------------------------"""


"""str.isupper()   checks whether all the case-based characters (letters) of the string are uppercase"""
# str = "THIS IS STRING EXAMPLE....WOW!!!"
# print (str.isupper())
# str = "THIS is string example....wow!!!"
# print (str.isupper())
"""------------------------------------------------------------------------------------------------------------"""


"""str.isnumeric()  checks whether the string consists of only numeric characters"""
# str = "this2016"
# print (str.isnumeric())
# str = "234434348"
# print (str.isnumeric())
"""------------------------------------------------------------------------------------------------------------"""


"""str.isspace()  checks whether the string consists of whitespace"""
# str = "       "
# print (str.isspace())
# str = "This is string example....wow!!!"
# print (str.isspace())
# print ("".isspace())
"""--------------------------------------------------------------------------------------------------------------"""


"""
str.istitle()  
checks whether all the case-based characters in the string following non-casebased letters 
are uppercase and all other case-based characters are lowercase
"""
# str1 = "This Is Sring Example...Wow!!!"
# print (str1.istitle())
# str1 = "This is string example....wow!!!"
# print (str1.istitle())

"""-------------------------------------------------------------------------------------------------------------"""


# """str.join(sequence)  returns a string in which the string elements of sequence have been joined by str separator"""
# s = "-"
# seq = ("a", "b", "c") # This is sequence of strings.
# seq1 = ("This", "is", "my", "home") # This is sequence of strings.
# print (s.join( seq ))
# print(" ".join(seq1))
"""------------------------------------------------------------------------------------------------------------"""


"""str.lower() convert all characters to lowercase"""
# str = "THIS IS STRING EXAMPLE....WOW!!!"
# print (str.lower())
"""-------------------------------------------------------------------------------------------------------------"""


"""max(str)  returns max alphabetical character"""
# str = "this is a string example....really!!!"
# print ("Max character: " + max(str))
# str = "this is a string example....wow!!!"
# print ("Max character: " + max(str))
"""-------------------------------------------------------------------------------------------------------------"""


"""min(str)  returns min alphabetical character"""
# str = "www.google.com^!"
# print ("Min character: " + min(str))
"""-------------------------------------------------------------------------------------------------------------"""


# """str.replace(old, new[, max])  replace old coccurrence with new optionally restricted with max replacements"""
# str1 = "this is string example....wow!!! this is really string"
# print (str1.replace("is", "was"))
# print (str1.replace("is", "was", 3))
"""-------------------------------------------------------------------------------------------------------------"""


"""str.split(str="", num = string.count(str)) splits using separator and return list"""
# str1 = "this is string example....wow!!!"
# print (str1.split( ))
# print (str1.split('i', 2))
# print (str1.split('i'))
"""------------------------------------------------------------------------------------------------------------"""


"""str.upper()  converts all alphabets to uppercase"""
# str = "this is string example....wow!!!"
# print ("str.upper : ",str.upper())
"""-----------------------------------------------------------------------------------------------------------"""


l1 = [1,2,3]
l2 = [ele**2 if ele%2==0 else ele**3 for ele in l1]
print(l2)
l3 = [ele**2 if ele%2==0 else ele**3 for ele in l1]