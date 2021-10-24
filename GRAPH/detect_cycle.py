from graph_traversals import Stack
from collections import deque, defaultdict


def detect_cycle_undirected_bfs(G, s):
    visit = defaultdict(bool)
    queue = deque()
    queue.append((s, -1))

    visit[s] = True
    while queue:
        (node, parent) = queue.popleft()
        for i in G[node]:
            if not visit[i]:
                visit[i] = True
                queue.append((i, node))
            elif i != parent:
                return True
    return False


def detect_cycle_undirected_dfs(G, s, visit, parent):
    visit[s] = True
    for i in G[s]:
        if not visit[i]:
            if detect_cycle_undirected_dfs(G, i, visit, s):
                return True
        elif i != parent:
            return True
    return False


def detect_cycle_directed_dfs(G, s, visit):
    visit[s] = True
    for i in G[s]:
        if not visit[i]:
            if detect_cycle_undirected_dfs(G, i, visit, s):
                return True
        else:
            return True
    return False


# def detect_cycle_directed(G, s):
#     is_cyclic = False
#     current = s
#
#     RecurStack = Stack()
#     NorStack = Stack()
#
#     NorStack.push(current)
#     while len(NorStack.arr) > 0:
#         current = NorStack.pop()
#         print("Traversing ", current)
#         child = G[current]
#         if any([True if c in RecurStack.arr else False for c in child]):
#             is_cyclic = True
#         for i in child:
#             NorStack.push(i)
#         RecurStack.push(current)
#     return is_cyclic


if __name__ == "__main__":
    '''
    graph = {'0': set(['1', '2']),
         '1': set(['2']),
         '2': set(['0', '3']),
         '3': set(['3'])}
    '''

    graph = {'0': {'1'},
             '1': {'2'},
             '2': {'3'},
             '3': {'0'}}

    # graph = {'0': {},
    #          '1': {},
    #          '2': {},
    #          '3': {},
    #          '4': []}

    visited = defaultdict(bool)
    start = '0'
    # print(detect_cycle_undirected_dfs(graph, start, visited, -1))
    print(detect_cycle_undirected_bfs(graph, start))
    # print(detect_cycle_directed_dfs(graph, start, visited))

    # if detect_cycle_directed(graph, start):
    #     print("There is a cycle")
    # else:
    #     print("There is no cycle")
