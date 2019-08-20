# find the length of a list
# l1 = [10,20,30,40,50]
# count = len(l1)
# print(count)

# find length of list without len function
# c = 0
# l1 = [10,20,30,40,50]
# for ele in l1:
#     c += 1
# print("list contains %d elements" %c)

# find sum of 1-Dimensional list using sum function
# l1 = [10,20,30,40,50]
# s = sum(l1)
# print("{} is {} ".format('sum', s))

# find sum of 1-Dimensional list without sum function
# s = 0
# l1 = [10,20,30,40,50]
# for ele in l1:
#     s += ele
# print("{} is {} ".format('sum', s))

# find max element from a list
# l1 = [10,20,30,40,50]
# print("max element is", max(l1))

# find max element without max function
# l1 = [10,20,100,30,95]
# m = l1[0]
# for e in l1:
#     if e > m:
#         m = e
# print("max element is {}".format(m))

# find min element from a list
# l1 = [10,20,30,40,50]
# print("min element is", min(l1))

# concatenate lists
# l1 = [2,5,7]
# l2 = [8,9,10]
# l3 = l1+l2
# print("l1: ",l1)
# print("l2: ",l2)
# print("l3: ",l3)

# repitition of list
# create a list of 10 elements with all elements as 0
# l1 = [0]*10
# print(l1)
# print(len(l1))

#repeat list with more than 1 element
# l1 = [1,3,5]
# print(l1*3)

# look for an element in the list
# l1 = [10,20,30,40,50]
# print(40 in l1)
# print(60 in l1)
# print(60 not in l1)
# n = int(input("enter num to search: "))
# if n in l1:
#     print("%d found in the list" %n)
# else:
#     print("%d not found in the list" % n)

#slicing operator in list
# l1 = [10,20,30,40,50,60]
# print(l1[0:5])  # elements from 0 to 4 index
# print(l1[:5])   # elemnts from 0 to 4 index
# print(l1[1:5])    # elements from 1 to 4 index
# print(l1[1:])   # elements from 1 to last index
# print(l1[0:5:1]) # same as above step is 1
# print(l1[0:5:2]) # values at indexes 0,2,4
# print(l1[0:4:2]) # values at indexes 0,2
# print(l1[5:1:-1])  # values at indexes 5 to 2
# print(l1[5:1])      # empty list
# print(l1[::-1])  # gives reverse of the list
# print(l1[:5:2])  # elements at 0,2,4 indexes
# print(l1[-1:-5:-1]) # elements from 5 to 2 index l1[5:1:-1]
# print(l1[-1:-5])    # empty list
# print(l1[-5:-2])
# print(l1[1::2])
# print(l1[5:0:-1])

# str1 = "abba"
# if str1 == str1[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

