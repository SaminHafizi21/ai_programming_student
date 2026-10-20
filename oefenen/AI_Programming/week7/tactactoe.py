class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # nog aanvullen
    
    def make_move(self, x, y, player):
        if self.is_valid_move(x, y):
            self.board[x][y] = player
            return True
        return False
    
    def is_valid_move(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == ' '
    
    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        # Check for tie
        if all(cell != ' ' for row in self.board for cell in row):
            return 'tie'
        return None

    def print_board(self):
        horizontal_line = "+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print("| {} | {} | {} |".format(row[0], row[1], row[2]))
            print(horizontal_line)

    def minimax(self, depth, is_maximizing):
        winner = self.check_winner()
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        elif winner == 'tie':
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    def find_best_move(self): 
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'X'
                    score = self.minimax(0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def play(self):
        #cli game, computer is X
        print("Welcome to Tic-Tac-Toe! You are O, computer is X.")
        self.print_board()

        while True:
            # Player move
            x, y = map(int, input("Enter row and column (0-2): ").replace("-", " ").split())
            if not self.make_move(x, y, 'O'):
                print("Invalid move, try again.")
                continue
            self.print_board()

            if self.check_winner() is not None:
                break

            # Computer move
            move = self.find_best_move()
            if move:
                self.make_move(move[0], move[1], 'X')
                print(f"Computer played {move}")
                self.print_board()

            winner = self.check_winner()
            if winner:
                if winner == 'tie':
                    print("It's a tie!")
                else:
                    print(f"{winner} wins!")
                break

def main():
    game = TicTacToe()
    game.play()

if __name__ == "__main__":
    main()