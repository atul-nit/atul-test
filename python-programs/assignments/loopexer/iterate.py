"""To iterate a loop from 1-20 and print its sum of current vaue and next value"""

l1 = list(range(1,21))
print(l1)
length = len(l1)

i = 0
for ele in l1:
    if( i != (length - 1)):
        print(l1[i] + l1[i+1])
        i += 1