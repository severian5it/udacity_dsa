import math
import heapq


def distance(x, y):
    """Return euclidean distance between 2 bidimensional point
    Args:
        x: first point, with 2 coordinates
        y: secong point, with 2 coordinates
    Returns:
        distance as float
    """
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))


def build_path(prev_node, start, goal):
    """Return euclidean distance between 2 bidimensional point
    Args:
        prev_node: dictionary, with the node we came from
        start: start node
        goal: end node
    Returns:
        path as a list
    """
    path = [goal]
    prev = goal
    while prev != start:
        prev = prev_node[prev]
        path.append(prev)

    return path[::-1]


def shortest_path(M, start, goal):
    """Find the shortest path via A*, using extimated cost in priority Queue
    Args:
        M: Graph
        start: start node
        goal: end node
    Returns:
        path as a list
    """
    frontier = []  # frontier will be priority queue
    heapq.heappush(frontier, (0, start))  # first
    goal_coo = M.intersections[goal]

    prev_node = {}
    cost = {}
    prev_node[start] = None
    cost[start] = 0

    while not len(frontier) == 0:
        current = heapq.heappop(frontier)[1]
        current_coo = M.intersections[current]

        if current == goal:
            break

        for next in M.roads[current]:
            next_coo = M.intersections[next]
            new_cost = cost.get(current, 0) + distance(current_coo, next_coo)

            if next not in cost or new_cost < cost[next]:
                cost[next] = new_cost
                priority = new_cost + distance(next_coo, goal_coo)
                heapq.heappush(frontier, (priority, next))
                prev_node[next] = current

    return build_path(prev_node, start, goal)