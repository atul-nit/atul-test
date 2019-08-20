# opening a file
# f = open("test1.txt", "r")
# print(f.read())
# f.close()

#opening a file using with statement
# with open("test1.txt", "r") as fr:
#     contents = fr.read()   # reading entire content at once
#     print(contents)
#     print(type(contents))

# with open("test1.txt", "r") as fr:
#     lines = fr.readlines()   # reading all lines in list
    # print(lines)
#     #print(type(lines))
#     for line in lines:
#         print(line, end="")

# with open("test1.txt", "r") as fr:
#     line = fr.readline()  # reads the current line and moves to next line
#     print(line, end="")
#     while line != '':
#         line = fr.readline()
#         print(line, end="")

# with open('test1.txt', "r") as fr:
    # for line in fr:
    #     print(line)
    # fr.seek(0)
    # for line in fr:
    #     print(line)
    # print(fr.read(5))
    # content = fr.read()
    # print(len(content))
    # print(fr.tell())

# fileNot FoundError
# with open("test3.txt", "r") as fr:
#     # for l in fr:
#     #     print(l)
#     # fr.seek(0)
#     # for l in fr:
#     #     print(l)
#     print(fr.read(5))
#     fr.seek(0)
#     print(fr.read())


# writing a string to a file
# with open("test1.txt", "w") as fw:
#     to_write = "hello there!\nHow are you"
#     fw.write(to_write)
#
# with open("test2.txt", "w") as fw:
#     pass

# with open("test1.txt", "r") as fr:
#     with open("test2.txt", "w") as fw:
#         for line in fr:
#             fw.write(line)

# with open("fnums1.txt", "r") as fr1:
#     with open("fnums2.txt", "r") as fr2:
#         with open("fnums3.txt", "w") as fw:
#             len_fnums1 = len(fr1.readlines())
#             len_fnums2 = len(fr2.readlines())
#             limit = len_fnums1 if len_fnums1>len_fnums2 else len_fnums2
#             print(limit)
#             print(fr1.read())
#             print(fr1.readline())
#             # for i in range(limit):
#             #     line1 = fr1.readline()
#             #     line2 = fr2.readline()
#             #     print(line1)
#                 #print(int(line1))

# with open("fnums1.txt", "r") as fr1:
#     with open("fnums2.txt", "r") as fr2:
#         with open("fnums3.txt", "w") as fw:
#             print(fr1.readlines())
#             print(fr1.read())

# with open("test2.txt", "a") as fw:
#     fw.write("\nthis line has been added")

# To create a new file
"""
"x" : Create - will create a file, returns an error if the file exist
"w" : Write - will create a file if the specified file does not exist
"a" : Append - will create a file if the specified file does not exist
"""
# f = open("myfile.txt", "x")
