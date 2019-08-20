# Creating your own exception class
# class HeightError(Exception):
#     pass
# h = int(input("enter height: "))
# try:
#     if h <= 0:
#         raise HeightError("height must be greater than 0")
# except HeightError as e:
#     print("from height error:")
#     print(e)

class HeightError(Exception):
    def __init__(self, msg):
        self.msg = "from HeightError "+msg
        # super().__init__("from HeightError "+msg)
    # def __str__(self):
    #     return self.msg

h = int(input("enter height: "))
# # ee = HeightError("hello there")
# # print(ee)
# try:
#     if h<=0:
#         raise HeightError("height must be greater than 0")
# except HeightError as e:
#     print(e)

try:
    if h <= 0:
        raise HeightError("height must be greater than 0")
except HeightError as e:
    print(e)