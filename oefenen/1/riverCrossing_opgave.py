from collections import deque


class RiverCrossing:
    def __init__(self):
        self.initial_state = (3, 3, 0)  # (boeren_links, wolven_links, boot_kant)

        # Mogelijke overtochten (boeren, wolven)
        # een 'move' is een tuple (aantal_boeren, aantal_wolven) dat aangeeft hoeveel van elk type de boot overzet
        self.moves = [
            (1, 0),
            (2, 0),  # 1 of 2 boeren
            (0, 1),
            (0, 2),  # 1 of 2 wolven
            (1, 1),  # 1 boer en 1 wolf
        ]

        # je kan hier items als volgt uithalen:
        # for b, w in self.moves:
        #     print(f"Boeren: {b}, Wolven: {w}")

    def is_valid_state(self, boeren_links, wolven_links):
        # deze functie controleert of een staat geldig is. Geeft True terug als de staat geldig is, anders False.

        boeren_rechts = 3 - boeren_links
        wolven_rechts = 3 - wolven_links

        # Controleer of waarden binnen bereik liggen

        # Controleer of boeren niet worden opgegeten

        if 0 < boeren_rechts and wolven_rechts > boeren_rechts:
            return False
        if 0 < boeren_links and wolven_links > boeren_links:
            return False

        if not (0 <= boeren_links <= 3):
            return False

        if not (0 <= wolven_links <= 3):
            return False

        if boeren_links == 0 and wolven_links > 0:
            return True
        if boeren_rechts == 0 and wolven_rechts > 0:
            return True

    def get_new_states(self, state):
        # deze functie genereert alle mogelijke opvolgerstaten vanuit de huidige staat
        # TODO

        for move in self.moves:
            b = move[0]
            w = move[1]

            if not self.is_valid_state(b, w):
                continue
            state.append((b, w, 1))
        return state

        # Tips:
        # - maak een onderscheid tussen de kant van de boot waar de boot vertrekt (0 of 1)
        # - maak gebruik van functies hierboven indien nodig

    def solve(self):
        # deze functie lost het probleem
        frontier = deque([self.initial_state])
        visited = {self.initial_state}
        parent: dict = {self.initial_node: None}
        goal = (0, 0, 1)

        while self.get_new_states():
            current = frontier.popleft()
            visited.add(current)
            for kind in current.Actions:
                if kind in visited or kind in parent:
                    continue
                parent[kind] = current  # parent van het kind(B) is currentNodeA
                if kind == goal:
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


# Testcode
rc = RiverCrossing()
start = rc.initial_state
print("Startstaat:", start)
print("Mogelijke eerste zetten:")
for s in rc.get_new_states(start):
    print(s)

print("Oplossing?")
solution = rc.solve()
# TODO: print de oplossing als die er is, anders geef aan dat er geen oplossing is
