"""
Oefening: TicTacToe met Expectimax (minimax met kanselement)
==============================================================

De computer speelt afwisselend PERFECT en WILLEKEURIG:
- zet 1: perfect, zet 2: willekeurig, zet 3: perfect, ...

Implementeer het EXPECTIMAX-algoritme. In minimax zijn er drie soorten knopen:
- MAX-knoop (X): de beste zet voor X.
- MIN-knoop (O, is_chance=False): de slechtste zet voor X.
- CHANCE-knoop (O, is_chance=True): de speler speelt willekeurig,
  dus neem het GEMIDDELDE over alle mogelijke zetten.
"""
import random


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.xTurn = True

    def make_move(self, x, y, player):
        """Plaats `player` op (x, y) als dat aan de beurt is en geldig."""
        if self.is_valid_move(x, y):
            if (self.xTurn and player == 'X') or (not self.xTurn and player == 'O'):
                self.board[x][y] = player
                self.xTurn = not self.xTurn
                return True
            print("Het is niet aan", player)
            return False
        print('Dit is geen geldige zet')
        return False

    def is_valid_move(self, x, y):
        # Check boundaries en of de cell nog leeg is
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == ' '

    def print_board(self):
        horizontal_line = "+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print("| {} | {} | {} |".format(row[0], row[1], row[2]))
            print(horizontal_line)

    def evaluate(self):
        """Geef 1 als X wint, -1 als O wint, anders 0."""
        for row in self.board:
            if row.count('X') == 3:
                return 1
            if row.count('O') == 3:
                return -1
        for col in range(3):
            if [self.board[row][col] for row in range(3)].count('X') == 3:
                return 1
            if [self.board[row][col] for row in range(3)].count('O') == 3:
                return -1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X' \
                or self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X':
            return 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O' \
                or self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O':
            return -1
        return 0

    def is_full(self):
        return all(' ' not in row for row in self.board)

    def number_empty(self):
        return sum(row.count(' ') for row in self.board)

    def copy(self):
        """Maak een diepe kopie van het spel (zonder bijwerkingen)."""
        game = TicTacToe()
        game.xTurn = self.xTurn
        for i in range(3):
            for j in range(3):
                game.board[i][j] = self.board[i][j]
        return game

    # ================== Hieronder: te implementeren ==================

    def minimax(self, depth, is_maximizing, is_chance=False,
                alpha=float('-inf'), beta=float('inf')):
        """Implementeer EXPECTIMAX.

        Args:
            depth: het aantal nog te bekijken zetten.
            is_maximizing: True op een MAX-knoop (X), False op MIN/chance.
            is_chance: True als de speler hier WILLEKEURIG kiest.
            alpha, beta: grenzen voor alpha-beta-pruning (optioneel).

        Returns:
            De verwachte score: 1 = X wint, -1 = O wint, 0 = gelijkspel.
        """
        score = self.evaluate()

        # Terminale staat of geen diepte meer over
        if score in (1, -1) or self.is_full() or depth == 0:
            return score

        if is_maximizing:
            # MAX-knoop: kies de beste zet voor X
            # TODO: probeer elke lege cel, zet 'X' op een kopie en neem het max.
            return 0
        elif not is_chance:
            # MIN-knoop: kies de slechtste zet voor X
            # TODO: probeer elke lege cel, zet 'O' op een kopie en neem het min.
            return 0
        else:
            # CHANCE-knoop: de speler speelt willekeurig
            # TODO: tel de score van elke zet op en deel door het aantal.
            #       Let op: hier géén pruning, want elke zet telt even zwaar.
            return 0

    def find_best_move(self):
        """Geef de beste zet voor X via expectimax."""
        # TODO: probeer elke lege cel, roep minimax aan en onthoud de
        #       (i, j) van de zet met de hoogste waarde.
        return (-1, -1)

    def random_move(self):
        """Geef een willekeurige geldige zet (gebruik random.shuffle)."""
        # TODO: verzamel alle lege velden en kies er één willekeurig uit.
        return (-1, -1)

    def play(self):
        """Speel X (computer) tegen O (jij). De computer speelt
        afwisselend perfect (`find_best_move`) en willekeurig (`random_move`)."""
        # TODO: pas deze methode aan zoals in tictactoe_chance.py.
        pass


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
