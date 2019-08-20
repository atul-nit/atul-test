# WAP to find a number using binary search
"""
Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array.
If the value of the search key is less than the item in the middle of the interval,
narrow the interval to the lower half. Otherwise narrow it to the upper half.
Repeatedly check until the value is found or the interval is empty.
"""

def binarySearch(arr, l, r, x):
    # check the base case:
    if r >= l:
        mid = l + (r - 1)//2

        # If element is present at the middle itself
        if x == arr[mid]:
            return mid

        # If element is smaller than mid, then it
        # can be only present in the left subarray
        elif x < arr[mid]:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can be present
        # only in the right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # Element is not present in the list
        return -1


# Test Array
arr = [1,4,6,7,8,19]
x = 5

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index %d" %result)
else:
    print("Element is not present in array")

