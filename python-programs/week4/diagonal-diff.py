import math
m = [
    [12,20,30],
    [13,15,18],
    [42,19,10]
]

rows = len(m)
d1 = 0
d2 = 0
for r in range(rows):
    for c in range(rows):
        # Sum of primary diagonal
        if r == c:
            print(m[r][c])
            d1 += m[r][c]

        # Sum of secondary diagonal
        if r == rows-c-1:
            print(m[r][c])
            d2 += m[r][c]
print("d1: %d" % d1)
print("d2: %d" % d2)
print(abs(d1-d2))

