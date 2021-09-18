def median_sorted_arrays(A, B, n, m):
    # A will always be smaller array

    if n > m:
        # Handling the case if B is smaller
        return median_sorted_arrays(B, A, m, n)

    low = 0
    high = n
    while low <= high:

        import math
        pos_x = (low + high) >> 1
        pos_y = ((n + m + 1) >> 1) - pos_x  # handle both odd and even

        import sys
        max_left_x = -sys.maxsize - 1 if pos_x == 0 else A[pos_x - 1]
        max_left_y = -sys.maxsize - 1 if pos_y == 0 else B[pos_y - 1]

        min_right_x = sys.maxsize if pos_x == n else A[pos_x]
        min_right_y = sys.maxsize if pos_y == m else B[pos_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (n + m) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_y, min_right_x)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = pos_x - 1
        else:
            low = pos_x + 1

    return 0


A = [1, 3, 8, 9, 15, 16, 20, 22, 26]
B = [7, 11, 18, 19, 21, 25]
print(median_sorted_arrays(A, B, len(A), len(B)))