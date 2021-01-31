import math

# Helper Class
class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance

# Helper Classes
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)

class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    # adds an edge between node1 and node2 in both directions
    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

# my solution, is working but a need 2 dedicated items
class QueueElement(object):
    def __init__(self, Node, distance):
        self.node = Node
        self.distance = distance

class PriorityQueue(object):
    def __init__(self):
        self.component = [] #of QueueElement

    def isEmpty(self):
        return len(self.component) == 0

    def size(self):
        return len(self.component)

    def push(self, node, distance):
        element = QueueElement(node, distance)
        self.component.append(element)# here distance is the distance from start

    def update(self, node, distance):
        for element in self.component:
            if element.node == node and distance < element.distance:
                element.distance = distance

    def return_distance(self, node):
        for element in self.q:
            if element.node == node:
                return element.distance

    def pop(self):
        if len(self.component)> 0:
            max = 0
            for i in range(len(self.component)):
                # overriding priority implementation for nodes
                if self.component[i].distance < self.component[max].distance:
                    max = i
            element = self.component[max]
            del self.component[max]
            return element
        else:
            return None


def dijkstra(graph, start_node, end_node):
    q = PriorityQueue()
    q.push(start_node, 0)
    for node in graph.nodes:
        if node != start_node:
            q.push(node, math.inf)

    while q.size() > 0:  # Repeat until the stack is empty
        element = q.pop()  # Pop out a node added recently
        current_node, start_distance = element.node, element.distance
        if current_node == end_node:
            return start_distance

        for child in current_node.edges:
            child_start_distance = child.distance + start_distance
            q.update(child.node, child_start_distance)

        if current_node == end_node:
            return current_node

# udacity solution, using a dictionary, access to end node is faster
import math  # Need math.inf constant


def dijkstra(graph, start_node, end_node):
    # Create a dictionary that stores the distance to all nodes in the form of node:distance as key:value
    # Assume the initial distance to all nodes is infinity.
    # Use math.inf as a predefined constant equal to positive infinity
    distance_dict = {node: math.inf for node in graph.nodes}

    # Build a dictionary that will store the "shortest" distance to all nodes, wrt the start_node
    shortest_distance = {}

    distance_dict[start_node] = 0

    while distance_dict:

        # Sort the distance_dict, and pick the key:value having smallest distance
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]

        # Remove the current node from the distance_dict, and store the same key:value in shortest_distance
        shortest_distance[current_node] = distance_dict.pop(current_node)

        # Check for each neighbour of current_node, if the distance_to_neighbour is smaller than the alreday stored distance, update the distance_dict
        for edge in current_node.edges:
            if edge.node in distance_dict:

                distance_to_neighbour = node_distance + edge.distance
                if distance_dict[edge.node] > distance_to_neighbour:
                    distance_dict[edge.node] = distance_to_neighbour

    return shortest_distance[end_node]


# Test Case 1:

# Create a graph
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])

# add_edge() function will add an edge between node1 and node2 in both directions
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_y, 5)

# Shortest Distance from U to Y is 14
print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(graph, node_u, node_y)))

# Test Case 2
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')

graph = Graph([node_A, node_B, node_C])

graph.add_edge(node_A, node_B, 5)
graph.add_edge(node_B, node_C, 5)
graph.add_edge(node_A, node_C, 10)

# Shortest Distance from A to C is 10
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph, node_A, node_C)))

# Test Case 3
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')
node_D = GraphNode('D')
node_E = GraphNode('E')

graph = Graph([node_A, node_B, node_C, node_D, node_E])

graph.add_edge(node_A, node_B, 3)
graph.add_edge(node_A, node_D, 2)
graph.add_edge(node_B, node_D, 4)
graph.add_edge(node_B, node_E, 6)
graph.add_edge(node_B, node_C, 1)
graph.add_edge(node_C, node_E, 2)
graph.add_edge(node_E, node_D, 1)

# Shortest Distance from A to C is 4
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph, node_A, node_C)))