s = "This is my home"
words = 0
space = 0
flag_space = 0
for c in s:
    if c == ' ':
        words += 1
        space += 1
print("words: ", words+1)
print("space: ", space)