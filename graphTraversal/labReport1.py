import random

class Node:
    def __init__(self, x, y, depth=0):
        self.x = x
        self.y = y
        self.depth = depth

class DFS:
    def __init__(self, size):
        self.N = size
        self.grid = [[random.choice(['.', '#']) for _ in range(size)] for _ in range(size)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.source = self._get_empty_cell()
        self.goal = self._get_empty_cell()
        while self.source == self.goal:
            self.goal = self._get_empty_cell()
        self.path = []
        self.visited_order = []
        self.found = False

    def _get_empty_cell(self):
        while True:
            r, c = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if self.grid[r][c] == '.':
                return (r, c)

    def _dfs(self, x, y, visited):
        if (x, y) in visited or self.found:
            return
        visited.add((x, y))
        self.visited_order.append((x, y))
        if (x, y) == self.goal:
            self.found = True
            return
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.N and 0 <= ny < self.N and self.grid[nx][ny] == '.' and (nx, ny) not in visited:
                self._dfs(nx, ny, visited)
                if self.found:
                    self.path.append((nx, ny))
                    return

    def find_path(self):
        visited = set()
        self._dfs(*self.source, visited)
        if self.found:
            self.path.append(self.source)
            self.path.reverse()

    def display_grid(self):
        for r in range(self.N):
            for c in range(self.N):
                if (r, c) == self.source:
                    print('S', end=' ')
                elif (r, c) == self.goal:
                    print('G', end=' ')
                elif (r, c) in self.path:
                    print('*', end=' ')
                else:
                    print(self.grid[r][c], end=' ')
            print()

    def run(self):
        print("Generated Grid:")
        self.find_path()
        self.display_grid()
        print(f"\nSource: {self.source}")
        print(f"Goal: {self.goal}")
        print(f"DFS Path: {self.path}")
        print(f"DFS Traversal Order: {self.visited_order}")

if __name__ == "__main__":
    size = random.randint(4, 7)
    dfs = DFS(size)
    dfs.run()
