from collections import deque, defaultdict

"""
Eulerian Circuit or path is a path in a graph that visits every edge exactly once.
Given a directed graph, check whether it has an Eulerian Path or not

Eulerian path in directed graph if and only if following conditions are satisfied:
1. out_degree = 1 + in_degree (atmost)
2. in_degree = 1 + out_degree (atmost)
3. in_degree == out_degree
"""

def eulerian_circuit():
    pass


"""
PATTERN: BFS
Rotting oranges
"""


def rotting_oranges(grid):
    # rows and columns
    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    visited = set()

    d = 0

    # first store rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
                visited.add((r,c))

    while queue:
        r, c, d = queue.popleft()

        # extract 4-dimension neighbours

        for n1, n2 in [(r + 1, c),
                         (r - 1, c),
                        (r, c - 1),
                        (r, c + 1)]:
            if 0 <= n1 < rows and 0 <= n2 < cols:
                if (n1, n2) not in visited and grid[n1][n2] == 1:
                    queue.append((n1, n2, d+1))
                    visited.add((n1, n2))

    # Check if there are any fresh oranges left
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                return -1

    return d


print(rotting_oranges([[0,2]]))




