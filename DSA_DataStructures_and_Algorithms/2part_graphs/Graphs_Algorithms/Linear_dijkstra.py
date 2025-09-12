from collections import deque

def calculate_shortest_paths(graph, start_node):
    num_nodes = len(graph)
    infinity = float("inf")
    distances = [infinity] * num_nodes
    distances[start_node] = 0

    q = deque()
    q.append((start_node, 0))

    while q:
        u, time_left = q.popleft()

        if time_left > 0:
            q.append((u, time_left - 1))
            continue

        for v, cost in graph[u]:
            if distances[v] > distances[u] + cost:
                distances[v] = distances[u] + cost
                q.append((v, cost))

    return distances

graph_data = [
    [(1, 5), (2, 2)],
    [(3, 1), (0, 5), (2, 1)],
    [(0, 2), (1, 1), (3, 7)],
    [(2, 7), (1, 1)]
]

source_node = 2
print( calculate_shortest_paths(graph_data, source_node) )

