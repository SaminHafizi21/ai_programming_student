
import colorama
import art

class Othello():
    def __init__(self) -> None:
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        self.initialize_board()
        self.player = 'X'

    def print_colored_board(self):
        # voor de mensen die het iets fancier willen
        colorama.init()
        for row in self.board:
            colored_row = [colorama.Fore.GREEN + cell + colorama.Fore.RESET if cell == "X" else colorama.Fore.RED + cell + colorama.Fore.RESET if cell == "O" else cell for cell in row]
            print(" ".join(colored_row))

    def print_board(self):
            horizontal_line = "+---+---+---+---+---+---+---+---+"
            print(horizontal_line)
            for row in self.board:
                print("| {} | {} | {} | {} | {} | {} | {} | {} |".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                print(horizontal_line)

    def initialize_board(self):
        # Create ASCII art
        ascii_art = art.text2art("Othello")
        print(ascii_art)

        # dit creërt de startpositie
        self.board[3][3] = self.board[4][4] = "O"
        self.board[3][4] = self.board[4][3] = "X"

    def is_valid_move(self, row, col, player):
        if self.board[row][col] != " ":
            return False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        # in alle richtingen rond het punt kijken
        for dr, dc in directions:
            r, c = row, col
            r += dr
            c += dc
            if not (0 <= r < 8) or not (0 <= c < 8):
                continue
            # als de steen in deze richting van de tegenspeler is, checken of er ergens verder een eigen steen ligt
            if self.board[r][c] == self.opponent():
                r += dr
                c += dc
                while (0 <= r < 8) and (0 <= c < 8):
                    # de reeks is onderbroken, geen goede plaats om te leggen
                    if self.board[r][c] == " ":
                        break
                    # hier ligt een eigen steen
                    if self.board[r][c] == player:
                        return True
                    r += dr
                    c += dc
        return False

    def opponent(self):
        if self.player == "X":
            return "O"
        else:
            return "X"
        
    def change_player(self):
        print('changed_player')
        self.player = self.opponent()

    def make_move(self, row, col, player):
        if self.is_valid_move(row, col, player):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            #steen leggen
            self.board[row][col] = player

            #en alle tussenliggende stenen omdraaien
            for dr, dc in directions:
                r, c = row, col
                r += dr
                c += dc
                while (0 <= r < 8) and (0 <= c < 8):
                    if self.board[r][c] == " ":
                        break
                    # steen van eigen kleur
                    if self.board[r][c] == player:
                        #achterwaarts teruglopen en stenen omdraaien
                        while (r != row) or (c != col):
                            r -= dr
                            c -= dc
                            self.board[r][c] = player
                        break
                    r += dr
                    c += dc
        # je zou ook hier change_player kunnen doen ipv op lijn circa 127

    def count_pieces(self):
        x_count = sum(row.count("X") for row in self.board)
        o_count = sum(row.count("O") for row in self.board)
        return x_count, o_count

    def random_move(self):
        pass

def play():
    game = Othello()

    while True:
        game.print_board()
        x_count, o_count = game.count_pieces()
        print(f"X: {x_count}, O: {o_count}")

        if not any(game.is_valid_move(row, col, game.player) for row in range(8) for col in range(8)):
            print("Geen geldige zetten meer voor de huidige speler.")
            game.change_player()
            if not any(game.is_valid_move(row, col, game.player) for row in range(8) for col in range(8)):
                print("Geen enkele geldige zet meer. Game over.")
                x_count, o_count = game.count_pieces()
                if x_count > o_count:
                    print("X wint!")
                elif x_count < o_count:
                    print("O wint!")
                else:
                    print("Gelijkstand!")
                break

        while True:
            try:
                print("Speler " + game.player + ", kies een zet.")
                row, col = map(int, input("Enter je zet (rij SPATIE kolom): ").split())
                if game.is_valid_move(row, col, game.player):
                    game.make_move(row, col, game.player)
                    break
                else:
                    print("Ongeldige input.")
            except ValueError:
                print("Ongeldige input. Geef twee getallen in zoals 0 0 voor het item helemaal linksbovenaan.")

        game.change_player()

if __name__ == "__main__":
    play()
