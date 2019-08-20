import xml.etree.ElementTree as ET

xmlfile = 'my1.xml'
# xmlfile = r'D:\python-related\python practice\myxml1.xml'
tree = ET.parse(xmlfile)
root = tree.getroot()
# Get the root element object
# print(tree.__class__.__name__)
# print(root)
# Get the root element tag name
# print(root.tag)

# for emp in root:
#     print(emp.tag)
#     for person in emp:
#         if person.text is not None:
#             print("{} : {}".format(person.tag, person.text))
#         else:
#             print("{} : {}".format(person.tag, person.attrib))

# for persons in root.findall('./Person'):
#     for person in persons:
#         if person.text is not None:
#             print("{} : {}".format(person.tag, person.text))
#         else:
#             print("{} : {}".format(person.tag, person.attrib))


# Get current children of root node
# # # Works fine if all nodes have text
# for item in root:
#     r = {}
#     for p in item:
#         r[p.tag] = p.text.encode("utf8")
#     print(r)




# Get child nodes of root
# data = []
# for item in root:
#     result = {}
#     for person in item:
#         if person.text != None:
#             result[person.tag] = person.text.encode('utf8')
#         else:
#             result[person.tag] = person.attrib["name"]
#     data.append(result)

# for item in root:
#     for person in item:
#         print(person.attrib)
#         print("----------")

""" [{}, {}, {}]"""
# data = []
# for person in root:
#     result = {}
#     for person_attr in person: # fname, lname, city, expertise
#         if person_attr.text is not None:
#             result[person_attr.tag] = person_attr.text.encode('utf8')
#         else:
#             result[person_attr.tag] = person_attr.attrib["name"]
#     data.append(result)
#
# for person in data:
#     print(person)

# result = []
# for person in root.findall('./person'):
#     person_detail = {}
#     for person_attr in person:
#         if person_attr.text != None:
#             person_detail[person_attr.tag] = person_attr.text.encode('utf8')
#         else:
#             person_detail[person_attr.tag] = person_attr.attrib["name"]
#     result.append(person_detail)
#
# for person in result:
#     print(person)

