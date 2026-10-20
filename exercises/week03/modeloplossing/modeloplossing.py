"""
Week 3: oplossingen
===================
Oefening 1: Breadth-First Search
Oefening 2: Sliding Puzzle (8-puzzle)
Oefening 3: Maze met DFS
Oefening 4: Dijkstra
"""

import heapq
from collections import deque

import numpy as np


# =============== Oefening 1: Breadth-First Search ===============


class State:
    """Eenvoudige state met een naam (en PascalCase-alias)."""

    def __init__(self, name: str):
        self.name = name
        self.Name = name  # alias voor compatibiliteit


class Node:
    """Graafnode met een state en een lijst van acties."""

    def __init__(self, state: State):
        self.state = state
        self.State = state  # alias voor compatibiliteit
        self.Actions: list = []

    def add_action(self, action):
        self.Actions.append(action)


def breadth_first_search(initial_node: Node, goal_state: State):
    """BFS met parent-tracking; geeft het pad als lijst van States
    terug, of None als er geen pad bestaat."""
    if initial_node.state.name == goal_state.name:
        return [initial_node.state]

    frontier = deque([initial_node])
    explored = {initial_node}
    parent: dict = {initial_node: None}

    while frontier:
        current = frontier.popleft()
        explored.add(current)
        for kind in current.Actions:
            if kind in explored or kind in parent:
                continue
            parent[kind] = current  # parent van het kind(B) is currentNodeA
            if kind.state.name == goal_state.name:
                # pad reconstrueren via parent-links (backward)
                pad = [kind.state]
                stap = kind
                while parent[stap] is not None:
                    stap = parent[stap]
                    pad.append(stap.state)
                pad.reverse()
                return pad
            frontier.append(kind)
    return None


def print_path(pad: list) -> str:
    """Maak van een lijst van States een leesbare string A -> B -> C."""
    return " -> ".join(state.name for state in pad)


# =============== Oefening 2: Sliding Puzzle ===============


class SlidingPuzzle:
    """8-puzzle (3x3 grid) met getallen 1-8 en een leeg vakje (0)."""

    GRIDSIZE = 3
    EMPTY = 0

    GOAL = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]

    def __init__(self, game):
        self.Game = np.array(game)

    def possible_new_configurations(self) -> list:
        """Alle configuraties na één verschuiving van het lege vakje."""
        configs = []
        row, col = self.locate_empty()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < self.GRIDSIZE and 0 <= c < self.GRIDSIZE:
                nieuw = self.duplicate()
                nieuw.Game[row][col] = nieuw.Game[r][c]
                nieuw.Game[r][c] = self.EMPTY
                configs.append(nieuw)
        return configs

    def locate_empty(self) -> tuple:
        """Geef de (rij, kolom)-positie van het lege vakje."""
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return (row, col)
        raise Exception("Geen leeg vakje!")

    def manhattan_distance(self) -> int:
        """Manhattan-afstand tot de goal-configuratie."""
        doel_positie = {}
        for r in range(self.GRIDSIZE):
            for c in range(self.GRIDSIZE):
                doel_positie[self.GOAL[r][c]] = (r, c)

        totaal = 0
        for r in range(self.GRIDSIZE):
            for c in range(self.GRIDSIZE):
                tegel = self.Game[r][c]
                if tegel == self.EMPTY:
                    continue
                doel_r, doel_c = doel_positie[tegel]
                totaal += abs(r - doel_r) + abs(c - doel_c)
        return totaal

    def is_goal(self) -> bool:
        """True als de configuratie de goal-configuratie is."""
        return self.Game.tolist() == self.GOAL

    def duplicate(self):
        """Maak een diepe kopie van deze puzzel."""
        return SlidingPuzzle(
            [
                [self.Game[r][c] for c in range(self.GRIDSIZE)]
                for r in range(self.GRIDSIZE)
            ]
        )

    def log(self):
        """Print de huidige configuratie."""
        print("---")
        for row in self.Game:
            print(", ".join(str(int(x)) for x in row))
        print("---")


def _puzzel_sleutel(p: SlidingPuzzle) -> tuple:
    """Hashbare sleutel voor een configuratie."""
    return tuple(map(tuple, p.Game.tolist()))


