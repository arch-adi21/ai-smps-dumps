from collections import deque

class BucketState:
    """
    Represents the current amount of water in each bucket.
    """
    def __init__(self, x, y, z):
        self.x = x  # Water in 8L bucket
        self.y = y  # Water in 5L bucket
        self.z = z  # Water in 3L bucket

    def is_goal(self):
        """
        Check if any bucket has exactly 4 liters.
        """
        return self.x == 4 or self.y == 4 or self.z == 4

    def __repr__(self):
        """
        Return a string representation of the state.
        """
        return f"({self.x}, {self.y}, {self.z})"


def get_next_states(state):
    """
    Generate all possible states by pouring water between buckets.
    """
    x, y, z = state.x, state.y, state.z
    capacities = (8, 5, 3)  # Maximum capacity of each bucket
    next_states = []

    # Pour water from one bucket to another
    # Pour from x to y
    pour = min(x, capacities[1] - y)  # Amount we can pour
    next_states.append(BucketState(x - pour, y + pour, z))

    # Pour from x to z
    pour = min(x, capacities[2] - z)
    next_states.append(BucketState(x - pour, y, z + pour))

    # Pour from y to x
    pour = min(y, capacities[0] - x)
    next_states.append(BucketState(x + pour, y - pour, z))

    # Pour from y to z
    pour = min(y, capacities[2] - z)
    next_states.append(BucketState(x, y - pour, z + pour))

    # Pour from z to x
    pour = min(z, capacities[0] - x)
    next_states.append(BucketState(x + pour, y, z - pour))

    # Pour from z to y
    pour = min(z, capacities[1] - y)
    next_states.append(BucketState(x, y + pour, z - pour))

    return next_states


def solve(initial_state):
    """
    Solve the problem using Breadth-First Search (BFS).
    """
    queue = deque([(initial_state, [])])  # (current state, path to reach it)
    visited = set()  # To track visited states

    while queue:
        current_state, path = queue.popleft()

        # Check if the goal is reached
        if current_state.is_goal():
            return path + [current_state]

        # Avoid revisiting states
        if (current_state.x, current_state.y, current_state.z) in visited:
            continue
        visited.add((current_state.x, current_state.y, current_state.z))

        # Add all possible next states to the queue
        for next_state in get_next_states(current_state):
            if (next_state.x, next_state.y, next_state.z) not in visited:
                queue.append((next_state, path + [current_state]))

    return None  # No solution found


# Main Program
initial_state = BucketState(8, 0, 0)  # Start with 8L in the first bucket
solution = solve(initial_state)

if solution:
    print("Solution:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
