from collections import deque

class BFS:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        self.found = False  # Flag indicating if the goal was found
        self.goal_level = 0  # Level at which the goal is found
        self.N = 0  # Grid size (assumes a square grid)

    def init(self):
        # Define the grid: 1 = walkable, 0 = wall
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]

        self.N = len(graph)

        # Define source and goal positions
        source = (0, 2, 0)  # (x, y, level)
        goal = (4, 4)

        # Start the BFS search
        self.st_bfs(graph, source, goal)

        # Output the result
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal_level)
        else:
            print("Goal cannot be reached from starting block")

    def st_bfs(self, graph, source, goal):
        queue = deque()
        queue.append(source)

        while queue:
            x, y, level = queue.popleft()  # Remove node from front of queue

            # Explore neighbors in all four directions
            for dx, dy in self.directions:
                v_x, v_y = x + dx, y + dy

                # Check boundaries and if cell is walkable (1)
                if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                    v_level = level + 1  # One move further

                    # Check if we've reached the goal
                    if (v_x, v_y) == goal:
                        self.found = True
                        self.goal_level = v_level
                        return

                    # Mark the cell as visited (prevent revisiting)
                    graph[v_x][v_y] = 0

                    # Add neighbor node to the queue
                    queue.append((v_x, v_y, v_level))

# Run the BFS
if __name__ == "__main__":
    bfs = BFS()
    bfs.init()
