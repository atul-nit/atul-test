"""To calculate facorial"""

num = int(input("Enter the num"))

fact = 1
while(num != 1):
    fact  = fact * (num)
    num -= 1
print(fact)
