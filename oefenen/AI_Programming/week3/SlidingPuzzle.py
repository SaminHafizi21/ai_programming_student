from collections import deque
import time

class Configuration: # abstracte klasse voor puzzels en simpele spellen
    def cost(self):
        pass

    def possible_new_configurations(self):
        pass

    def log(self):
        pass

class SlidingPuzzle(Configuration):
    GRIDSIZE = 3
    EMPTY = 0

    def __init__(self, game):
        # game is typisch een Gridsize-op-Gridsize array met waardes van de puzzel.
        self.Game = game 

    def cost(self):
        # totale kost van het bord
        total = 0
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                value = self.Game[row][col]
                if value != self.EMPTY:
                    goal_row = (value - 1) // self.GRIDSIZE
                    goal_col = (value - 1) % self.GRIDSIZE
                    total += self.tile_cost(goal_row, goal_col, row, col)
        return total

    def tile_cost(self, goal_row, goal_col, row, col):
        # cost om 1 tegel op zijn plaats te krijgen
        return abs(goal_row - row) + abs(goal_col - col)
        

    def possible_new_configurations(self):
        #geef een array terug van alle nieuwe mogelijke spelposities vanaf hier (transities)
        configs = []
        empty_row, empty_col = self.locate_empty()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            new_r, new_c = empty_row + dr, empty_col + dc
            if self.can_move_to(new_r, new_c):
                new_game = self.duplicate()
                #swap
                new_game[empty_row][empty_col], new_game[new_r][new_c] = new_game[new_r][new_c], new_game[empty_row][empty_col]
                configs.append(SlidingPuzzle(new_game))
        return configs

    def can_move_to(self, row, col):
        # check of naar deze rij kan worden gemoved
        return 0 <= row < self.GRIDSIZE and 0 <= col < self.GRIDSIZE

    def locate_empty(self):
        # geef de locatie terug van het lege vakje
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return [row, col]
        raise Exception("Something went wrong!")

    def duplicate(self):
        new_game = [[self.Game[row][col] for col in range(self.GRIDSIZE)] for row in range(self.GRIDSIZE)]
        return new_game

    def log(self):
        print("---")
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                print(self.Game[row][col], end=", ")
            print()
        print("---")

    def is_goal(self):
        goal = [[(r * self.GRIDSIZE + c + 1) % (self.GRIDSIZE ** 2)
                for c in range(self.GRIDSIZE)]
                for r in range(self.GRIDSIZE)]
        return self.Game == goal
    
    def as_tuple(self):
        return tuple(tuple(row) for row in self.Game)

def breadth_first_search(start_puzzle):
    queue = deque([(start_puzzle, [])])  # (state, path)
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current.as_tuple() in visited:
            continue
        visited.add(current.as_tuple())

        if current.is_goal():
            return path + [current]

        for neighbor in current.possible_new_configurations():
            queue.append((neighbor, path + [current]))

    return None  # no solution found

if __name__ == "__main__":
    # game = [ # een voorbeeld van een simpele puzzel
    #     [1, 2, 3],
    #     [4, 5, 0],
    #     [7, 8, 6]
    # ]
    # game = [
    # [1, 2, 3],
    # [4, 5, 6],
    # [0, 7, 8]
    # ]
    # game = [
    # [1, 2, 3],
    # [5, 0, 6],
    # [4, 7, 8]
    # ]
    # game = [
    # [7, 2, 4],
    # [5, 0, 6],
    # [8, 3, 1]
    # ]
    # game = [
    # [1, 2, 3],
    # [4, 5, 6],
    # [8, 7, 0]
    # ]
    game = [
        [0,1,3],
        [4,5,8],
        [7,2,6]
    ]

    puzzle = SlidingPuzzle(game)

    print("Original:")
    puzzle.log()

    solution = breadth_first_search(puzzle)

    if solution:
        print(f"Solved in {len(solution)-1} moves!")
        for step in solution:
            step.log()
            #time.sleep(1)
    else:
        print("No solution found.")
    
