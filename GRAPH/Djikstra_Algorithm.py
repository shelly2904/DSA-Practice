from queue import PriorityQueue

# Complexity : O(|E| + |V| log |V|)


class Graph:
    def __init__(self, n_vertices):
        self.vertices = n_vertices
        self.edges = [[-1 for _ in range(n_vertices)] for _ in range(n_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, start_vertex):
        d = {v: float('inf') for v in range(self.vertices)}
        d[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, cur_vertex) = pq.get()
            self.visited.append(cur_vertex)

            for neighbor in range(self.vertices):
                if self.edges[cur_vertex][neighbor] != -1:
                    distance = self.edges[cur_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = d[neighbor]
                        new_cost = d[cur_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            d[neighbor] = new_cost

        return d


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3)

D = g.dijkstra(0)

for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])
