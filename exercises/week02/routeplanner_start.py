"""
Oefening 3: Routeplanner (Utility-based Agent)
===============================================
Een utility-based agent maximaliseert een interne utility-functie.

Voor de route Antwerpen -> Parijs is een interessante utility:
    utility = -d(huidige stad, nieuwe stad)

De agent zoekt NIET (dit doen we in week 3): bij elke stap kiest hij greedy de
buur met de hoogste utility (kleinste afstand).
"""

from typing import Optional

CITIES = ["Antwerpen", "Brussel", "Gent", "Luik", "Doornik", "Reims", "Parijs"]

# Afstandsmatrix (onvolledig): wie met wie is er een weg?
ROADS: dict[tuple[str, str], float] = {
    ("Antwerpen", "Brussel"): 45,
    ("Antwerpen", "Gent"): 60,
    ("Brussel", "Luik"): 100,
    ("Brussel", "Gent"): 55,
    ("Brussel", "Doornik"): 90,
    ("Gent", "Doornik"): 65,
    ("Doornik", "Reims"): 130,
    ("Luik", "Reims"): 110,
    ("Reims", "Parijs"): 145,
    ("Gent", "Parijs"): 300,
}


def distance(a: str, b: str) -> Optional[float]:
    """Geef de afstand tussen twee steden, of None zonder weg."""
    if (a, b) in ROADS:
        return ROADS[(a, b)]
    if (b, a) in ROADS:
        return ROADS[(b, a)]
    return None


class RouteAgent:
    """Utility-based agent: kiest bij elke stap de dichtstbijzijnde buur."""

    def utility(self, from_city: str, to_city: str) -> float:
        """TODO: geef -d(from_city, to_city) terug."""
        d = distance(from_city, to_city)
        return -d

    def neighbours(self, city: str) -> list[str]:
        """TODO: geef alle steden met een directe weg naar `city`."""
        directCities = []

        for i in CITIES:
            if distance(city, i) is not None:
                directCities.append(i)
        return directCities

    def choose_next(self, current_city: str, visited: set[str]) -> Optional[str]:
        """TODO: kies onder de niet-bezochte buren de buur met de
        hoogste utility. Geen buren meer? -> None.
        """
        print(f"Visited city is: {visited}")
        nietBezocht = []
        for c in self.neighbours(current_city):
            if c not in visited:
                nietBezocht.append(c)

        if not nietBezocht:
            return None

        return max(nietBezocht, key=lambda c: self.utility(current_city, c))

    def plan_route(self, start_city: str, goal_city: str) -> list[str]:
        """TODO: bouw de route stad per stad via choose_next.
        Stop zodra de goal bereikt is of de agent vastzit.
        """
        route = [start_city]
        visited = {start_city}
        current = start_city

        while current != goal_city:
            volgende_city = self.choose_next(current, visited)

            if volgende_city is None:
                break

            route.append(volgende_city)
            visited.add(volgende_city)

            current = volgende_city

        return visited


if __name__ == "__main__":
    agent = RouteAgent()
    route = agent.plan_route("Antwerpen", "Parijs")
    print("Route:", " -> ".join(route))

    # agent.neighbours("Antwerpen")
    # test = agent.choose_next("Brussel", {"Antwerpen"})
    totale_afstand = 0.0
    for a, b in zip(route, route[1:]):
        d = distance(a, b)
        if d is not None:
            totale_afstand += d
    print("Totale afstand:", totale_afstand, "km")

    # Vergelijk met wat we gaan doen in week 3: wat is de kortste route met de hand? (week 3: Dijkstra!)
