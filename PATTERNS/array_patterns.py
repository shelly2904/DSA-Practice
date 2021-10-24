"""
Array patterns
"""

"""
Product except self without division
"""


def product_except_self(arr):
    n = len(arr)
    left = [1] * n
    right = [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * arr[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * arr[i + 1]

    for i in range(n):
        arr[i] = left[i] * right[i]

    return arr


"""
PATTERN: Two pointers
Minimum merge operations to make array as palindrome
"""


def min_op_palindrome(arr):
    n = len(arr)
    i = 0
    j = n - 1
    count = 0

    while i < j:
        if arr[i] < arr[j]:
            arr[i + 1] += arr[i]
            i += 1
            count += 1
        elif arr[i] > arr[j]:
            arr[j - 1] += arr[j]
            j -= 1
            count += 1
        else:
            i += 1
            j -= 1

    return count


# print(product_except_self([1, 2, 3, 4]))
print(min_op_palindrome([6, 1, 4, 3, 1, 7]))
