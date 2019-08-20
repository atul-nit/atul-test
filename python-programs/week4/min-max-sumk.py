"""
Given an array of integers and a number k, find maximum sum of a subarray of size k.
"""


# O(n) solution in Python3 for finding
# maximum sum of a subarray of size k

# Returns maximum sum in
# a subarray of size k.
def maxSum(arr, n, k):
    # n must be greater
    if (n < k):
        print("Invalid")
        return -1

    # Compute sum of first
    # window of size k
    res = 0
    for i in range(k):
        res += arr[i]

    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    curr_sum = res
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        res = max(res, curr_sum)

    return res



def check_sum(arr, n, k):
    if (n < k):
        print("Invalid")
        return -1

    res = 0
    for i in range(k):
        res += arr[i]

    curr_sum = res
    for i in range(k, n):
        print("i: {} and i-k: {}".format(i, i-k))
        curr_sum += arr[i] - arr[i - k]
        res = max(res, curr_sum)

    return res


# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
# print(maxSum(arr, n, k))
check_sum(arr, n ,k)
# This code is contributed by Anant Agarwal.