def a_star(graph, h, start, goal):
    open_list = [start]
    closed_list = []

    g = {node: float('inf') for node in graph}
    g[start] = 0

    f = {node: float('inf') for node in graph}
    f[start] = h[start]

    parent = {start: None}

    while open_list:
        # Select node with minimum f(n)
        current = min(open_list, key=lambda x: f[x])
        print("Visited:", current)

        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return list(reversed(path))

        open_list.remove(current)
        closed_list.append(current)

        # Explore neighbours
        for neighbour, cost in graph[current]:
            if neighbour in closed_list:
                continue

            temp_g = g[current] + cost

            if neighbour not in open_list:
                open_list.append(neighbour)

            # If better path found
            if temp_g < g[neighbour]:
                parent[neighbour] = current
                g[neighbour] = temp_g
                f[neighbour] = g[neighbour] + h[neighbour]

    return None


# Graph with cost values
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

# Heuristic values
h = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 2,
    'E': 0,   # goal h=0
    'F': 4
}

print("\n--- A* Search ---")
path = a_star(graph, h, 'A', 'E')
print("Optimal Path:", path)
