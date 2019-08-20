class Users:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def __str__(self):
        return self.fullname()

    @classmethod
    def from_str(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, age)

# tom = Users.from_str("TOM,Jones,78")
# print(tom.fullname())
with open("classtest.txt", "r") as fp:
    lines = fp.readlines()
    obj_dict = {}
    i = 1
    for line in lines:
        key = "user"+str(i)
        value = Users.from_str(line)
        obj_dict[key] = value
        i += 1

for key, val in obj_dict.items():
    print(key, val)