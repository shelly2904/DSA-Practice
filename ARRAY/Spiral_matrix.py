def spiral_matrix(A, n, m):
    top = 0
    left = 0
    bottom = n - 1
    right = m - 1

    dir = 0
    no_element = n*m
    no_ele_visit = 0
    while no_element != no_ele_visit:
        if dir == 0:
            for i in range(left, right + 1):
                print(A[top][i])
                no_ele_visit += 1
            top += 1
        elif dir == 1:
            for i in range(top, bottom + 1):
                print(A[i][right])
                no_ele_visit += 1
            right -= 1
        if dir == 2:
            for i in range(right, left-1, -1):
                print(A[bottom][i])
                no_ele_visit += 1
            bottom -= 1
        if dir == 3:
            for i in range(bottom, top-1, -1):
                print(A[i][left])
                no_ele_visit += 1
            left += 1

        dir = (dir + 1) % 4


# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# spiral_matrix(arr, len(arr), len(arr[0]))


def spiral_matrix_2(n):


    result = [[0] * n for _ in range(n)]
    top = 0
    left = 0
    bottom = n - 1
    right = n - 1

    dir = 0
    no_element = n*n
    no_ele_visit = 0
    while no_element != no_ele_visit:
        if dir == 0:
            for i in range(left, right + 1):
                result[top][i] = no_ele_visit + 1
                no_ele_visit += 1
            top += 1
        elif dir == 1:
            for i in range(top, bottom + 1):
                result[i][right] = no_ele_visit + 1
                no_ele_visit += 1
            right -= 1
        if dir == 2:
            for i in range(right, left-1, -1):
                result[bottom][i] = no_ele_visit + 1
                no_ele_visit += 1
            bottom -= 1
        if dir == 3:
            for i in range(bottom, top-1, -1):
                result[i][left] = no_ele_visit + 1
                no_ele_visit += 1
            left += 1
        dir = (dir + 1) % 4

    return result


print(spiral_matrix_2(3))

