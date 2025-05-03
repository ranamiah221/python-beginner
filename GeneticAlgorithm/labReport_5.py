import random

class QueenSolver:
    def __init__(self, board_size=8, group_size=100, tweak_chance=0.05, max_steps=1000):
        self.size = board_size
        self.group = [self.make_board() for _ in range(group_size)]
        self.group_size = group_size
        self.tweak_chance = tweak_chance
        self.max_steps = max_steps

    def make_board(self):
        setup = list(range(self.size))
        random.shuffle(setup)
        return setup

    def count_attacks(self, setup):
        clash = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if abs(setup[i] - setup[j]) == abs(i - j):
                    clash += 1
        return clash

    def pick_parents(self):
        part = random.sample(self.group, 5)
        part.sort(key=lambda s: self.count_attacks(s))
        return part[0], part[1]

    def mix_boards(self, one, two):
        split = random.randint(1, self.size - 2)
        new_one = one[:split] + [q for q in two if q not in one[:split]]
        return new_one

    def tweak(self, board):
        if random.random() < self.tweak_chance:
            a, b = random.sample(range(self.size), 2)
            board[a], board[b] = board[b], board[a]
        return board

    def solve(self):
        for step in range(self.max_steps):
            self.group.sort(key=lambda s: self.count_attacks(s))
            if self.count_attacks(self.group[0]) == 0:
                print(f"Success at step {step}")
                return self.group[0]

            next_group = self.group[:20]  
            while len(next_group) < self.group_size:
                p1, p2 = self.pick_parents()
                child = self.mix_boards(p1, p2)
                child = self.tweak(child)
                next_group.append(child)

            self.group = next_group

        print("Couldn't find a clean layout.")
        return None

if __name__ == "__main__":
    task = QueenSolver(board_size=8)
    result = task.solve()
    if result:
        print("Queen positions:", result)
