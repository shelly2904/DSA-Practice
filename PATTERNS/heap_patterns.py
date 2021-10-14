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
    return -hp.data[0]

def k_largest(arr, k):
    if not arr:
        return -1

    hp = MinHeap()
    for i in range(0, len(arr)):
        hp.push(arr[i])
        while len(hp.data) > k:
            hp.pop()

    return hp.data[0]

print(k_smallest([1,4,2,5,6], 3))
print(k_largest([1,4,2,5,6], 1))