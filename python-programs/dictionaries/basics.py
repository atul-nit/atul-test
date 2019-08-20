# creating a dictionary
d1 = {"name": "john", "salary": 2000, "age": 34}
# print(list(d1.items()))

"""
[("name", "john"), ("salary", 2000), ("age", 34)]
"""
# Accessing a dictionary
# print(d1["name"])
# print(d1["age"])
# print(d1.get("school", "NA"))
# print(d1)

# d2 = dict([("name","Peter"),("age",10)])
# print(d2)
# we get an error if we attemp to access a key not present

# updating a dictionary
# d1["age"] = 35
# d1["dept"] = "Management"
# print(d1)


# updating multiple keys
# print(d1)
# d2 = {"age":45, "dept":"sales", "salary":29099}
# d1.update(d2)
# print(d1)

# v = d1.setdefault("class", "high school")
# print(v)
# print(d1)

# remove dictionary elements
# del d1["age"]
# print(d1)
# d1.clear()
# print(d1)
# del d1
# print(d1)

# for k in d1:
#     print("{} : {}".format(k, d1[k]))

# for key, val in d1.items():
#     print("{} : {}".format(key, val))

# for t in d1.items():
#     print(t)

# key, val = ("name", "john")
# print(d1.items())
# print(d1.keys())
# print(d1.values())
# print("class" in d1)
# print("name" in d1)
# print(max(d1))
# print(max(d1.keys()))


s = {"name", "class", "age"}
# d3 = dict.fromkeys(s)
# print(d3)
# d3 = dict.fromkeys(s, 10)
# print(d3)

# s1 = ["orange", "apple", "banana"]
# s2 = [100, 150, 400]
# d3 = dict.fromkeys(s1, s2)
# print(d3)
# print(zip(s1,s2))
# d4 = dict(zip(s1,s2))
# print(d4)
# print(list(zip(s1,s2)))

# find key for maximum value
# import operator
# stats = {'a':1000, 'b':3000, 'c': 100}
# print(max(stats.items(), key=operator.itemgetter(1))[0])
#
# t1 = [(200,2), (400, 1), (500, 4), (600, 3)]
# print(max(t1))
# print(max(t1, key=operator.itemgetter(1))[0])
# t1 = [(200,2,12), (400, 1,151), (500, 4,20), (600, 3,11)]
# print(max(t1, key=operator.itemgetter(2)))

# print(d1.get("class", "NA"))
# print(d1.get("age"))
# print(d1.get("class"))

# Dictionary Comprehension
# keys = ['orange','apple','guava','watermelon']
# values = [100,120,200,90]
# d = {key:val+10 for (key,val) in zip(keys, values)}
# print(d)

# make dictionary using list comprehension
# l1 = [1,2,3,4]
# d3 = {"item"+str(i): i**2 for i in l1}
# print(d3)

# d2 = {"aa": 123, (1, 2): "hello"}
# print(d2)
#
# print(d2[(1,2)])