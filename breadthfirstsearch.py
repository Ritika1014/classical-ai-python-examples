# Breadth-First Search (BFS) Implementation

from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print("Visited:", node)

        if node == goal:
            return "Goal Found!"

        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                queue.append(neighbour)

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

print("\n--- BFS Traversal ---")
result = bfs(graph, 'A', 'E')
print(result)
