"""De volledige stedengraaf van Antwerpen naar Parijs (startversie).

Volgt de structuur uit course-text/03_zoekalgoritmes.md: states zijn
`State`-objecten, zoekoperaties werken op `Node`-objecten met acties.
Vul zelf de functies bouw_nodes, reconstruct_pad, breadth_first_search
en depth_first_search in.
"""

from collections import deque

STEDEN_GRAAF = {
    "Antwerpen": ["Breda", "Eindhoven", "Gent"],
    "Breda": ["Antwerpen", "Rotterdam", "Eindhoven"],
    "Eindhoven": ["Antwerpen", "Breda"],
    "Rotterdam": ["Breda"],
    "Gent": ["Antwerpen", "Brugge", "Kortrijk", "Brussel"],
    "Brugge": ["Gent", "Kortrijk"],
    "Kortrijk": ["Gent", "Brugge", "Lille"],
    "Brussel": ["Gent", "Charleroi", "Namen"],
    "Charleroi": ["Brussel", "Namen"],
    "Namen": ["Brussel", "Charleroi", "Luxemburg"],
    "Luxemburg": ["Namen", "Metz"],
    "Lille": ["Kortrijk", "Arras"],
    "Arras": ["Lille", "Amiens"],
    "Amiens": ["Arras", "Saint-Quentin", "Rouen", "Beauvais"],
    "Saint-Quentin": ["Amiens", "Laon"],
    "Laon": ["Saint-Quentin", "Reims", "Soissons"],
    "Reims": ["Laon", "Metz"],
    "Soissons": ["Laon", "Compiegne"],
    "Rouen": ["Amiens"],
    "Beauvais": ["Amiens", "Compiegne", "Saint-Denis"],
    "Compiegne": ["Beauvais", "Soissons", "Saint-Denis"],
    "Saint-Denis": ["Compiegne", "Beauvais", "Parijs"],
    "Metz": ["Luxemburg", "Reims", "Dijon"],
    "Dijon": ["Metz", "Parijs"],
    "Parijs": ["Saint-Denis", "Versailles", "Orleans", "Dijon"],
    "Versailles": ["Parijs", "Le Mans"],
    "Orleans": ["Parijs", "Le Mans"],
    "Le Mans": ["Versailles", "Orleans"],
}

START = "Antwerpen"
DOEL = "Parijs"


class State:
    """Een state in de state space (hier: een stad)."""

    def __init__(self, name: str) -> None:
        self.name = name


class Node:
    """Een node in de search tree: een state plus zijn acties."""

    def __init__(self, state: State, parent: "Node | None" = None) -> None:
        self.state = state
        self.actions: list[Node] = []
        # Extra t.o.v. de cursustekst: parent-verwijzing om het pad te reconstrueren
        self.parent = parent

    def add_action(self, action: "Node") -> None:
        self.actions.append(action)


def bouw_nodes(graaf: dict[str, list[str]]) -> dict[str, Node]:
    """Vertaal de adjacency-dict naar Node-objecten met acties."""
    nodes = {
        stad: Node[State(stad)] for stad in graaf
    }  # elke stad in die graaf zit, maak een sted van met node

    for stad, buurnodes in graaf.item():
        # buren toevoegen
        for buur in buurnodes:
            nodes[stad].add_action(nodes[buur])
    return nodes


def reconstruct_pad(node: Node) -> list[str]:
    """Bouw het gevonden pad op via de parent-verwijzingen."""
    pass


def breadth_first_search(
    graaf: dict[str, list[str]], start: str, doel: str, verbose: bool = False
) -> list[str] | None:
    """BFS volgens de cursustekst: openklappen niveau per niveau via een FIFO-queue.
    Vindt het pad met het minste aantal steden.
    """
    pass


def depth_first_search(
    graaf: dict[str, list[str]], start: str, doel: str, verbose: bool = False
) -> list[str] | None:
    """DFS volgens de cursustekst: recursief, eerst zoeken in de diepte.
    Vindt snel een pad, maar niet noodzakelijk het kortste.
    """
    pass


def naar_mermaid(graaf):
    """Exporteer de graaf als mermaid flowchart (elke rand één keer)."""
    regels = ["flowchart LR"]
    gezien = set()
    for stad, verbindingen in graaf.items():
        for buur in verbindingen:
            rand = frozenset({stad, buur})
            if rand not in gezien:
                gezien.add(rand)
                regels.append(f"    {stad} --- {buur}")
    return "\n".join(regels)
