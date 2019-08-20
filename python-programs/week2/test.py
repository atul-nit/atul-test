# # Method 1
# import hello1
# # #
# s_add = hello1.add(4,9)
# print(s_add)
# # #
# s_sub = hello1.subtract(2,8)
# print(s_sub)


# # Method 2
# from hello1 import add, subtract, x
# from hello1 import *
# #
# print(__name__)
# print(add(3,6))
# print(subtract(3,6))
# print(x)
#
# """
# __name__ = "hello1"
# __name__ = "__main__"
# """

# from mypack1 import md111
# # #
# md111.show_message( "this is message from test" )

# from mypack1.md111 import show_message
# # #
# show_message( "this is message from test" )

# import mypack1.md111 as m1
#
# m1.show_message("fff")


"----------------------------------"
# from hello1 import show
# from hello2 import show as show1
#
# show()
# show1()