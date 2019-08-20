from os import listdir
from os.path import isfile, join
import os


# mypath = 'D:\python-related\python practice'
mypath = '/Users/atsingh/Documents/python-programs'
# ld = os.listdir(mypath)
# print(ld)


## list only file in a path
# ld = os.listdir(mypath)
# for f in ld:
#     if isfile(join(mypath, f)):
#         print(join(mypath, f))
#         print(f)

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)


## list all the csv file in a path
# ld = listdir(mypath)
# r = []
# for f in ld:
#     filepath = join(mypath, f)
#     if isfile(filepath):
#         if filepath.endswith(".txt"):
#             r.append(f)
# print(r)
# print(len(r))

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# # print(onlyfiles)
# for f1 in onlyfiles:
#     if f1.split(".")[1] == 'csv':
#         print(f1)

# s = "sample.csv".split(".")
# print(s)

# list everything inside the path
# for f in listdir(mypath):
#     print(f)

# list only files in the given path
# for f in listdir(mypath):
#     # print(join(mypath,f))
#     if isfile(join(mypath,f)):
#         print(f)

# list current working directory

# """current file relative path"""
# print(__file__)
# """current file absolute or relative path"""
# print(os.path.realpath(__file__))
# """current directory path"""
# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)

# create a directory
# path_to_create = 'D:\python-related\python practice\week33'
# path_to_create = '/Users/atsingh/Documents/python-programs/week32'
# os.mkdir(path_to_create)
# print(os.path.exists(path_to_create))
# remove the directory
# path_to_remove = 'D:\python-related\python practice\week33'
# path_to_remove = '/Users/atsingh/Documents/python-programs/week32'
# os.rmdir(path_to_remove)

# print(__file__)
# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# print(os.getcwd())


## list all files and directories in the current directory
# l = os.listdir('.')
# print(os.listdir(os.getcwd()))
# print(l)