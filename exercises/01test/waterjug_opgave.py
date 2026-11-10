from collections import deque


class WaterJugState:
    def __init__(self, jug8, jug5, jug3):
        self.jug8 = jug8
        self.jug5 = jug5
        self.jug3 = jug3
        self.parent = None

    def __eq__(self, other):
        #deze krijg je cadeau, zodat python kan checken of twee states hetzelfde zijn
        return self.jug8 == other.jug8 and self.jug5 == other.jug5 and self.jug3 == other.jug3

    def __hash__(self):
        return hash((self.jug8, self.jug5, self.jug3))
    
    def is_valid_state(self):
        
        if self.jug3 > 3: 
            return False
        if self.jug5 > 5: 
            return False
        if self.jug8 > 8: 
            return False
        


            
        return True
        
    
    def get_next_states(self):
        next_states = []
        
        
        # for state in [WaterJugState(8,5,3), (3,5,0), WaterJugState(4,4,0), WaterJugState(0,0,0), WaterJugState(8,4,1), WaterJugState(7,5,1), WaterJugState(5, 5, 2)]:
        for state in [(8,5,3), (3,5,0), (4,4,0), (0,0,0), (8,4,1), (7,5,1), (5, 5, 2)]:
            
            
            if not self.is_valid_state():
                continue
            else:
                next_states.append(state)
                self.jug8, self.jug5, self.jug3 = state

        return next_states

        # Mogelijke acties: 
        # vul jug8, vul jug5, vul jug3,  
        # leeg jug8, leeg jug5, leeg jug3, 
        # elke mogelijk combinatie van giet van pot x naar pot y
        
        # HINT: als je overgiet van de bijvoorbeeld jug5 naar jug8, dan heb je in jug8 (8 - self.jug8) liter plaats, 
        # en in jug5 heb je (self.jug5) liter water zitten. Het kleinste getal van die 2, kan je effectief overgieten zonder morsen.



    """BFS"""
    def find_solution(self):
        initial_state = (self.jug8, self.jug5, self.jug3)
        goal = WaterJugState(4,4,0)
        
        if self.__eq__(goal):
            return [initial_state]
        
        frontier = deque([initial_state])
        explored = {initial_state}
        parent: dict = {initial_state: None}

        while frontier:
            current = frontier.popleft()
            explored.add(current)
            for kind in self.get_next_states():
                if kind in explored or kind in parent:
                    continue
                parent[kind] = current
                # if kind == goal:
                #     # pad reconstrueren via parent-links (backward)
                #     pad = [kind.state]
                #     stap = kind
                #     while parent[stap] is not None:
                #         stap = parent[stap]
                #         pad.append(stap.state)
                #     pad.reverse()
                #     return pad
                frontier.append(kind)
        return None


if __name__ == '__main__':
    initial_state = WaterJugState(8, 5, 0)
    solution = initial_state.find_solution()
    if solution:
        print("Oplossing gevonden:")
        # print opeenvolgende stappen van de oplossing
    else:
        print("Geen oplossing gevonden.")
    
    
    # initial_state.get_next_states()
