"""
Heap Patterns
"""

"""
K-th smallest/largest element
"""

import heapq

class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return heapq.heappop(self.data)


class MinHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return self.data[0]

    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)


def k_smallest(arr, k):
    if not arr:
        return -1

    hp = MaxHeap()
    for i in range(0, len(arr)):
        hp.push(arr[i])
        while len(hp.data) > k:
            hp.pop()
    return [- i for i in hp.data]

def k_largest(arr, k):
    if not arr:
        return -1

    hp = MinHeap()
    for i in range(0, len(arr)):
        hp.push(arr[i])
        while len(hp.data) > k:
            hp.pop()

    return hp.data


"""
Given an array of n elements, where each element is at most k away from its target position, 
devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, 
an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Example:
Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}
"""
def k_sorted(arr, k):
    hp = MinHeap()

    res = []
    for i in range(len(arr)):
        hp.push(arr[i])
        if len(hp.data) > k:
            res.append(hp.pop())
    while hp.data:
        res.append(hp.pop())

    return res


"""
K-closest element
"""
def k_closest(arr, x, k):
    hp = MinHeap()

    res = []
    for i in range(len(arr)):
        hp.push((abs(x-arr[i]), arr[i]))

    i = 0
    while i < k:
        (idx, value) = hp.pop()
        res.append(value)
        i += 1
    return res

print(k_closest([6, 5, 7, 8, 10, 9], 7, 3))






# Calling functions
# print(k_sorted([6, 5, 3, 2, 8, 10, 9], 3))
# print(k_smallest([1,4,2,3,5,6], 3))
# print(k_largest([1,4,2,5,7,8,6], 3))