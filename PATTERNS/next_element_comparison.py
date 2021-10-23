"""
Foundation patterns:
1. Next Greater to the Right (NGR)
2. Next Greater to the Left (NGL)
3. Next Smaller to the Right (NSR)
4. Next Smaller to the Left (NSL)
"""

from collections import deque


def ngr(arr):
    # Output arr
    res = [-1] * len(arr)

    # stack
    stack = deque()

    # to start from the end
    for i in reversed(range(len(arr))):
        while stack:
            if stack[-1] <= arr[i]:
                stack.pop()
            else:
                res[i] = stack[-1]
                break
        stack.append(arr[i])
    return res


def ngl(arr):
    # Output arr
    res = [-1] * len(arr)

    # stack
    stack = deque()

    # to start from the end
    for i in range(len(arr)):
        while stack:
            if stack[-1] <= arr[i]:
                stack.pop()
            else:
                res[i] = stack[-1]
                break
        stack.append(arr[i])
    return res


def nsr(arr):
    # Output arr
    res = [-1] * len(arr)

    # stack
    stack = deque()

    # to start from the end
    for i in reversed(range(len(arr))):
        while stack:
            if stack[-1] > arr[i]:
                stack.pop()
            else:
                res[i] = stack[-1]
                break
        stack.append(arr[i])
    return res


def nsl(arr):
    # Output arr
    res = [-1] * len(arr)

    # stack
    stack = deque()

    # to start from the end
    for i in range(len(arr)):
        while stack:
            if stack[-1] > arr[i]:
                stack.pop()
            else:
                res[i] = stack[-1]
                break
        stack.append(arr[i])
    return res


"""
Stock Span Problem
"""


def stock_span_problem(arr):
    # Output arr
    res = [-1] * len(arr)

    # stack
    stack = deque()

    # to start from the end
    for i in range(len(arr)):
        while stack:
            if stack[-1][0] <= arr[i]:
                stack.pop()
            else:
                res[i] = stack[-1][1]
                break
        stack.append((arr[i], i))

    for i in range(len(res)):
        # if res[i] == -1:
        #     continue

        res[i] = i - res[i]

    return res


"""
Maximum Area in Histogram
"""
import sys


def mah(arr):
    nsr_arr = [-1] * len(arr)
    nsl_arr = [-1] * len(arr)

    # stack
    stack = deque()

    # to start from the end
    for i in range(len(arr) - 1, -1, -1):
        while stack:
            if stack[-1][0] > arr[i]:
                stack.pop()
            else:
                nsr_arr[i] = stack[-1][1]
                break
        stack.append((arr[i], i))

    # stack
    stack1 = deque()

    # to start from the end
    for i in range(len(arr)):
        while stack1:
            if stack1[-1][0] > arr[i]:
                stack1.pop()
            else:
                nsl_arr[i] = stack1[-1][1]
                break
        stack1.append((arr[i], i))

    max_area = - sys.maxsize - 1
    for i in range(len(arr)):
        ngl_index = nsl_arr[i]
        ngr_index = nsr_arr[i]

        # if ngl_index == -1 or ngr_index == -1:
        #     continue
        curr_area = (ngr_index - ngl_index - 1) * arr[i]
        max_area = max(max_area, curr_area)

    return max_area


"""
Maximum Area histogram in Binary Matrix
"""


def mah_matrix(arr):
    r = len(arr)
    c = len(arr[0])
    max_area = -sys.maxsize - 1

    res = [0] * c
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0:
                res[j] += arr[i][j]
                max_area = max(max_area, mah(res))

    return max_area


"""
Rain water trapping
"""

def rain_water_trapping():
    pass

# print(mah([6, 2, 5, 4, 5, 1, 2, 6]))

print(mah_matrix([[1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]))
