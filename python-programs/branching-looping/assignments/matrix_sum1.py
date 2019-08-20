m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# m = [
#     [1,2,3,4,5],
#     [10,20,30,40,50],
#     [10,22,33,44,55],
#     [1,3,5,7,9],
#     [1,5,6,5,8],
# ]

s = 0
i = 0
mi = len(m)//2
print(mi)
print(m[mi][mi])

for x in m:
    for y in x:
        s += y
print("sum of matrix: {}".format(s))
print("sum of matrix except middle ele: {}".format(s-m[mi][mi]))