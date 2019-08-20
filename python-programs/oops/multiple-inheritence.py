class A:
    def __init__(self):
        print("contructor AAAAA")
        super().__init__()

    def show(self):
        print("show from AAAA")


class B:
    def __init__(self):
        print("constructor BBBB")

    def show(self):
        print("show from BBBB")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("constructor CCCC")

c1 = C()
c1.show()