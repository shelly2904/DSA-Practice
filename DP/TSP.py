
# coding: utf-8

# In[5]:

from math import radians, cos, sin, asin, sqrt
import numpy as np
from itertools import combinations
from copy import deepcopy
import time


#using the haversine formula: https://en.wikipedia.org/wiki/Haversine_formula
def find_dist(coord1, coord2):
    lat1, lon1, lat2, lon2 = map(radians, [coord1['lat'], coord1['lon'], coord2['lat'], coord2['lon']])
    dlat = lat2 - lat1
    dlon = lon2 - lon1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c    #radius of earth
    return km


class TSP_Solver(object):
    def __init__(self):
        self.minCost = {} #cost of visiting a vertex from start via some nodes
        self.Parent = {} #parent for vertex
    
    def make_possible_combinations(self, node_list, start):
        node_list1 = deepcopy(node_list)
        node_list1.remove(start)
        output = sum([map(list, combinations(node_list1, i)) for i in range(len(node_list1) + 1)], [])
        return output
    
    #using Held-Karp Algorithm: https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
    def compute_cost(self, node_list, start, dist):
        #create all subsets
        subsets = self.make_possible_combinations(node_list, start)
        subsets.sort(lambda x,y: len(x) < len(y))
        
        for subset in subsets:
            for node in node_list:
                if node == start:
                    continue

                if node in subset:
                    continue
                cost = 0
                parent = start
                if not subset:
                    cost = dist[start][node]
                    parent = start
                else:
                    cost_list = []
                    for vertex in subset:
                        subset_temp = deepcopy(subset)
                        subset_temp.remove(vertex)
                        cost_list.append((vertex, self.minCost[str([vertex, subset_temp])] + dist[vertex, node]))
                    temp = min(cost_list, key = lambda t: t[1])
                    cost = temp[1]
                    parent = temp[0]
                
                #Storing the subproblems
                self.minCost[str([int(node), subset])] = cost
                self.Parent[str([int(node), subset])] = parent
                
        #We need to reach the start vertex:
        #considering subset [start, [all nodes]]
        
        cost_list = []
        last_subset = subsets[-1]
        start_vertex = start
        for vertex in last_subset:
            subset_temp = deepcopy(last_subset)
            subset_temp.remove(vertex)
            cost_list.append((vertex, self.minCost[str([vertex, subset_temp])] + dist[vertex, start_vertex]))
        temp = min(cost_list, key = lambda t: t[1])
        cost = temp[1]
        parent = temp[0]
        self.minCost[str([int(start_vertex), subset])] = cost
        self.Parent[str([int(start_vertex), subset])] = parent
        #printing the tour
        self.printTour(start, node_list)
    
    
    def printTour(self, start, node_list):
        nodes = deepcopy(node_list)
        vertex =start
        while nodes:
            print 'Go to vertex ', vertex 
            nodes.remove(vertex)
            vertex = self.Parent[str([vertex, nodes])]
        print 'Go to vertex ', vertex
        if vertex == start:
            print "Traversed all"
        else:
            print "Something is wrong :-("
        


if __name__=="__main__":
    #graph with coordinates, 
    graph = [{'lat': 28.41, 'lon': 77.27}, 
             {'lat': 28.51, 'lon': 77.29},
             {'lat': 28.56, 'lon': 77.37},
             {'lat': 28.47, 'lon': 77.30},
             {'lat': 28.78, 'lon': 77.31},
             {'lat': 28.65, 'lon': 77.32},
             {'lat': 28.42, 'lon': 77.33},
             {'lat': 28.50, 'lon': 76.79}]

    
    nodes = [x for x in range(0, len(graph))]   #naming the nodes as 0.....n
    n = len(nodes)
    start_vertex = 0
    dist_matrix = np.zeros(shape=(n, n))
    
    #compute the distance matrix
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
            if dist_matrix[i][j] != 0:
                continue
            dist_matrix[i][j] = find_dist(graph[nodes[i]], graph[nodes[j]])

    #Creating TSP object
    tsp = TSP_Solver()
    start = time.clock()
    tsp.compute_cost(nodes, 0, dist_matrix)
    print "Total time taken: ", time.clock() - start, " seconds"


