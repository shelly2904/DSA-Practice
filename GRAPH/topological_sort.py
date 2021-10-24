"""
Topological ordering is linear ordering of the vertices in directed acyclic graph
The answer will not be unique and also there will be no topological ordering of
cyclic graphs
"""

"""
Applications of Topological sort:
1. Cycle in directed graph detected
2. Ordering of tasks
3. Itinerary in Airport
"""
from collections import defaultdict, deque


# Assuming Input "G" is list of lists
def topological_sort(G):
    adj_list = defaultdict(list)
    indeg = defaultdict(int)

    for i in G:
        if len(i) > 1:
            adj_list[i[0]].append(i[1])
            indeg[i[1]] += 1

    queue = deque()
    for ver in adj_list.keys():
        if indeg[ver] == 0:
            queue.append(ver)

    cnt = 0
    while queue:
        cnt += 1
        x = queue.popleft()
        print(x)
        for i in adj_list[x]:
            indeg[i] -= 1
            if indeg[i] == 0:
                queue.append(i)


if __name__ == "__main__":
    # graph = [['A', 'C'],
    #          ['B', 'C'],
    #          ['C', 'D'],
    #          ['C', 'B'],
    #          ['D', 'E'],
    #          ['D', 'F']]

    graph = [['LAX', 'DXB'],
             ['DFW', 'JFK'],
             ['LHR', 'DFW'],
             ['JFK', 'LAX']]

    topological_sort(graph)
