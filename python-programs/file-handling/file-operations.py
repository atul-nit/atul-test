# To remove a file
# import os
# os.remove("myfile.txt")

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# reading and writing the file without truncating
# we can't read multiple times. To do so set the file pointer to 0
# with open("test1.txt", "r+") as frw:
    # content = frw.read()
    # print(content)
    # frw.write("some line")
    # frw.seek(0) # setting the file pointer to zero
    # content = frw.read()
    # print("\n"+content)
    # frw.write("fgfgfgfgfgfg")

# writing and reading the file with truncating
# with open("test1.txt", "w+") as fwr:
#     fwr.write("Hello there\nHow are you")
#     fwr.seek(0)
    # print("initial: {}".format(fwr.tell()))
    # print(fwr.read())
    # print("final: {}".format(fwr.tell()))


# appending and writing to the file without truncating
with open("test1.txt", "a+") as fwr:
    fwr.write("your name please\nWhere are you from?")
    fwr.seek(0)
    print(fwr.read())