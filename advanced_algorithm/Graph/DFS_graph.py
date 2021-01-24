class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)


# my solution, I need to add a graph, but it seems to work.
def dfs_search(graph, root_node, search_value):
    visited = []
    while visited != graph.nodes:
        next_node = None
        for c in root_node.children:
            if c.value == search_value:
                return c
            if c not in visited:
                next_node = c

        if next_node is None:
            next_node = visited.pop()

        visited.append(root_node)
        root_node = next_node

    return -1

assert nodeA == dfs_search(graph1, nodeA, 'A')
assert nodeS == dfs_search(graph1, nodeP, 'S')
assert nodeR == dfs_search(graph1, nodeH, 'R')

# udacity solution
def dfs_search(root_node, search_value):
    visited = set()  # Sets are faster for lookups
    stack = [root_node]  # Start with a given root node

    while len(stack) > 0:  # Repeat until the stack is empty

        current_node = stack.pop()  # Pop out a node added recently
        visited.add(current_node)  # Mark it as visited

        if current_node.value == search_value:
            return current_node

        # Check all the neighbours
        for child in current_node.children:

            # If a node hasn't been visited before, and not available in the stack already.
            if (child not in visited) and (child not in stack):
                stack.append(child)


assert nodeA == dfs_search(nodeA, 'A')
assert nodeS == dfs_search(nodeP, 'S')
assert nodeR == dfs_search(nodeH, 'R')