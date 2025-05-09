class IDDFSMazeSolver:
    def __init__(self):
        self.rows = self.cols = 0
        self.maze = []
        self.visited = []
        self.path = []
        self.goal_found = False
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] == 0

    def dls(self, x, y, goal_x, goal_y, depth):
        if (x, y) == (goal_x, goal_y):
            self.path.append((x, y))
            self.goal_found = True
            return True

        if depth == 0:
            return False

        self.visited[x][y] = True
        self.path.append((x, y))

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny) and not self.visited[nx][ny]:
                if self.dls(nx, ny, goal_x, goal_y, depth - 1):
                    return True

        self.path.pop()  # backtrack
        self.visited[x][y] = False
        return False

    def iddfs(self, start_x, start_y, goal_x, goal_y):
        max_depth = self.rows * self.cols
        for depth in range(max_depth + 1):
            self.visited = [[False] * self.cols for _ in range(self.rows)]
            self.path = []
            if self.dls(start_x, start_y, goal_x, goal_y, depth):
                print(f"✅ Path found at depth {depth}")
                print(f"🧭 Traversal Path: {self.path}")
                return True
        print(f"❌ No path found within depth {max_depth}")
        return False

    def solve_maze(self):
        try:
            self.rows, self.cols = map(int, input("Enter maze dimensions (rows cols): ").split())
            print("Enter maze rows (0 = open, 1 = wall):")
            self.maze = [list(map(int, input().split())) for _ in range(self.rows)]

            start_x, start_y = map(int, input("Enter start coordinates (x y): ").split())
            goal_x, goal_y = map(int, input("Enter goal coordinates (x y): ").split())

            if not self.is_valid(start_x, start_y) or not self.is_valid(goal_x, goal_y):
                print("⚠️ Invalid start or goal position (either wall or out of bounds)")
                return

            self.iddfs(start_x, start_y, goal_x, goal_y)

        except Exception as e:
            print(f"❗ Error: {e}")

if __name__ == "__main__":
    IDDFSMazeSolver().solve_maze()
