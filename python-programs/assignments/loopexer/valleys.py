import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time_parts = s.split(":")
    h = int(time_parts[0])
    h_new = h
    if 'pm' in s.lower():
        if h != 12:
            h_new = h + 12
    else:
        if h == 12:
            h_new = h - 12
        else:
            h_new = h
    time_parts[0] = str(h_new)
    st = ":".join(time_parts).strip("APM")
    return st


if __name__ == '__main__':
    s = input("enter time: ")
    result = timeConversion(s)
    print(result)

