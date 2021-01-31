'''
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
Input parameters explanation:

1. Number of islands = 4
2. Island 1 and 2 are connected via a bridge with cost = 1
   Island 2 and 3 are connected via a bridge with cost = 4
   Island 1 and 4 are connected via a bridge with cost = 3
   Island 4 and 3 are connected via a bridge with cost = 2
   Island 1 and 3 are connected via a bridge with cost = 10

Step 1 - Create a Graph

Create a graph with given number of islands, and the cost between each pair of islands. A graph can be represented as a adjacency_matrix, which is a list of lists. For example, given:
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]

The graph would look like:
graph =  [[], [(2, 1), (4, 3), (3, 10)], [(1, 1), (3, 4)], [(2, 4), (4, 2), (1, 10)], [(1, 3), (3, 2)]]
where, a sublist at  𝑖𝑡ℎ  index represents the adjacency_list of  𝑖𝑡ℎ  island. A tuple within a sublist is (neighbor, edge_cost).

Step 2 - Traverse the graph in a Greedy way.
Traverse the graph in a Greedy way.
Create a blank minHeap, and push any one island (vertex) into it.
While there are elements remaining in the minHeap, do the following:

Pop out an island having smallest edge_cost, and reduce the heap size. You can use heapq.heappop() for this purpose.
If the current island has not been visited before, add the edge_cost to the total_cost. You can use a list of booleans to keep track of the visited islands.
Find out all the neighbours of the current island from the given graph. Push each neighbour of the current island into the minHeap. You can use heapq.heappush() for this purpose.
Mark current island as visited tuple in the adjacency_list of the
When we have popped out all the elements from the minHeap, we will have the minimum total_cost to visit all the islands.

'''


def create_graph(config, num_islands):
    graph = [[]]*(num_islands+1)
    for c in config:
        idx = c[0]
        list_to_extend = graph[idx]
        if list_to_extend:
            list_to_extend.append((c[1], c[2]))
        else:
            list_to_extend = [(c[1], c[2])]
        graph[idx] = list_to_extend

    for c in config:
        idx = c[1]
        list_to_extend = graph[idx]
        if list_to_extend:
            list_to_extend.append((c[0], c[2]))
        else:
            list_to_extend = [(c[0], c[2])]
        graph[idx] = list_to_extend

    return graph


print(create_graph([[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]], 4))

"""
:param: num_islands - number of islands
:param: bridge_config - bridge configuration as explained in the problem statement
return: cost (int) minimum cost of connecting all islands
TODO complete this method to returh minimum cost of connecting all islands
"""
# Solution

# The following Solution makes use of one of Python's PriorityQueue implementation (heapq)
# For more details - https://thomas-cokelaer.info/tutorials/python/module_heapq.html
import heapq


def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    # A graph can be represented as a adjacency_list, which is a list of blank lists
    graph = [list() for _ in range(num_islands + 1)]

    # populate the adjacency_list
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]

        # An entry in a sublist of graph is represented as a tuple (neighbor, edge_cost)
        graph[source].append((destination, cost))
        graph[destination].append((source, cost))

    # Try this: print("graph = ",graph)
    return graph


def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """

    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # Heap is represented as a list of tuples
    # A "node" in heap is represented as tuple (edge_cost, neighbor)
    minHeap = [(0, start_vertex)]
    total_cost = 0

    while len(minHeap) > 0:
        # Here, heapq.heappop() will automatically pop out the "node" having smallest edge_cost, and reduce the heap size
        cost, current_vertex = heapq.heappop(minHeap)

        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue # skip current loop

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(minHeap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)