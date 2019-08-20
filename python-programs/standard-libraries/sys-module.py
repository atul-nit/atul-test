import sys

# print(sys.version)
# print(sys.version_info)
# print(sys._current_frames())
# print(sys.modules.keys())
# print(sys.path)
# for p in sys.path:
#     print(p)
# print("enter something: ")
# a = sys.stdin.readline()
# print(a)

# get copyright information
# print(sys.copyright)

a = 10
b = 10
c = 10
print(sys.getrefcount(0))
print(sys.getrefcount(a))
