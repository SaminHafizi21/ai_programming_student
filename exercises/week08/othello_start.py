"""
Oefening: Mini Othello met Evaluatiefunctie & Minimax
=======================================================
"""
import random


class Othello:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        self.initialize_board()
        self.player = 'X'

    def print_board(self):
        horizontal_line = "+---+---+---+---+---+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print("| {} | {} | {} | {} | {} | {} | {} | {} |".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            print(horizontal_line)

    def initialize_board(self):
        self.board[3][3] = self.board[4][4] = "O"
        self.board[3][4] = self.board[4][3] = "X"

    def is_valid_move(self, row, col, player):
        if self.board[row][col] != " ":
            return False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row, col
            r += dr
            c += dc
            if not (0 <= r < 8) or not (0 <= c < 8):
                continue
            if self.board[r][c] == self.opponent():
                r += dr
                c += dc
                while (0 <= r < 8) and (0 <= c < 8):
                    if self.board[r][c] == " ":
                        break
                    if self.board[r][c] == player:
                        return True
                    r += dr
                    c += dc
        return False

    def opponent(self):
        return "O" if self.player == "X" else "X"

    def change_player(self):
        self.player = self.opponent()

    def make_move(self, row, col, player):
        if self.is_valid_move(row, col, player):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            self.board[row][col] = player
            for dr, dc in directions:
                r, c = row, col
                r += dr
                c += dc
                while (0 <= r < 8) and (0 <= c < 8):
                    if self.board[r][c] == " ":
                        break
                    if self.board[r][c] == player:
                        while (r != row) or (c != col):
                            r -= dr
                            c -= dc
                            self.board[r][c] = player
                        break
                    r += dr
                    c += dc

    def count_pieces(self):
        x_count = sum(row.count("X") for row in self.board)
        o_count = sum(row.count("O") for row in self.board)
        return x_count, o_count

    def valid_moves(self, player):
        return [(r, c) for r in range(8) for c in range(8)
                if self.is_valid_move(r, c, player)]

    def random_move(self):
        # TODO: kies een geldige zet
        pass

    def evaluate(self, player):
        # TODO: evaluatiefunctie (bijv. stukken + mobiliteit)
        pass

    def minimax(self, depth, is_maximizing, player):
        # TODO: implementeer minimax (simuleer zetten op een kopie)
        pass

    def best_move(self, depth=3):
        # TODO: kies de beste zet via minimax
        pass


def play():
    game = Othello()

    while True:
        game.print_board()
        x_count, o_count = game.count_pieces()
        print(f"X: {x_count}, O: {o_count}")

        if not game.valid_moves(game.player):
            print("Geen geldige zetten meer.")
            game.change_player()
            if not game.valid_moves(game.player):
                print("Game over.")
                break

        if game.player == 'X':
            # TODO: laat de computer spelen met best_move()
            pass
        else:
            # TODO: menselijke input
            pass

        game.change_player()


if __name__ == "__main__":
    play()