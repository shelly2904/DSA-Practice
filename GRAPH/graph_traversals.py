# Graph Traversals: BFS and DFS

class Queue(object):
    def __init__(self):
        self.arr = []
        self.front = 0
        self.rear = -1

    def push(self, data):
        self.arr.append(data)
        self.rear += 1

    def pop(self):
        if not self.arr:
            return False
        top = self.arr[self.front]
        del self.arr[self.front]
        return top


class Stack(object):
    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, data):
        self.arr.append(data)
        self.top += 1

    def pop(self):
        if not self.arr:
            return False
        top = self.arr[self.top]
        del self.arr[self.top]
        self.top -= 1
        return top


# BFS
def bfs(graph, start):
    visited = []
    queue = Queue()
    queue.push(start)
    while len(queue.arr) > 0:
        ele = queue.pop()
        if ele not in visited:
            print(ele)
            visited.append(ele)
            for i in graph[ele]:
                queue.push(i)


# DFS
def dfs(graph, start):
    visited = []
    stack = Stack()
    stack.push(start)
    while len(stack.arr) > 0:
        ele = stack.pop()
        if ele not in visited:
            print(ele)
            visited.append(ele)
            for i in graph[ele]:
                stack.push(i)


if __name__ == "__main__":
    graph = {'A': {'B', 'C'}, 'B': {'A', 'D', 'E'},
             'C': {'A', 'F'}, 'D': {'B'},
             'E': {'B', 'F'},
             'F': {'C', 'E'}}

# bfs(graph, 'A')
# dfs(graph, 'A')
