def add(n1, n2):
    print("hello1 add")
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def show():
    print("show from hello 1")

print("from module hello1")

x = 10

print(__name__)

if __name__ == "__main__":
    print(add(1,4))
    print(subtract(7,3))

