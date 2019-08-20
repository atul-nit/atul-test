# append
# l1 = [1,3,5]
# print("before appending")
# print(l1)
# l1.append(10)
# print("after appending")
# print(l1)
# append list to a list
# l1.append([20,30])
# print(l1)
# print(l1[3])
# print(l1[3][1])

# m = [[10,1],[5,7]]
# print(m[0][0])
# print(m[1][1])
# print(m[1][0])
"""
"""


# extend
# aList = [123, 'xyz', 'zara', 'abc', 123]
# bList = [123, 2009, 'manni']
# aList.extend(bList)
# print ("Extended List : ", aList)

# index
# aList = [123, 'xyz', 'zara', 'abc', 'xyz']
# print ("Index for xyz : ", aList.index( 'xyz' ))
# print ("Index for zara : ", aList.index( 'zara' ))
# print ("Index for pappu : ", aList.index( 'pappu' )) # raise an exception

# insert
# aList = [123, 'xyz', 'zara', 'abc']
# aList.insert( 3, 2009)
# print ("Final List : ", aList)
# aList.insert(len(aList), "rrr")  # insert at the end, same like append
# print(aList)

# pop
# aList = [123, 'xyz', 'zara', 'abc']
# print ("removed element from List : ", aList.pop())
# print("list after pop: ", aList)
# print ("B List : ", aList.pop(1))
# print(aList)

# remove
# aList = [123, 'xyz', 'zara', 'abc', 'xyz']
# aList.remove('xyz')
# print ("List : ", aList)
# aList.remove('abc')
# print ("List : ", aList)

# reverse
# aList = [123, 'xyz', 'zara', 'abc', 'xyz']
# print(aList.reverse())
# print ("List : ", aList)

# sort
aList = ["123", 'xyz', 'zara', 'abc', '$', 'xyz']
# aList.sort()
# print ("List : ", aList)
# sort in descending order method 1
# aList.sort()
# aList.reverse()
# print(aList)
#
# # sort in descending order method 2
# aList.sort(reverse=True)
# print(aList)

# count
# l1 = [1,3,5,1,0,3,1]
# print("1 occurs %d times in list" %l1.count(1))
# print("3 occurs %d times in list" %l1.count(3))
# print("5 occurs %d time(s) in list" %l1.count(5))
# print("6 occurs %d times in list" %l1.count(6))

# list comprehension
# l1 = [1,3,4,5,10]
# r = []
# for ele in l1:
#     r.append(ele**2)
# print(r)
# #
# r1 = [ele**2 for ele in l1]
# print(r1)

# r = [ele**2 for ele in l1 if ele%2==0]
# print(r)

# r = [ele**2 if ele%2==0 else ele**3 for ele in l1]
# print(r)

# import operator
# fruits = ["orange", "apple", "guava"]
# calories = [100, 120, 450, 500]
# z = list(zip(fruits, calories))
# print(z)
# print(max(z))
# print(max(z, key=operator.itemgetter(1)))

# for f, c in zip(fruits, calories):
#     print("{} contains {} calories".format(f, c))