def solve_puzzle(start_puzzle: SlidingPuzzle):
    """BFS over alle configuraties; geeft het pad van configuraties
    terug (start + elke zet), of None als de goal onbereikbaar is."""
    if start_puzzle.is_goal():
        return [start_puzzle]

    frontier = deque([start_puzzle])
    nodes = {_puzzel_sleutel(start_puzzle): start_puzzle}
    parent: dict = {_puzzel_sleutel(start_puzzle): None}
    explored = {_puzzel_sleutel(start_puzzle)}

    while frontier:
        current = frontier.popleft()
        for kind in current.possible_new_configurations():
            k = _puzzel_sleutel(kind)
            if k in explored:
                continue
            explored.add(k)
            parent[k] = _puzzel_sleutel(current)
            nodes[k] = kind
            if kind.is_goal():
                pad = [kind]
                stap = k
                while parent[stap] is not None:
                    stap = parent[stap]
                    pad.append(nodes[stap])
                pad.reverse()
                return pad
            frontier.append(kind)
    return None


# =============== Oefening 3: Maze met DFS ===============


class Maze:
    """Maze op een grid met muren, een start- en een eindpositie."""

    def __init__(self, size, start, end, walls):
        self.size = size
        self.start = start
        self.end = end
        self.maze = np.zeros(size, dtype=str)
        self.maze[:, :] = "."
        self.maze[start] = "S"
        self.maze[end] = "E"
        for wall in walls:
            self.maze[wall] = "#"

    def valid_moves(self, current) -> list:
        """Geef de (rij, kolom)-buren die binnen het grid liggen
        en geen muur zijn."""
        moves = []
        rij, kolom = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = rij + dr, kolom + dc
            if 0 <= r < self.size[0] and 0 <= c < self.size[1]:
                if self.maze[r][c] != "#":
                    moves.append((r, c))
        return moves

    def extract_path(self, stack) -> list:
        """Haal het pad (start tot end) uit de stack als lijst van
        grid-coördinaten."""
        pad = []
        for positie in stack:
            pad.append(positie)
            if positie == self.end:
                break
        return pad

    def print_maze(self):
        """Print het maze."""
        for row in self.maze:
            print(" ".join(str(x) for x in row))


def find_path(maze: Maze):
    """DFS met een stack (LIFO); geeft (pad, stappen) terug waarbij
    pad de lijst coördinaten van start tot end is. Zonder oplossing:
    (None, 0)."""
    stack = [maze.start]
    parent = {maze.start: None}
    visited = {maze.start}

    while stack:
        current = stack.pop()
        if current == maze.end:
            pad = []
            stap = current
            while stap is not None:
                pad.append(stap)
                stap = parent[stap]
            pad.reverse()
            return (pad, len(pad) - 1)
        for buur in maze.valid_moves(current):
            if buur not in visited:
                visited.add(buur)
                parent[buur] = current
                stack.append(buur)
    return (None, 0)


# =============== Oefening 4: Dijkstra ===============


class Edge:
    """Gerichte, gewogen boog tussen twee nodes."""

    def __init__(self, from_node, to_node, cost):
        self.FromNode = from_node
        self.ToNode = to_node
        self.Cost = cost


class Problem:
    """Kortste-pad-probleem met een start- en een goalstate."""

    def __init__(self):
        self.InitialState = None
        self.GoalState = None

    @staticmethod
    def read_from_file(filepath):
        """Lees een graafbestand in en maak er een Problem van."""
        known_nodes = {}
        with open(filepath, "r") as file:
            from_node = file.readline().strip()
            to_node = file.readline().strip()
            initial_node = Problem.get_or_create(known_nodes, from_node)
            goal_node = Problem.get_or_create(known_nodes, to_node)

            for line in file:
                line = line.strip()
                node_name, transitions = line.split(": ")
                node = Problem.get_or_create(known_nodes, node_name)
                transitions_arr = transitions.split(" ")
                for i in range(0, len(transitions_arr), 2):
                    t_name = transitions_arr[i]
                    t_cost = float(transitions_arr[i + 1])
                    t_node = Problem.get_or_create(known_nodes, t_name)
                    node.add_action(Edge(node, t_node, t_cost))

        problem = Problem()
        problem.InitialState = initial_node
        problem.GoalState = goal_node
        return problem

    @staticmethod
    def get_or_create(nodes, node_name):
        """Geef de bestaande node met deze naam of maak een nieuwe."""
        if node_name in nodes:
            return nodes[node_name]
        node = Node(State(node_name))
        nodes[node_name] = node
        return node


