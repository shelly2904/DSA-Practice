# https://leetcode.com/problems/move-zeroes/


def move_zeroes_left(arr):
    i = j = len(arr) - 1

    while i >= 0 and j >= 0:
        if arr[i] != 0:
            arr[j] = arr[i]
            j -= 1
        i -= 1

    while j >= 0:
        arr[j] = 0
        j -= 1

    return arr

def move_zeroes_right(arr):
    i = j = 0

    while i < len(arr) and j < len(arr):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
        i += 1

    while j < len(arr):
        arr[j] = 0
        j += 1

    return arr

print(move_zeroes_right([0, 1, 2, 3, 0, 5]))
