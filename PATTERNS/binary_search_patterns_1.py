from binary_search_patterns import binary_search, first_occ
"""
Search in nearly sorted array
"""


def search_nearly_sorted(arr, key):
    pass


"""
Find floor and ceil of element in sorted array
"""


def find_floor(arr, key):
    low = 0
    high = len(arr) - 1
    n = len(arr)
    floor = -1

    while low <= high:

        mid = low + (high - low) // 2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] > key:
            high = mid - 1
        else:
            floor = arr[mid]
            low = mid + 1
    return floor


def find_ceil(arr, key):
    low = 0
    high = len(arr) - 1
    n = len(arr)
    ceil = -1

    while low <= high:

        mid = low + (high - low) // 2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            low = mid + 1
        else:
            ceil = arr[mid]
            high = mid - 1
    return ceil


"""
Next Alphabetical element
"""


def next_alpha_ele(arr, key):
    pass


"""
Find element in infinite sorted array
"""


def search_infinite(arr, key):
    low = 0
    high = 1
    val = arr[0]

    while val < key:
        low = high
        high *= 2
        val = arr[high]

    idx = binary_search(arr[low: high+1], key)
    if idx == -1:
        return idx
    else:
        return idx + low


def search_1(arr, key):
    low = 0
    high = 1
    val = arr[0]

    while val < key:
        low = high
        high *= 2
        val = arr[high]

    idx = first_occ(arr[low: high+1], key)
    if idx == -1:
        return idx
    else:
        return idx + low



"""
Minimum difference element
"""


def minimum_diff(arr, key):
    pass


# Floor and ceil
# print("Floor is", find_floor([1, 2, 3, 4, 6, 7, 8], 5))
# print("Ceil is", find_ceil([1, 2, 3, 4, 6, 7, 8], 5))

# Search in infinite
# print(search_infinite([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170], 100))
print(search_1([0, 0, 0, 1, 1, 1], 1))