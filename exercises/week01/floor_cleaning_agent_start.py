"""
Oefening 2: Floor Cleaning Agent (Model-based Reflex Agent)
=============================================================
Implementeer een model-based reflex agent voor een robotstofzuiger.
Volg het stappenplan in opgave_week1.md.
"""


class FloorCleaningAgent:
    """
    Een model-based reflex agent die een kamer proper maakt.

    De kamer is een grid van `rows` × `cols` tegels.
    De robot start in de linkerbovenhoek (rij 0, kolom 0).
    """

    def __init__(self, rows=5, cols=10):
        """
        Initialiseer de robot met een lege kamer van `rows` × `cols`.

        Tip: gebruik een 2D-lijst om de status van elke tegel bij te houden.
        """
        self.rows = rows
        self.cols = cols

        # TODO: interne state initialiseren
        # - huidige positie (rij, kolom)
        # - grid met proper/vuil status per tegel (bv. True = proper, False = vuil)

        self.row = 0  # startrij (bovenaan)
        self.col = 0  # startkolom (links)

        # Voorbeeld: grid aanmaken (alle tegels beginnen vuil)
        # self.grid = [[False for _ in range(cols)] for _ in range(rows)]

        self.grid = []
        for r in range(rows):
            rij = []
            for k in range(cols):
                rij.append(False)
            self.grid.append(rij)

    # ---------- Basisbewegingen ----------

    def move_up(self):
        """Verplaats de robot één tegel omhoog (rij -1)."""
        if self.row > 0:
            self.row -= 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet omhoog: rand bereikt")

    def move_down(self):
        """Verplaats de robot één tegel omlaag (rij +1)."""
        if self.row < self.rows - 1:
            self.row += 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet omlaag: rand bereikt")

    def move_right(self):
        """Verplaats de robot één tegel naar links (kolom -1)."""
        if self.col < self.cols - 1:
            self.col += 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet naar rechts: rand bereikt")

    def move_left(self):
        """Verplaats de robot één tegel naar rechts (kolom +1)."""
        if self.col > 0:
            self.col -= 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet naar links: rand bereikt")

    # ---------- Stofzuigen ----------

    def clean_tile(self):
        """Stofzuig de huidige tegel (maak hem proper)."""
        # TODO: markeer huidige tegel als proper
        self.grid[self.row][self.col] = True
        print(f"Tegel ({self.row}, {self.col}) is nu proper!")

    # ---------- Strategie ----------

    def clean_room(self):
        """
        Laat de robot de volledige kamer proper maken.
        Gebruik een systematische strategie (bv. zigzag-patroon).
        """
        # TODO: implementeer een strategie
        # Tip: je kan een move_to(row, col) hulpmethode gebruiken

        for r in range(self.rows):
            for c in range(self.cols):
                if not self.grid[self.row][self.col]:
                    self.clean_tile()
                if r % 2 == 0:
                    self.move_right()
                else:
                    self.move_left()
            self.move_down()

    # ---------- Helper om naar een specifieke tegel te gaan ----------

    def move_to(self, target_row, target_col):
        """
        Verplaats de robot van huidige positie naar (target_row, target_col).
        Gebruik de basisbewegingen move_up/down/left/right.
        """
        # TODO: implementeer
        # Beweeg eerst verticaal, dan horizontaal (of omgekeerd)

        while target_col < self.col:
            self.move_left()
        while target_col > self.col:
            self.move_right()

        while target_row > self.row:
            self.move_down()
        while target_row < self.row:
            self.move_up()

    # ---------- Weergave ----------

    def print_status(self):
        """Toon de huidige status van de kamer."""
        print("\nKamer status (V = vuil, P = proper, R = robot):")
        for r in range(self.rows):
            rij_str = ""
            for c in range(self.cols):
                if r == self.row and c == self.col:
                    rij_str += " R "
                elif self.grid[r][c] == True:
                    rij_str += " P "
                else:
                    rij_str += " ? "
            print(rij_str)
        print()


if __name__ == "__main__":
    # Test je agent
    robot = FloorCleaningAgent()

    print("Beginstatus:")
    robot.print_status()
    # robot.move_down()
    # robot.move_right()
    # robot.move_left()
    # robot.clean_tile()

    # TODO: roep clean_room() aan
    # robot.clean_room()
    robot.move_to(2, 4)
    robot.move_to(2, 1)

    print("Eindstatus:")
    robot.print_status()
