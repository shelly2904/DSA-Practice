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
        return self.data[0]

    def push(self, val):
        heapq.heappush(self.data, val)
        self.data = list(reversed(self.data))

    def pop(self):
        return heapq.heappop(list(reversed(self.data)))
        self.data = list(reversed(self.data))

#
# class MaxHeap:
#     def __init__(self):
#         self.data = []
#
#     def top(self):
#         return -self.data[0]
#
#     def push(self, val):
#         if "tuple" in str(type(val)):
#             val = (-val[0], val[1])
#         else:
#             val = -val
#         heapq.heappush(self.data, val)
#
#     def pop(self):
#         return - heapq.heappop(self.data)


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


"""
K-frequent element
"""
from collections import defaultdict

def k_frequent(arr, k):
    hp = MaxHeap()
    res = []

    hashmap = defaultdict(int)

    for i in range(len(arr)):
        hashmap[arr[i]] += 1

    for key,v in hashmap.items():
        hp.push((v, key))

    id = 0
    while id < k:
        (idx, value) = hp.pop()
        res.append(value)
        id += 1

    return res


"""
Find median of running integers
"""

def find_running_median(arr):
    minheap = MinHeap()
    maxheap = MaxHeap()

    for num in arr:
        if not maxheap.data or maxheap.data[0] >= num:
            maxheap.push(num)
        else:
            minheap.push(num)

        if len(maxheap.data) > len(minheap.data) + 1:
            minheap.push(maxheap.pop())
        elif len(maxheap.data) < len(minheap.data):
            maxheap.push(minheap.pop())

        if len(maxheap.data) == len(minheap.data):
            print("Median is: ", (maxheap.pop()/2 + minheap.pop()/2))
        else:
            print("Median is: ", maxheap.pop())

find_running_median([1, 2, 3, 4 ])

# print(k_frequent([6, 6, 6, 9, 10, 9, 10, 8], 3))

# Calling functions
# print(k_closest([6, 5, 7, 8, 10, 9], 7, 3))
# print(k_sorted([6, 5, 3, 2, 8, 10, 9], 3))
# print(k_smallest([1,4,2,3,5,6], 3))
# print(k_largest([1,4,2,5,7,8,6], 3))