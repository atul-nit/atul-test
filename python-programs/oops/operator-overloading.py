class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Vector(self.a+other.a, self.b+other.b) # Vector(11, 9)

    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)

    def __str__(self):
        return "({},{})".format(self.a, self.b)

v1 = Vector(2, 5)
v2 = Vector(9, 4)
v3 = v1+v2
v4 = v1-v2
print(v1)
print(v2)
print(v3)
print(v4)

"""
(2,5)
(9,4)
Vector(2+9, 5+4) => (11, 9)
"""

