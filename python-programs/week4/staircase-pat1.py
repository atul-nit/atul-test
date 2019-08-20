"""
n = 4
output:

   #
  ##
 ###
####
"""

n = int(input("enter size: "))

i = n
while i > 0:
    j = 0
    while j < i-1:
        print(" ", end="")
        j += 1
    k = 0
    while k < n-i+1:
        print("#", end="")
        k += 1
    print()
    i -= 1

