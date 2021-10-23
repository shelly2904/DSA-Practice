"""
Binary Search
"""


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


"""
Binary Search on reverse sorted array
"""


def binary_search_reverse(arr, key):
    low = 0
    high = len(arr)

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


"""
Order Agnostic Search
"""


def order_agnostic_search(arr, key):
    if arr[0] <= arr[1]:
        return binary_search(arr, key)
    else:
        return binary_search_reverse(arr, key)


"""
First and last occurrence of element in sorted array
"""


def first_occ(arr, key):
    low = 0
    high = len(arr) - 1

    res = -1

    while low <= high:

        mid = low + (high - low) // 2
        if arr[mid] == key:
            res = mid
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return res


def last_occ(arr, key):
    low = 0
    high = len(arr) - 1

    res = -1

    while low <= high:

        mid = low + (high - low) // 2
        if arr[mid] == key:
            res = mid
            low = mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return res


"""
Number of times the array is rotated
"""


def rotation_times(arr):
    low = 0
    high = len(arr) - 1
    n = len(arr)

    while low <= high:

        mid = low + (high - low) // 2
        # prev = (mid - 1 + n) % n
        # nex = (mid + 1) % n
        prev = mid - 1
        nex = mid + 1

        if arr[prev] > arr[mid] and arr[mid] <= arr[nex]:
            return mid
        elif arr[mid] > low:
            low = mid + 1
        else:
            high = mid - 1
    return -1


"""
Search in nearly sorted array
"""

def search_nearly_sorted(arr, key):
    

# Binary search
# print("Element found at", binary_search([1, 2, 3, 4, 5, 6, 7], 9))

# Binary search reverse
# print("Element found at", binary_search_reverse([7, 6, 5, 4, 3, 1, 0], 1))

# Order Agnostic Search
# print("Element found at", order_agnostic_search([1, 2, 3, 4, 5, 6, 7], 2))

# First and last occurrence in sorted array
# first = first_occ([1, 2, 4, 4, 4, 6, 7], 4)
# last = last_occ([1, 2, 4, 4, 4, 6, 7], 4)
# print(last - first + 1)

# Rotation n times
print("Element found at", rotation_times([18, 19, 20, 21, 2, 3, 4, 5]))
