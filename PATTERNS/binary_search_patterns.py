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


# Binary search
# print("Element found at", binary_search([1, 2, 3, 4, 5, 6, 7], 9))

# Binary search reverse
# print("Element found at", binary_search_reverse([7, 6, 5, 4, 3, 1, 0], 1))

# Order Agnostic Search
# print("Element found at", order_agnostic_search([1, 2, 3, 4, 5, 6, 7], 2))

# First and last occurrence in sorted array
print("Element found at", first_occ([1, 2, 4, 4, 4, 6, 7], 4))
print("Element found at", last_occ([1, 2, 4, 4, 4, 6, 7], 4))
