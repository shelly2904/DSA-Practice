"""
Allocate Pages of Books
"""


def is_valid(arr, n, k, mx):
    st = 1
    sum1 = 0

    for i in range(n):
        sum1 += arr[i]
        if sum1 > mx:
            st += 1
        if st > k:
            return False
    return True


def allocate_pages(arr, k):
    start = max(arr)
    end = sum(arr)
    n = len(arr)

    res = -1  # not possible case
    if n < k:
        return res

    while start <= end:
        mid = start + ((end - start) // 2)

        if is_valid(arr, n, k, start):
            res = mid
            end = mid - 1
        else:
            start = mid + 1

    return res


print(allocate_pages([10, 20, 30, 40], 2))
