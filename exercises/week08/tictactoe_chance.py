import sys
import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.xTurn = True
    
    def make_move(self, x, y, player):
        if self.is_valid_move(x, y):
            #check of het aan de juiste speler is
            if ((self.xTurn and (player == 'X')) or (not self.xTurn and (player == 'O'))):
                self.board[x][y] = player
                self.xTurn = not self.xTurn
                return True
            else:
                print("Het is niet aan ", player)
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
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X' or self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X':
            return 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O' or self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O':
            return -1
        return 0

    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def number_empty(self):
        counter = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    counter += 1
        return counter

    def minimax(self, depth, is_maximizing, is_chance=False, alpha=float('-inf'), beta=float('inf')):
        # dit implementeert het minimax algoritme
        score = self.evaluate()

        if score == 1:
            return score
        elif score == -1:
            return score
        elif self.is_full():
            return 0
        elif (depth == 0):
            #print("STOP, computer kan niet meer verder")
            #sys.exit(1)
            return 0

        if is_maximizing:
            best = -2 # laag genoeg beginnen
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        # X invullen en checken wat er dan precies zou gebeuren, recursieve definitie
                        new_move = self.copy()
                        new_move.board[i][j] = 'X' 
                        best = max(best, new_move.minimax(depth - 1, not is_maximizing, is_chance, alpha, beta)) #tegengestelde positie
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            break # alpha pruning
            return best
        else:
            if not is_chance:
                best = 2 # hoog genoeg beginnen
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == ' ':
                            new_move = self.copy()
                            new_move.board[i][j] = 'O' 
                            best = min(best, new_move.minimax(depth - 1, not is_maximizing, not is_chance, alpha, beta))
                            beta = min(beta, best)
                            if beta < alpha:
                                break # beta pruning
                return best
            else:
                # hier gaat de computer een random move doen
                free_moves = self.number_empty()
                free_moves_on_the_fly = 0
                total = 0
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == ' ':
                            free_moves_on_the_fly += 1
                            new_move = self.copy()
                            new_move.board[i][j] = 'O' 
                            total += new_move.minimax(depth - 1, not is_maximizing, not is_chance, alpha, beta)
                            # hier geen pruning !!!!
                average = total / free_moves_on_the_fly # gemiddelde berekenen !
                return average

    def find_best_move(self):
        best_val = -2
        best_move = (-1, -1)
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    new_move = self.copy()
                    new_move.board[i][j] = 'X'
                    move_val = new_move.minimax(10, False)
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move
    
    def random_move(self):
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    possible_moves.append((i,j))
        
        random.shuffle(possible_moves)
        return possible_moves[0]

    def copy(self):
        game = TicTacToe()
        for i in range(3):
            for j in range(3):
                game.board[i][j] = self.board[i][j]
        return game

    def play(self):
        print("Tic-Tac-Toe Game")
        self.print_board()

        playDumb = False

        while not self.is_full():
            if self.xTurn:
                print("Computer gaat een zet doen:")
                if not playDumb:
                    x, y = self.find_best_move()
                else:
                    x, y = self.random_move()

                #self.board[x][y] = 'X'
                self.make_move(x,y,'X')
                self.print_board()
                playDumb = not playDumb

            else:
                player_x, player_y = map(int, input("Enter je zet (rij SPATIE kolom): ").split())
                if self.board[player_x][player_y] != ' ':
                    print("Ongeldig, probeer opnieuw.")
                    continue
                
                #self.board[player_x][player_y] = 'O'
                self.make_move(player_x, player_y, 'O')
                
                print('Board na jouw zet:')
                self.print_board()

            if self.evaluate() == 1:
                print("Computer wint!")
                break

            elif self.is_full():
                print("Gelijkstand!")
                break

            elif self.evaluate() == -1:
                print("Jij wint!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
