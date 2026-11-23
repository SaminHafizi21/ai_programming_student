"""
Week 8 — Oplossing: Othello met Minimax & Evaluatiefunctie + Monty Hall
=======================================================================
Oefening 1: Mini Othello (zie `opgave_week7.md`): een willekeurige
geldige zet, een evaluatiefunctie, minimax met depth-parameter en een
best_move die de computer laat spelen.
Oefening 2: Monty Hall (zie `montyhall_opgave.py`): het driedeurenprobleem
met een expectimax-simulator die de winstpercentages vergelijkt.

Zie ook `oefeningen-adversarial_search.md` (labo week 7-8).
"""

import random

# =============== Oefening 1: Othello met Minimax ===============


class Othello:
    """Mini Othello (reversi) op een 8x8-bord met een minimax-computer.

    De computer speelt "X"; de mens speelt "O". Het bord-gedeelte is
    overgenomen uit `othello_start.py`; de AI-methodes vullen het aan.
    """

    def __init__(self) -> None:
        """Maak een leeg 8x8-bord en zet de startpositie klaar."""
        self.board: list[list[str]] = [[" " for _ in range(8)] for _ in range(8)]
        self.initialize_board()
        self.player = "X"

    def print_board(self) -> None:
        """Toon het bord in de terminal."""
        horizontal_line = "+---+---+---+---+---+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} |")
            print(horizontal_line)

    def initialize_board(self) -> None:
        """Zet de startpositie: 2 X-stenen en 2 O-stenen in het midden."""
        self.board[3][3] = self.board[4][4] = "O"
        self.board[3][4] = self.board[4][3] = "X"

    def opponent(self) -> str:
        """Geef de speler die niet aan zet is."""
        return "O" if self.player == "X" else "X"

    def change_player(self) -> None:
        """Geef de beurt door aan de andere speler."""
        self.player = self.opponent()

    def is_valid_move(self, row: int, col: int, player: str) -> bool:
        """Controleer of (row, col) een geldige zet is voor `player`.

        Args:
            row: het rij-nummer (0 tot 7).
            col: het kolom-nummer (0 tot 7).
            player: "X" of "O".

        Returns:
            True als een steen geplaatst kan worden en er in minstens één
            richting eigen stenen ingesloten worden, anders False.
        """
        if not (0 <= row < 8) or not (0 <= col < 8):
            return False
        if self.board[row][col] != " ":
            return False

        other = "O" if player == "X" else "X"
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if not (0 <= r < 8) or not (0 <= c < 8):
                continue
            # Enkel verder kijken als er een steen van de tegenstander ligt
            if self.board[r][c] == other:
                r += dr
                c += dc
                while (0 <= r < 8) and (0 <= c < 8):
                    if self.board[r][c] == " ":
                        break
                    # Hier ligt een eigen steen: de flank is gesloten
                    if self.board[r][c] == player:
                        return True
                    r += dr
                    c += dc
        return False

    def make_move(self, row: int, col: int, player: str) -> None:
        """Plaats een steen en draai alle ingesloten stenen om.

        Args:
            row: het rij-nummer.
            col: het kolom-nummer.
            player: "X" of "O".
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.board[row][col] = player
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while (0 <= r < 8) and (0 <= c < 8):
                if self.board[r][c] == " ":
                    break
                if self.board[r][c] == player:
                    # Achterwaarts teruglopen en stenen omdraaien
                    while (r != row) or (c != col):
                        r -= dr
                        c -= dc
                        self.board[r][c] = player
                    break
                r += dr
                c += dc

    def count_pieces(self) -> tuple[int, int]:
        """Geef (aantal X-stenen, aantal O-stenen)."""
        x_count = sum(row.count("X") for row in self.board)
        o_count = sum(row.count("O") for row in self.board)
        return x_count, o_count

    def valid_moves(self, player: str) -> list[tuple[int, int]]:
        """Geef alle geldige zetten voor `player` als (rij, kolom)-tupels."""
        return [(r, c) for r in range(8) for c in range(8)
                if self.is_valid_move(r, c, player)]

    def _game_over(self) -> bool:
        """Geef True als geen van beide spelers nog een zet kan doen."""
        return not self.valid_moves("X") and not self.valid_moves("O")

    def copy(self) -> "Othello":
        """Maak een diepe kopie van het bord (zonder bijwerkingen)."""
        kopie = Othello()
        for r in range(8):
            for c in range(8):
                kopie.board[r][c] = self.board[r][c]
        kopie.player = self.player
        return kopie
    def random_move(self) -> tuple[int, int] | None:
        """Kies een willekeurige geldige zet voor de speler die aan zet is.

        Returns:
            Een geldig (rij, kolom)-tupel, of None als er geen zet is.
        """
        zetten = self.valid_moves(self.player)
        random.shuffle(zetten)
        return zetten[0] if zetten else None

    def evaluate(self, player: str) -> float:
        """Evalueer de staat vanuit het perspectief van `player`.

        Eerst het stuksaldo (eigen stenen min stenen van de tegenstander),
        uitgebreid met mobiliteit (aantal geldige zetten van de ene speler
        min dat van de andere). Een terminale staat krijgt een grote
        eindscore.

        Args:
            player: "X" of "O".

        Returns:
            Een score: hoe hoger, hoe beter voor `player`.
        """
        x_count, o_count = self.count_pieces()
        if self._game_over():
            if x_count > o_count:
                return 1000.0 if player == "X" else -1000.0
            if o_count > x_count:
                return -1000.0 if player == "X" else 1000.0
            return 0.0

        other = "O" if player == "X" else "X"
        stenen = (x_count - o_count) if player == "X" else (o_count - x_count)
        mobiliteit = len(self.valid_moves(player)) - len(self.valid_moves(other))
        return float(stenen + 10 * mobiliteit)

    def minimax(self, depth: int, is_maximizing: bool, player: str) -> float:
        """Minimax met een evaluatiefunctie, zetten gesimuleerd op kopieën.

        Args:
            depth: hoeveel zetten er nog vooruit gekeken wordt
                (0 = enkel de evaluatiefunctie).
            is_maximizing: True op een knoop waar `player` aan zet is,
                False op een knoop waar de tegenstander aan zet is.
            player: de speler wiens score gemaximaliseerd wordt.

        Returns:
            De score die `player` kan afdwingen tegen een perfecte
            tegenstander.
        """
        score = self.evaluate(player)
        if depth == 0 or self._game_over():
            return score

        other = "O" if player == "X" else "X"
        if is_maximizing:
            zetten = self.valid_moves(player)
            if not zetten:
                return score
            best = float("-inf")
            for r, c in zetten:
                kopie = self.copy()
                kopie.make_move(r, c, player)
                best = max(best, kopie.minimax(depth - 1, False, player))
            return best

        zetten = self.valid_moves(other)
        if not zetten:
            return score
        best = float("inf")
        for r, c in zetten:
            kopie = self.copy()
            kopie.make_move(r, c, other)
            best = min(best, kopie.minimax(depth - 1, True, player))
        return best

    def best_move(self, depth: int = 3) -> tuple[int, int] | None:
        """Kies de beste zet via minimax voor de speler die aan zet is.

        Args:
            depth: de zoekdiepte (standaard 3).

        Returns:
            Het (rij, kolom)-tupel van de beste zet, of None als er geen
            geldige zet is.
        """
        beste_zet = None
        beste_waarde = float("-inf")
        for r, c in self.valid_moves(self.player):
            kopie = self.copy()
            kopie.make_move(r, c, self.player)
            waarde = kopie.minimax(depth - 1, False, self.player)
            if waarde > beste_waarde:
                beste_waarde = waarde
                beste_zet = (r, c)
        return beste_zet


def play() -> None:
    """Speel Othello: de computer (X) met best_move, jij (O) via input."""
    game = Othello()
    while True:
        game.print_board()
        x, o = game.count_pieces()
        print(f"X: {x}, O: {o}")

        if not game.valid_moves(game.player):
            andere = game.opponent()
            if not game.valid_moves(andere):
                if x > o:
                    print("X wint!")
                elif o > x:
                    print("O wint!")
                else:
                    print("Gelijkstand!")
                break
            print(f"Speler {game.player} kan geen zet doen; beurt gaat door.")
            game.change_player()
            continue

        if game.player == "X":
            print("Computer doet een zet:")
            zet = game.best_move()
            if zet is not None:
                game.make_move(zet[0], zet[1], "X")
        else:
            try:
                row, col = map(int,
                               input("Enter je zet (rij SPATIE kolom): ").split())
            except ValueError:
                print("Ongeldige input. Geef twee getallen zoals '0 0'.")
                continue
            if not game.is_valid_move(row, col, "O"):
                print("Ongeldige zet.")
                continue
            game.make_move(row, col, "O")
        game.change_player()

# =============== Oefening 2: Monty Hall ===============


class MontyHallGame:
    """Het driedeurenprobleem: achter één van drie deuren staat een auto.

    De speler kiest een deur, de presentator (host) opent altijd een deur
    met een geit, waarna de speler kan wisselen van deur.
    """

    def __init__(self) -> None:
        """Zet de drie deuren klaar: twee geiten en één auto."""
        self.doors: list[str] = ["geit", "geit", "auto"]
        random.shuffle(self.doors)
        self.player_choice: int | None = None
        self.host_reveals: int | None = None

    def choose_door(self, door_number: int) -> None:
        """Kies een deur (0, 1 of 2).

        Args:
            door_number: het deur-nummer; andere waarden worden genegeerd.
        """
        if 0 <= door_number < 3:
            self.player_choice = door_number
        else:
            print("Ongeldige deur. Kies tussen 0 en 2.")

    def host_reveal(self) -> None:
        """De host geeft een deur vrij waar een geit achter staat."""
        available_doors = [i for i in range(3)
                           if i != self.player_choice and self.doors[i] == "geit"]
        self.host_reveals = random.choice(available_doors)

    def switch_choice(self) -> None:
        """Laat de speler wisselen naar de enige andere dichte deur."""
        remaining_doors = [i for i in range(3)
                           if i != self.player_choice and i != self.host_reveals]
        self.player_choice = remaining_doors[0]

    def is_player_winner(self) -> bool:
        """Geef True als er een auto achter de gekozen deur staat."""
        if self.player_choice is None:
            return False
        return self.doors[self.player_choice] == "auto"

    def play_game(self, switch: bool = False) -> bool:
        """Speel een volledig spel en geef de uitkomst terug.

        Args:
            switch: True als de speler wisselt van deur.

        Returns:
            True als de speler de auto wint.
        """
        self.choose_door(random.randint(0, 2))
        self.host_reveal()
        if switch:
            self.switch_choice()
        return self.is_player_winner()


def expectimax_simulation(switch: bool, num_simulations: int = 10000) -> float:
    """Simuleer het Monty Hall-probleem en geef de winratio terug.

    Args:
        switch: True als er gewisseld wordt van deur.
        num_simulations: het aantal spellen in de simulatie.

    Returns:
        Het winaandeel (tussen 0.0 en 1.0).
    """
    total_wins = 0
    for _ in range(num_simulations):
        game = MontyHallGame()
        if game.play_game(switch):
            total_wins += 1
    return total_wins / num_simulations


def compare() -> None:
    """Vergelijk het winpercentage met en zonder wisselen."""
    win_rate_switch = expectimax_simulation(switch=True)
    win_rate_no_switch = expectimax_simulation(switch=False)

    print(f"Win percentage met switching: {win_rate_switch:.4f}")
    print(f"Win percentage zonder switching: {win_rate_no_switch:.4f}")


if __name__ == "__main__":
    # Othello: kort voorbeeld zonder interactieve input
    spel = Othello()
    spel.print_board()
    print("Random zet:", spel.random_move())
    print("Beste zet (depth 2):", spel.best_move(depth=2))

    # Monty Hall: vergelijk de twee strategieën
    compare()
