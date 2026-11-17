"""
Week 2: modeloplossing van alle oefeningen
===========================================
Oefening 1: Self-Driving Car (model-based reflex agent)
Oefening 2: Foute sensor (fault-tolerant agent)
Oefening 3: Routeplanner (utility-based agent)
Oefening 4: Breadth-First Search
Oefening 5: Sliding Puzzle
"""

from collections import deque
from typing import Optional


# =============== Oefening 1: Self-Driving Car ===============


class LidarSensorInput:
    def __init__(self, distance: float = 0.0):
        self.DistanceTo = distance


class Brake:
    def __str__(self):
        return "BRAKE"


class Nothing:
    def __str__(self):
        return "NOTHING"


class SelfDrivingCar:
    """Model-based reflex agent: onthoudt de vorige afstand."""

    def __init__(self):
        self.previous_distance: Optional[float] = None

    def process(self, sensor_input: LidarSensorInput):
        afstand = sensor_input.DistanceTo

        if self.previous_distance is None:
            # eerste meting: nog geen snelheid bekend
            self.previous_distance = afstand
            return Nothing()

        delta = self.previous_distance - afstand  # positief = nadering
        if delta > 0:
            tijd_tot_botsing = afstand / delta
        else:
            tijd_tot_botsing = float("inf")

        self.previous_distance = afstand

        if tijd_tot_botsing < 5.0:
            return Brake()
        return Nothing()


# =============== Oefening 2: Foute sensor ===============


class Reading:
    """Eén meetslag van beide hoogtemeters."""

    def __init__(self, sensor_a: float, sensor_b: float):
        self.sensor_a = sensor_a
        self.sensor_b = sensor_b


class Correct:
    def __str__(self):
        return "CORRECTIE AANVRAGEN"


class FaultTolerantAgent:
    """Model-based reflex agent met redundante sensoren en sensor model."""

    TOLERANCE = 50.0
    DESCENT_LIMIT = -10.0

    def __init__(self):
        self.previous_value: Optional[float] = None
        self.suspected_sensor: Optional[str] = None

    def read_all(self, p: Reading) -> tuple:
        return p.sensor_a, p.sensor_b

    def reliable_value(self, a: float, b: float) -> float:
        """Kies de betrouwbaarste meting op basis van overeenkomst
        en (bij discrepantie) consistentie met de vorige waarde."""
        if self.previous_value is None:
            # eerste meetslag: nog geen referentie, kies sensor a
            if a != b:
                self.suspected_sensor = "b"
            return a

        if abs(a - b) <= self.TOLERANCE:
            # beide sensoren zijn het bij benadering eens
            self.suspected_sensor = None
            return (a + b) / 2.0

        # discrepantie: kies de sensor het dichtst bij de vorige waarde
        if abs(a - self.previous_value) <= abs(b - self.previous_value):
            self.suspected_sensor = "b"
            return a
        self.suspected_sensor = "a"
        return b

    def process(self, p: Reading):
        a, b = self.read_all(p)
        waarde = self.reliable_value(a, b)

        if self.previous_value is None:
            self.previous_value = waarde
            return Nothing()

        delta = waarde - self.previous_value
        self.previous_value = waarde

        if delta < self.DESCENT_LIMIT:
            return Correct()
        return Nothing()


# =============== Oefening 3: Routeplanner (utility-based) ===============

CITIES = ["Antwerpen", "Brussel", "Gent", "Luik", "Doornik", "Reims", "Parijs"]

ROADS: dict = {
    ("Antwerpen", "Brussel"): 45,
    ("Antwerpen", "Gent"): 60,
    ("Brussel", "Luik"): 100,
    ("Brussel", "Gent"): 55,
    ("Brussel", "Doornik"): 90,
    ("Gent", "Doornik"): 65,
    ("Doornik", "Reims"): 130,
    ("Reims", "Parijs"): 145,
    ("Gent", "Parijs"): 300,
}


def distance(a: str, b: str) -> Optional[float]:
    """Geef de afstand tussen twee steden, of None zonder weg.

    De wegen in ROADS zijn gericht: alleen de (a, b) combinaties uit
    de tabel zijn berijdbaar in die richting.
    """
    return ROADS.get((a, b))


class RouteAgent:
    """Utility-based agent: kiest bij elke stap de dichtstbijzijnde buur."""

    def utility(self, from_city: str, to_city: str) -> float:
        d = distance(from_city, to_city)
        return -d

    def neighbours(self, city: str) -> list:
        return [c for c in CITIES if distance(city, c) is not None]

    def choose_next(self, current_city: str, visited: set) -> Optional[str]:
        kandidaten = [c for c in self.neighbours(current_city) if c not in visited]
        if not kandidaten:
            return None
        return max(kandidaten, key=lambda c: self.utility(current_city, c))

    def plan_route(self, start_city: str, goal_city: str) -> list:
        """Bouw de route stad per stad via choose_next.

        Stop zodra de goal bereikt is of de agent vastzit (geen
        niet-bezochte buren meer).
        """
        route = [start_city]
        visited = {start_city}
        while route[-1] != goal_city:
            volgende = self.choose_next(route[-1], visited)
            if volgende is None:
                break  # vastgelopen
            route.append(volgende)
            visited.add(volgende)
        return route
