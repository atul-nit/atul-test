# Given a string, find its first non-repeating character

"""
Algorithm:
1) Scan the string from left to right and construct the count array.
2) Again, scan the string from left to right and check for count of each
 character, if you find an element who's count is 1, return it.
"""
NO_OF_CHARS = 256

def charCountArray(str1):
    count = [0] * 256
    for c in str1:
        count[ord(c)] += 1
    return count

def firstNonRepeatingChar(str1):
    count = charCountArray(str1)
    index = -1
    k = 0
    for c in str1:
        if count[ord(c)] == 1:
            index = k
            break
        k += 1
    return index

s = input("Enter any string: ")
index = firstNonRepeatingChar(s)
if index == -1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is : " + s[index])

