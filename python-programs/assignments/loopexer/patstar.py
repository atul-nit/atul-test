"""To print stars in a fashion"""


row = int(input("Enter the no. of base row stars : "))
l1 = list(range(1,row + 1,2)) # [1,3,5,7,9]
print(l1)
length = len(l1)
tabLen = (row - 1)//2 # 4
print (tabLen)

for ele in l1:
    i = 1
    while( i <= tabLen):
        print(" ",end="")
        i += 1
    j = 1
    while(j <= ele):
        print("*", end = "")
        j += 1
    print("\n")
    tabLen -= 1

