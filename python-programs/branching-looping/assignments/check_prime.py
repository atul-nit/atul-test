l1 = [141, 41, 75, 44, 243, 331]

count = 0
for val in l1:
    i = 1
    is_prime = True
    while i <= val//2:
        i += 1
        if val%i == 0:
            is_prime = False
            break
    if is_prime:
        print("{} is prime".format(val))
        count += 1
    else:
        print("{} is not prime".format(val))
print("there are {} prime numbers in the list".format(count))

