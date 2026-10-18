"""
Oefening 2: Sliding Puzzle (8-puzzle)
======================================
Implementeer de sliding puzzle en los hem op met BFS/DFS.
"""

import numpy as np


class SlidingPuzzle:
    GRIDSIZE = 3
    EMPTY = 0

    GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __init__(self, game):
        self.Game = np.array(game)

    def possible_new_configurations(self):
        rij, kol = self.locate_empty()
        conf_list = []
        # omhoog
        if rij > 0:
            kopie = self.duplicate()
            kopie.Game[rij][kol] = self.Game[rij - 1][kol]
            conf_list.append(kopie)

        # omlaag
        if rij < self.GRIDSIZE - 1:
            kopie = self.duplicate()
            kopie.Game[rij][kol] = self.Game[rij + 1][kol]
            conf_list.append(kopie)

        # rechts
        if kol > 0:
            kopie = self.duplicate()
            kopie.Game[rij][kol] = self.Game[rij][kol - 1]
            conf_list.append(kopie)

        # links
        if kol < self.GRIDSIZE - 1:
            kopie = self.duplicate()
            kopie.Game[rij][kol] = self.Game[rij][kol + 1]
            conf_list.append(kopie)

        return conf_list

    def locate_empty(self):
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return (row, col)
        raise Exception("Geen leeg vakje!")

    def manhattan_distance(self):
        # TODO: bereken de Manhattan-afstand tot de goal-configuratie
        return 0

    def is_goal(self):
        return np.array_equal(self.Game, self.GOAL)

    def duplicate(self):
        return SlidingPuzzle(
            [
                [self.Game[r][c] for c in range(self.GRIDSIZE)]
                for r in range(self.GRIDSIZE)
            ]
        )

    def log(self):
        print("---")
        for row in self.Game:
            print(", ".join(str(int(x)) for x in row))
        print("---")


def solve_puzzle(start_puzzle):
    # TODO: los de puzzel op met BFS
    pass


if __name__ == "__main__":
    game = [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
    puzzle = SlidingPuzzle(game)
    print("Startconfiguratie:")
    puzzle.log()

    # oplossing = solve_puzzle(puzzle)
    # print("Oplossing:", oplossing)

    puzzle.possible_new_configurations()


# bfs fifo
# dfs lifo
