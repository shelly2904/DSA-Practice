"""
Few questions asked in companies
"""

"""
Maximum number of flights in air
"""

from queue import PriorityQueue


def max_flights_air(arr):
    max_flights = 0

    pq = PriorityQueue()

    # Sorting by start time
    arr = sorted(arr, key=lambda x: x[0])
    for i in arr:
        while not pq.empty() and pq.queue[0][1] < i[0]:
            pq.get()
        pq.put(i)
        max_flights = max(max_flights, len(pq.queue))

    return max_flights


input = [[4, 8], [2, 5], [17, 20], [10, 21], [9, 18]]
print(max_flights_air(input))
