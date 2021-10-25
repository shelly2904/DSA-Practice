"""
Few questions asked in companies
"""

"""
Maximum number of flights in air
"""

from queue import PriorityQueue


class Flight:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def max_flights_air(arr):
    max_flights = 0

    pq = PriorityQueue()

    # Sorting by start time
    arr = sorted(arr, key=lambda x: x.start)

    for i in arr:
        while not pq.empty() and pq.queue[0][1] < i.start:
            pq.get()
        pq.put((i.start, i.end))
        max_flights = max(max_flights, len(pq.queue))

    return max_flights


input = [Flight(1, 4), Flight(2, 5), Flight(7, 9)]
print(max_flights_air(input))
