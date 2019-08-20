import json

# x =  '{ "name":"John", "age":30, "city":"New York"}'
# print(type(x))
# print(x)
# y = json.loads(x)
# print(type(y))
# print(y)

json_str = '''{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}'''
#
# d1 = json.loads(json_str)
# for item in d1.items():
#     print (item)
# children = d1['children']
# for child in children:
#     print(child)

# x = '[{"oranges":10, "apples":20, "bananas":30},{"oranges":50, "apples":60, "bananas":100}]'
# y = json.loads(x)
# print(type(y))
# print(y)
# for ele in y:
#     print(type(ele))
#     print(ele)




# loading json from a file
with open('sample-json1.json', 'r') as fr:
    d1 = json.load(fr)
    print(d1)
