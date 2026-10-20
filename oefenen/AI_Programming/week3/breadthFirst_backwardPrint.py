from collections import deque

class State:
    def __init__(self, name):
        self.name = name

class Node:
    def __init__(self, state):
        self.state = state
        self.actions = []
        self.parent = None

    def add_action(self, action):
        self.actions.append(action)

def breadth_first_search(initial_node, goal_state):
    frontier = deque([initial_node]) # verzameling van NODES
    visited = set() # deze bevat STATES

    while frontier:
        current_node = frontier.popleft()

        if (current_node.state == goal_state):
            return current_node
        
        visited.add(current_node.state)

        for neighbor_node in current_node.actions:
            if (neighbor_node not in frontier) and (neighbor_node.state not in visited):
                neighbor_node.parent = current_node # pijltje achteruit zetten
                frontier.append(neighbor_node) # essentieel dat dit een queue is

    return None

    
# Example usage
if __name__ == "__main__":
    # Create states
    state_a = State("A")
    state_b = State("B")
    state_c = State("C")
    state_d = State("D")
    state_e = State("E")
    state_f = State("F")
    state_h = State("H")

    # Create nodes and actions
    node_a = Node(state_a)
    node_b = Node(state_b)
    node_c = Node(state_c)
    node_d = Node(state_d)
    node_e = Node(state_e)
    node_f = Node(state_f)
    node_h = Node(state_h)

    node_a.add_action(node_b)
    node_a.add_action(node_c)
    node_b.add_action(node_d)
    node_b.add_action(node_e)
    node_c.add_action(node_f)
    node_f.add_action(node_h)

    # Perform breadth-first search
    goal_state = state_h
    solution_node = breadth_first_search(node_a, goal_state)

    if solution_node:
        print("Solution found! Goal state:", solution_node.state.name)
        print("Backward solution path: ")
        while solution_node.parent:
            solution_node = solution_node.parent
            print("Parent: ", solution_node.state.name)
    else:
        print("Solution not found.")
