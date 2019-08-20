class A:
    def __init__(self):
        print("contructor AAAAA")

    def show(self):
        print("show from AAAA")

class B(A):
    def __init__(self):
        super().__init__()
        print("constructor BBBB")

    # def show(self):
    #     print("show from BBBB")

class C(B):
    def __init__(self):
        super().__init__()
        print("constructor CCCC")

c1 = C()
c1.show()