# Tictactoe en minimax algoritme

## Spelletje tictactoe

Bij Tic Tac Toe is het de bedoeling om met X of O om ter eerst 3 op een rij te hebben. Spelers doen om de beurt een zet.
Implementeer het spel TicTacToe, waarbij X steeds mag beginnen. Hou bij wiens beurt het is, en de mogelijkheid om een zet te doen. Hieronder wat code als start:

```python
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # nog aanvullen
    
    def make_move(self, x, y, player):
        pass
    
    def is_valid_move(self, x, y):
        pass

    def print_board(self):
        horizontal_line = "+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print("| {} | {} | {} |".format(row[0], row[1], row[2]))
            print(horizontal_line)
```

## Minimax
Implementeer in deze klasse het minimax algoritme, vanuit het perspectief van de eerste speler, de X speler, zodat deze steeds de beste zet kan zoeken. Hiervoor kan je best volgende functies implementeren:
```python
    minimax(self, depth, is_maximizing):
        pass

    find_best_move(self): 
        pass
```
Je hebt waarschijnlijk ook nog andere functies nodig.

## CLI spel
Voorzie tot slot een `play()` methode, waarbij je de X kant door de computer laat spelen. Vraag via `player_x, player_y = map(int, input("Enter je zet (rij SPATIE kolom): ").split())` input aan de gebruiker om mee te spelen. Als alles goed is geïmplementeerd, kan je niet winnen van deze computer

### Uitbreiding
Geef jezelf een eerlijke kans door de computer 50% van de tijd een random beslissing te laten nemen in plaats van de beste zet.