import random

class MontyHallGame:
    def __init__(self):
        self.doors = ['geit', 'geit', 'auto']
        random.shuffle(self.doors)
        self.player_choice = None
        self.host_reveals = None

    def choose_door(self, door_number):
        # Kies 0 1 of 2
        pass

    def host_reveal(self):
        # De host geeft een deur met een geit vrij
        pass

    def switch_choice(self):
        # Speler wisselt van keuze
        pass

    def is_player_winner(self):
        # terminale check
        pass

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
    #TODO
    
def compare():
    # Bereken percentage winst - print het resultaat
    pass

if __name__ == "__main__":
    #test()
    compare()

