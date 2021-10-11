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



"""
Maximum Area histogram in Binary Matrix
"""

"""
Rain water trapping
"""

print(stock_span_problem([100, 80, 60, 70, 60, 75, 85]))
