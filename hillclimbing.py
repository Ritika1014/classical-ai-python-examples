import random

# Objective function to maximize
def f(x):
    return -(x - 3)**2 + 10

# Hill Climbing
def hill_climbing():
    # Step 1: Start with a random point
    current_x = random.uniform(-10, 10)
    step_size = 0.1

    while True:
        # Step 2: Generate neighbors
        neighbors = [current_x + step_size, current_x - step_size]

        # Step 3: Pick best neighbor
        best_neighbor = max(neighbors, key=f)

        # Step 4: Check improvement
        if f(best_neighbor) > f(current_x):
            current_x = best_neighbor  # Move to better neighbor
        else:
            break  # No improvement → stop

    return current_x, f(current_x)

# Run
best_x, best_value = hill_climbing()
print("Best x:", best_x)
print("Best value:", best_value)
