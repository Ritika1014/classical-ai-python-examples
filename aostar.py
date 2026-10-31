# AO* Search Algorithm Implementation

inf = float('inf')

# AND-OR Graph
graph = {
    'A': [('B', 'AND'), ('C', 'OR')],
    'B': [('D', 'OR'), ('E', 'OR')],    # AND node: D and E both needed
    'C': [('F', 'OR')],
    'D': [],
    'E': [],
    'F': []
}

# Heuristic cost values (admissible)
h = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 0,
    'E': 0,
    'F': 0
}

# Cost for each edge
cost = {
    ('A', 'B'): 1, ('A', 'C'): 3,
    ('B', 'D'): 1, ('B', 'E'): 1,
    ('C', 'F'): 2
}

solution_graph = {}

def ao_star(n):
    print("Expanding:", n)

    if not graph[n]:   # goal node
        return h[n]

    min_cost = inf
    best_child = None

    # Explore children
    for child, node_type in graph[n]:
        if node_type == 'OR':
            g_cost = cost.get((n, child), inf) + h[child]
        else:
            # AND node: Sum of all children cost
            g_cost = 0
            for c, t in graph[n]:
                g_cost += cost.get((n, c), inf) + h[c]

        if g_cost < min_cost:
            min_cost = g_cost
            best_child = child

    h[n] = min_cost
    solution_graph[n] = best_child

    ao_star(best_child)
    return h[n]


# Run AO*
start = 'A'
print("\n--- AO* Search ---")
final_cost = ao_star(start)
print("\nFinal Cost:", final_cost)
print("Solution Graph:", solution_graph)
