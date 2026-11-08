"""
Oefening: TicTacToe met Minimax & Alpha-Beta
==============================================
"""
import copy


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def possible_moves(self):
        """Geef lijst van (rij, kolom)-tupels van lege velden."""
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def is_valid_move(self, x, y):
        pass

    def make_move(self, x, y, player):
        pass

    def undo_move(self, x, y):
        self.board[x][y] = ' '

    def check_winner(self):
        pass

    def is_draw(self):
        return len(self.possible_moves()) == 0 and not self.check_winner()

    def minimax(self, depth, is_maximizing, alpha=None, beta=None, max_depth=None):
        pass

    def find_best_move(self):
        pass

    def print_board(self):
        horizontal_line = "+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print("| {} | {} | {} |".format(row[0], row[1], row[2]))
            print(horizontal_line)

    def play(self):
        pass


if __name__ == "__main__":
    game = TicTacToe()
    game.play()