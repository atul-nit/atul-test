"""
Given five positive integers, find the minimum and maximum values that can be
calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as
a single line of two space-separated long integers.
"""

def miniMaxSum(arr):
    max_val = max(arr)
    min_val = min(arr)
    max_sum = sum(arr) - min_val
    min_sum = sum(arr) - max_val
    print(min_sum, max_sum)


arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)