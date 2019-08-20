import json
import os
import re


# def get_json_data(content):
#     if "JSON" in content:
#         # print(content)
#         parts = content.split("=")
#         json_string = parts[1]
#         print(json_string)
#         d = json.loads(json_string)
#         print(d)



def add_product_to_config():
    prod = input("enter product: ")
    print(prod)
    pat1 = r'\[section:service\]\n'
    result = get_part(pat1)
    print(result)
    section_json = result.split("=")[1]
    print(section_json)
    section_dict = json.loads(section_json)
    print(section_dict)
    section_dict['products'].append(prod)
    print(section_dict)




current_dir = os.path.dirname(__file__)
# print(current_dir)
p = os.path.join(current_dir, 'my1.config')
# print(p)

def get_part(pat1):
    with open(p, 'r') as f:
        content = f.read()
        # print(content)
        # pat1 = r'\[section:service\]\n'
        pat2 = r'\[section:.*\]\n'
        part = re.split(pat1, content)[1]
        # print(part)
        part1 = re.split(pat2, part)[0]
        return part1
        # for part in parts:
        #     get_json_data(part)

command = input("enter task: ")
print(command)
for_add_prod = r'add product(s?)'
s = re.match(for_add_prod, command)
if s is None:
    print("command not found")
else:
    add_product_to_config()


# def get_data():
#     with open(p, 'r') as f:
#         content = f.read()
#         pat1 = r'\[section:.*\]\n'
#         parts = re.split(pat1, content)[1:]
#         print(parts)
#         for part in parts:
#             print(part.split("=")[1].strip(" \n"))
#
# get_data()
