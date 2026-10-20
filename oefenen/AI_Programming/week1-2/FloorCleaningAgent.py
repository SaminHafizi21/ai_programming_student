from random import randrange

class FloorCleaningAgent:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.floor = [[False for _ in range(width)] for _ in range(height)]  # Initialize the floor as dirty
        self.current_x = 0
        self.current_y = 0

    def clean(self, x, y):
        """
        Kuis de tegel op coordinaat (x,y)
        """
        if not self.floor:
            self.floor[x][y] = True

    def is_clean(self):
        """
        Controleer of de vloer proper is
        """
        for x in range(self.width):
            for y in range(self.height):
                tile = self.floor[x][y]
                print(tile)
                if not tile:
                    return False
        return True

    def clean_floor(self):
        """
        Kuis heel de vloer.
        """
        for y in range(self.height):
            for x in range(self.width):
                self.floor[x][y] = True

    def display_floor(self):
        """
        Geef de huidige staat van de vloer weer. C staat voor clean, D voor dirty
        """
        for row in self.floor:
            print(" ".join(["C" if cell else "D" for cell in row]))

    def move_left(self):
        """
        Ga 1 stap naar links
        """
        if self.current_x > 0 :
            self.current_x -= 1

    def move_right(self):
        """
        Ga 1 stap naar rechts
        """
        if self.current_x < self.width:
            self.current_x += 1

    def move_up(self):
        """
        Ga 1 stap naar boven
        """
        if self.current_y < self.height:
            self.current_y += 1

    def move_down(self):
        """
        Ga 1 stap naar beneden
        """
        if self.current_y > 0:
            self.current_y -= 1

    def move_randomly(self):
        """
        Maak een random beweging (optioneel)
        """
        r_x = randrange(0, self.width)
        r_y = randrange(0, self.height)

        self.current_x = r_x
        self.current_y = r_y

    def move_to_next_spot(self):
        """
        Ga op een systematische manier door de lijst van tegels
        """

        while True:
            if self.current_y % 2 == 0:
                if self.current_x < self.width:
                    self.move_right()
                    print("r")
                elif self.current_y < self.height:
                    self.move_up()
                    print("u1")
                else:
                    print("b1")
                    break
            else:
                if self.current_x <= self.width and self.current_x != 0:
                    self.move_left()
                    print("l")
                elif self.current_y < self.height:
                    self.move_up()
                    print("u2")
                else:
                    print("b2")
                    break

            print(f"{self.current_x}, {self.current_y}")
                
        

# Example usage:
agent = FloorCleaningAgent(5, 5)
#agent.display_floor()
#agent.clean_floor()
#agent.display_floor()
#agent.is_clean()
agent.move_to_next_spot()