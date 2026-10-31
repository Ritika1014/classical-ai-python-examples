# Best-First Search Implementation (Using Heuristic)

import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristic[start], start))

    while pq:
        cost, node = heapq.heappop(pq)
        print("Visited:", node)

        if node == goal:
            return "Goal Found!"

        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                heapq.heappush(pq, (heuristic[neighbour], neighbour))

    return "Goal Not Found"


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Simple heuristic values
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 7,
    'E': 1,   # goal has lowest heuristic
    'F': 2
}

print("\n--- Best-First Search Traversal ---")
result = best_first_search(graph, 'A', 'F', heuristic)
print(result)
