# Find all the factors of a given number

def factors( num ):
    f = [1]
    for ele in range(2,num//2+1):
        if num%ele == 0:
            f.append(ele)
    f.append(num)
    print(f)

n = int(input("enter number: "))
factors(n)