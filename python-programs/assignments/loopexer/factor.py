"""to find factors of a number"""

num = int(input("Enter the number: "))
l1 = list(range(1,num + 1))
print(l1)


for ele in l1:
    if(num % ele == 0):
        print(ele)