class Path:
    """Een pad van nodes met de totale kost."""

    def __init__(self, initial_state):
        self.Nodes = [initial_state]
        self.LeafNode = initial_state
        self.Cost = 0

    def __str__(self):
        node_names = [n.State.Name for n in self.Nodes]
        return "->".join(node_names) + "=" + str(self.Cost)


def dijkstra(problem: Problem):
    """Dijkstra met een priority queue; geeft een Path terug naar de
    goalstate, of None als de goal onbereikbaar is."""
    start_node = problem.InitialState
    goal_node = problem.GoalState

    afstand = {start_node: 0.0}
    parent = {start_node: None}
    visited = set()
    heap = [(0.0, start_node)]

    while heap:
        huidige_kost, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current is goal_node:
            pad = Path(goal_node)
            ketting = []
            stap = current
            while stap is not None:
                ketting.append(stap)
                stap = parent[stap]
            ketting.reverse()
            pad.Nodes = ketting
            pad.LeafNode = goal_node
            pad.Cost = huidige_kost
            return pad
        for edge in current.Actions:
            buur = edge.ToNode
            nieuwe_kost = huidige_kost + edge.Cost
            if buur not in visited and nieuwe_kost < afstand.get(buur, float("inf")):
                afstand[buur] = nieuwe_kost
                parent[buur] = current
                heapq.heappush(heap, (nieuwe_kost, buur))
    return None


if __name__ == "__main__":
    # ---- Oefening 1: BFS ----
    node_a = Node(State("A"))
    node_b = Node(State("B"))
    node_c = Node(State("C"))
    node_d = Node(State("D"))
    node_e = Node(State("E"))
    node_f = Node(State("F"))
    node_h = Node(State("H"))
    node_a.add_action(node_b)
    node_a.add_action(node_c)
    node_b.add_action(node_d)
    node_b.add_action(node_e)
    node_c.add_action(node_f)
    node_f.add_action(node_h)
    bfs_pad = breadth_first_search(node_a, node_h.state)
    print("BFS-pad:", print_path(bfs_pad) if bfs_pad else "geen pad")

    # ---- Oefening 2: Sliding Puzzle ----
    puzzle = SlidingPuzzle([[1, 2, 3], [4, 5, 0], [7, 8, 6]])
    oplossing = solve_puzzle(puzzle)
    print("Zetten:", len(oplossing) - 1 if oplossing else "geen oplossing")

    # ---- Oefening 3: Maze met DFS ----
    muren = [
        (2, 1),
        (2, 2),
        (2, 3),
        (4, 6),
        (6, 6),
        (7, 6),
        (8, 6),
        (4, 7),
        (4, 8),
        (5, 2),
        (6, 2),
        (4, 2),
        (3, 2),
        (8, 0),
        (9, 6),
        (1, 8),
        (2, 8),
        (6, 9),
        (7, 9),
        (3, 6),
        (3, 7),
        (4, 1),
        (5, 1),
    ]
    mijn_maze = Maze((10, 10), (0, 0), (9, 9), muren)
    maze_pad, stappen = find_path(mijn_maze)
    print("Maze-pad:", maze_pad)
    print("Stappen:", stappen)

    # ---- Oefening 4: Dijkstra ----
    n_a = Node(State("A"))
    n_b = Node(State("B"))
    n_c = Node(State("C"))
    n_a.Actions = [Edge(n_a, n_b, 2.0), Edge(n_a, n_c, 3.0)]
    n_b.Actions = [Edge(n_b, n_c, 1.0)]
    n_c.Actions = []
    probleem = Problem()
    probleem.InitialState = n_a
    probleem.GoalState = n_c
    print("Kortste pad:", dijkstra(probleem))
