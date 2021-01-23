# Helper Code
from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()  # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(
            list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[
            (to_node, from_node)] = distance  # lets make the graph undirected / bidirectional

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)


# my recursive solution
def dijkstra_rec(unvisited, results, node, graph, path):
    min_dist = -1
    to_visit = [n for n in graph.neighbours[node]]
    closest_node = None
    dist_source = results.get(node, 0)
    for n in to_visit:
        dist = graph.distances[(node, n)]
        results[n] = min(results.get(n, dist + dist_source), dist + dist_source)

        if (min_dist == -1 or graph.distances[(node, n)] < min_dist) and n in unvisited:
            min_dist = graph.distances[(node, n)]
            closest_node = n

    path[node] = closest_node

    unvisited.remove(node)
    return unvisited, results, closest_node, graph, path


def dijkstra(graph, source):
    results = {source: 0}
    unvisited = list(graph.nodes)
    dist_source = 0
    path = {}
    node = source
    # Declare and initialize result, unvisited, and path
    # As long as unvisited is non-empty
    while unvisited:
        unvisited, results, node, graph, path = dijkstra_rec(unvisited,
                                                                          results, node, graph, path)
    return results

# udacity solution O(N^2) as well
import sys

'''Find the shortest path from the source node to every other node in the given graph'''


def dijkstra(graph, source):
    result = {}
    result[source] = 0

    for node in graph.nodes:
        if (node != source):
            # he assing to the dict default huge values.
            result[node] = sys.maxsize

    unvisited = set(graph.nodes)

    path = {}

    '''THE GREEDY APPROACH'''
    # As long as unvisited is non-empty
    while unvisited:
        min_node = None

        # 1. Find the unvisited node having smallest known distance from the source node.
        for node in unvisited:
            if node in result:

                if min_node is None:
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break

        # known distance of min_node
        current_distance = result[min_node]

        # 2. For the current node, find all the unvisited neighbours.
        # For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]

                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.
                if ((neighbour not in result) or (distance < result[neighbour])):
                    result[neighbour] = distance

                    # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                    path[neighbour] = min_node

        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result

# Test 1
testGraph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A','B',3)
testGraph.add_edge('A','D',2)
testGraph.add_edge('B','D',4)
testGraph.add_edge('B','E',6)
testGraph.add_edge('B','C',1)
testGraph.add_edge('C','E',2)
testGraph.add_edge('E','D',1)

testGraph.print_graph()
print(dijkstra(testGraph, 'A'))     # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}