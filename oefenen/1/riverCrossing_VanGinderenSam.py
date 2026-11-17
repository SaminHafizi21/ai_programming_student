from collections import deque

class RiverCrossing:
    def __init__(self):
        self.initial_state = (3, 3, 0)  # (boeren_links, wolven_links, boot_kant)

        # Mogelijke overtochten (boeren, wolven)
        # een 'move' is een tuple (aantal_boeren, aantal_wolven) dat aangeeft hoeveel van elk type de boot overzet
        self.moves = [
            (1, 0), (2, 0),  # 1 of 2 boeren
            (0, 1), (0, 2),  # 1 of 2 wolven
            (1, 1),           # 1 boer en 1 wolf
        ]

        # je kan hier items als volgt uithalen:
        # for b, w in self.moves:
        #     print(f"Boeren: {b}, Wolven: {w}")

    def is_valid_state(self, boeren_links, wolven_links):
        # deze functie controleert of een staat geldig is. Geeft True terug als de staat geldig is, anders False.

        boeren_rechts = 3 - boeren_links
        wolven_rechts = 3 - wolven_links

        # Controleer of waarden binnen bereik liggen
        if (3 >= boeren_links >= 0) and (3 >= wolven_links >= 0):
            if (3 >= boeren_rechts >= 0) and (3 >= wolven_rechts >= 0):
                result = True
            else:
                result = False
        else:
            result = False

        # Controleer of boeren niet worden opgegeten
        if (boeren_links < wolven_links) or (boeren_rechts < wolven_rechts):
            if (boeren_links == 0) or (boeren_rechts == 0):
                result = True
            else:
                result = False
        
        return result

    def get_new_states(self, state):
        # deze functie genereert alle mogelijke opvolgerstaten vanuit de huidige staat
        new_states = []
        boat = state[2]

        if boat == 0:
            new_boat = 1
        else:
            new_boat = 0

        for b, w in self.moves:
            new_state = [state[0]-b,state[1]-w, new_boat]
            if self.is_valid_state(new_state[0],new_state[1]):
                new_states.append(new_state) 

        # Tips:
        # - maak een onderscheid tussen de kant van de boot waar de boot vertrekt (0 of 1)
        # - maak gebruik van functies hierboven indien nodig
        return new_states
    
    def solve(self):
        # deze functie lost het probleem
        visited = set()
        queue = deque([(self.initial_state)])
        print(queue)

        while queue:
            current_state = queue.popleft() # je moet nu ook de weg expliciet bijhouden!
            print(current_state)

            if current_state == (0, 0, 1):
                print("return")
                return current_state

            visited.add(tuple(current_state)) # cost 0 
            print(f"v: {visited}")
            
            for move in self.get_new_states(current_state):
                print(move)
           
                if move and (tuple(move) not in visited):
                    new_state = move
                    queue.append(new_state)
               
        print("None")
        return None


# Testcode
rc = RiverCrossing()
start = rc.initial_state
print("Startstaat:", start)
print("Mogelijke eerste zetten:")
for s in rc.get_new_states(start):
    print(s)

print("Oplossing?")
solution = rc.solve()
#TODO: print de oplossing als die er is, anders geef aan dat er geen oplossing is

