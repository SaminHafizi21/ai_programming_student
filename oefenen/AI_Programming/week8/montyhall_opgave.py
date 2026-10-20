import random

class MontyHallGame:
    def __init__(self):
        self.doors = ['geit', 'geit', 'auto']
        random.shuffle(self.doors)
        self.player_choice = None
        self.host_reveals = None

    def choose_door(self, door_number):
        # Kies 0 1 of 2
        self.player_choice = door_number

    def host_reveal(self):
        # De host geeft willekeurig een deur met een geit vrij
        possible_doors = [
            door for door in range(len(self.doors))
            if door != self.player_choice and self.doors[door] != 'auto'
        ]
        self.host_reveals = random.choice(possible_doors)


    def switch_choice(self):
        # Speler wisselt van keuze
        remaining = [door for door in range(3) if door != self.player_choice and door != self.host_reveals]
        self.player_choice = remaining[0]

    def is_player_winner(self):
        # terminale check
        if self.doors[self.player_choice] == 'auto':
            return True
        return False

    def play_game(self, switch=False):
        # simulatie
        self.choose_door(random.randint(0, 2))
        self.host_reveal()
        if switch:
            self.switch_choice()
        return self.is_player_winner()
    
def test():
    # voorbeeld gebruik
    game = MontyHallGame()
    game.choose_door(1)
    print("Initiële keuze:", game.doors[game.player_choice])
    game.host_reveal()
    print("Host geeft valse deur vrij:", game.doors[game.host_reveals])
    game.switch_choice()
    print("Speler wisselt:", game.doors[game.player_choice])
    print("Speler wint:", game.play_game(switch=True))
    
def expectimax_simulation(switch):
    total_wins = 0
    num_simulations = 10000  # aantal simulaties
    for _ in range(num_simulations):
        game = MontyHallGame()
        win = game.play_game(switch)
        if win:
            total_wins += 1
    return total_wins
    
def compare():
    # Bereken percentage winst - print het resultaat
    yes_switch = expectimax_simulation(True)
    no_switch = expectimax_simulation(False)
    print(f"Winst percentage als je switcht: {(yes_switch/100):.2f}%")
    print(f"Winst percentage als je blijft: {(no_switch/100):.2f}%")

if __name__ == "__main__":
    #test()
    compare()

