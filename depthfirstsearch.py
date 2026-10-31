# Depth-First Search (DFS) Implementation

def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        print("Visited:", node)

        if node == goal:
            return "Goal Found!"

        if node not in visited:
            visited.add(node)
            # reversed() ensures left-to-right traversal
            for neighbour in reversed(graph[node]):
                stack.append(neighbour)

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

print("\n--- DFS Traversal ---")
result = dfs(graph, 'A', 'E')
print(result)
