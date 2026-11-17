import numpy as np
from collections import deque

class Maze:
    def __init__(self, size, start, end, walls):
        self.size = size
        self.start = start
        self.end = end
        self.maze = np.zeros(size, dtype=str)
        self.maze[:, :] = '.'
        self.maze[start] = 'S'
        self.maze[end] = 'E'
        for wall in walls:
            self.maze[wall] = '#'


    def valid_moves(self, current):
        x, y = current
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check boundaries and walls
            if 0 <= nx < self.size[0] and 0 <= ny < self.size[1]:
                if self.maze[nx, ny] != '#':
                    moves.append((nx, ny))
        return moves

    def extract_path(self, stack):
        for (x, y) in path:
            if (x, y) not in [self.start, self.end]:
                self.maze[x, y] = '*'

    def print_maze(self):
        for row in self.maze:
            print(' '.join(row))

def find_path(maze):
    start = maze.start
    end = maze.end
    stack = [(start, [start])]  # (current_position, path_so_far)
    visited = set([start])

    while stack:
        current, path = stack.pop()

        if current == end:
            return path, len(path) - 1  # found end

        for move in maze.valid_moves(current):
            if move not in visited:
                visited.add(move)
                stack.append((move, path + [move]))

    return None, 0  # no path found

if __name__ == "__main__":
    # Voorbeeld gebruik:
    maze_size = (10, 10)
    start_point = (0, 0)
    end_point = (9, 9)
    walls = [(2, 1), (2, 2), (2, 3), (4, 6), (6, 6), (7, 6), (8, 6), (4, 7), (4, 8),
            (2,2), (5,2), (6,2), (4,2), (3,2), (8,0), (9, 6), (1,8), (2,8), (6,9), (7,9),
            (3,6), (3,7), (4,1), (5,1)]

    my_maze = Maze(maze_size, start_point, end_point, walls)
    my_maze.print_maze()
    print()
    path, steps = find_path(my_maze)

    if path:
        my_maze.extract_path(path)
    my_maze.print_maze()
    print("Path:", path)
    print("Steps:", steps)