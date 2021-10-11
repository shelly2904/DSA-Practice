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

print(nsl([6,0,5,7,1,9]))