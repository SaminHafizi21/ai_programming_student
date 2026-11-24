import numpy as np
import random
import math

class SudokuSASolver:
    def __init__(self, puzzle, initial_temp=10.0, alpha=0.99, max_iter=2000):
        self.initial_puzzle = np.array(puzzle)
        self.initial_temp = initial_temp
        self.alpha = alpha
        self.max_iter = max_iter
        
        self.grid = None
        self.fixed = None
        self.current_cost = None

    def _get_block_indices(self, block_idx):
        """Hardcoded lookup mapping: elke 2x2 blok krijgt exacte coördinaten terug."""
        blocks = {
            0: [(0,0), (0,1), (1,0), (1,1)],  # Boven-links blok
            1: [(0,2), (0,3), (1,2), (1,3)],  # Boven-rechts blok
            2: [(2,0), (2,1), (3,0), (3,1)],  # Onder-links blok
            3: [(2,2), (2,3), (3,2), (3,3)]   # Onder-rechts block
        }
        return blocks[block_idx]

    def _initialize_grid(self):
        """Vult lege plaatsen zpdat elke 2x2 blok begint met getallen 1-4."""
        self.grid = self.initial_puzzle.copy()
        self.fixed = self.initial_puzzle != 0
        
        for b in range(4):
            indices = self._get_block_indices(b)
            present = [self.grid[r, c] for r, c in indices if self.grid[r, c] != 0]
            missing = [val for val in [1, 2, 3, 4] if val not in present]
            random.shuffle(missing)
            
            for r, c in indices:
                if self.grid[r, c] == 0:
                    self.grid[r, c] = missing.pop()

    def _compute_cost(self, test_grid):
        """Telt hoeveel duplicates er zijn in rijen en kolommen (Perfect = 0). Hoe lager, hoe beter."""
        cost = 0
        for i in range(4):
            cost += (4 - len(np.unique(test_grid[i, :]))) # duplicaten per rij
            cost += (4 - len(np.unique(test_grid[:, i]))) # duplicaten per kolom
        return cost

    def _get_neighbor(self):
        """Swaps two non-clue numbers within a random 2x2 block."""
        new_grid = self.grid.copy()
        b = random.randint(0, 3)
        indices = self._get_block_indices(b)
        
        mutable = [(r, c) for r, c in indices if not self.fixed[r, c]]
        
        if len(mutable) >= 2:
            (r1, c1), (r2, c2) = random.sample(mutable, 2)
            new_grid[r1, c1], new_grid[r2, c2] = new_grid[r2, c2], new_grid[r1, c1]
            
        return new_grid

    def solve(self):
        """Dit algoritme zoekt een oplossing van de sudoku, of een goede benadering van een oplossing."""
        self._initialize_grid()
        self.current_cost = self._compute_cost(self.grid)
        T = self.initial_temp
        T *= self.alpha
        
        grid = self.grid
        best_grid = grid
        
        for k in range(self.max_iter):
            
            new_grid = self._get_neighbor()
            
            if self._compute_cost(new_grid) < self._compute_cost(grid):
                grid = new_grid
            else:
                delta = self._compute_cost(new_grid) - self._compute_cost(grid)
                P = math.exp(-delta/T)
                
                if random.random() < P:
                    grid = new_grid
            
            

             #TODO Voorzie een check om vroegtijdig te stoppen als er een echte oplossing wordt gevonden
            if self._compute_cost(grid) == 0:
                best_grid = grid
            
            if k % 10 == 0:
                print(f"{k} current grid cost: {self._compute_cost(grid)}, best grid cost: {self._compute_cost(best_grid)}")
            

        return best_grid


        #TODO print relevante outputs
        print("Reached max iterations without a perfect solution.")
        # return self.grid


# --- Running the Code ---
if __name__ == "__main__":
    puzzle_data = [
        [1, 0, 0, 4],
        [0, 4, 1, 0],
        [2, 0, 4, 0],
        [0, 3, 0, 1]
    ]  # 0 = lege cel; deze puzzel heeft exact één oplossing

    solver = SudokuSASolver(puzzle_data, initial_temp=10.0, alpha=0.99, max_iter=2000)
    solved_board = solver.solve()
    #TODO print de oplossing
