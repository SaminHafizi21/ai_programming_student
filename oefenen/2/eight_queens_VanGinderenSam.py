import random

class EightQueens:
    def __init__(self, population_size=100, mutation_rate=0.01, num_generations=200):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations
        self.n = 8  # 8x8 bord

    # -------------------------------------------------------
    # 1. Individu genereren
    # -------------------------------------------------------
    def generate_individual(self):
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    # -------------------------------------------------------
    # 2. Fitness berekenen
    # -------------------------------------------------------
    def calculate_fitness(self, individual):
        """
        Fitness = aantal NIET-aanvallende paren.
        
        We hebben 8 queens → aantal mogelijke paren = 28.
        Voor elk paar dat elkaar aanvalt, trekken we 1 punt af.
        
        Twee queens vallen elkaar aan wanneer:
        - ze in dezelfde KOLOM staan
        - ze op dezelfde DIAGONAAL staan
        (Horizontaal is onmogelijk in deze representatie, want 
        elke rij heeft precies 1 queen.)
        """

        non_attacking = 28  # maximaal aantal niet-aanvallende paren

        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Controleer of queens i en j in dezelfde kolom staan.
                # individual[i] bevat kolom van rij i.
                # Hint: gewone vergelijking volstaat.

                # if ...:
                #     non_attacking -= 1
                if individual[j] == individual[i]:
                    non_attacking -= 1

                # Controleer of queens i en j op dezelfde DIAGONAAL staan.
                # Queens staan diagonaal als het hoogteverschil gelijk is
                # aan het kolomverschil.
                # Hint: gebruik abs()

                # if ...:
                #     non_attacking -= 1
                if abs(i - j) == abs(individual[i]-individual[j]):
                    non_attacking -= 1

                if non_attacking == 28:
                    return -1

        return non_attacking


    # -------------------------------------------------------
    # 3. Populatie genereren
    # -------------------------------------------------------
    def generate_population(self):
        return [self.generate_individual() for _ in range(self.population_size)]

    # -------------------------------------------------------
    # 4. Crossover
    # -------------------------------------------------------
    def crossover(self, parent1, parent2):
        point = random.randint(0, len(parent1) - 1)
        return parent1[:point] + parent2[point:]

    # -------------------------------------------------------
    # 5. Mutatie
    # -------------------------------------------------------
    def mutate(self, individual):
        return [bit if random.random() > self.mutation_rate else abs(1 - bit) for bit in individual]

    # -------------------------------------------------------
    # 6. Bord printen
    # -------------------------------------------------------
    def print_board(self, individual):
        """
        Print het bord visueel:
        Een 'Q' op de positie van de dame,
        en '.' op lege vakken.
        """
        print("\nBordrepresentatie:\n")
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if individual[row] == col:
                    line += " Q "
                else:
                    line += " . "
            print(line)
        print("\n")
        print("Representatie:", individual)
        print("\n")


    # -------------------------------------------------------
    # 7. Genetisch algoritme
    # -------------------------------------------------------
    def genetic_algorithm(self):
        population = self.generate_population()
        for generation in range(self.num_generations):
            population.sort(key=self.calculate_fitness, reverse=True)
            best_individual = population[0]
            if self.calculate_fitness(best_individual) == -1:
                return best_individual
            new_population = population[:int(0.1 * self.population_size)]
            while len(new_population) < self.population_size:
                parent1 = random.choice(population[:int(0.5 * self.population_size)])
                parent2 = random.choice(population[:int(0.5 * self.population_size)])
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            population = new_population
            if generation % 1 == 0:
                print(f"Generatie {generation}: Beste waarde = {self.calculate_fitness(best_individual)}")
        return best_individual

# -------------------------------------------------------
# Voorbeeldgebruik
# -------------------------------------------------------
if __name__ == "__main__":
    queens = EightQueens()

    # Voorbeeld van een 'individu' in dit probleem:
    example_individu = [4, 2, 7, 3, 6, 0, 5, 1]
    queens.print_board(example_individu)

    solution = queens.genetic_algorithm()

    print("\nBeste oplossing:", solution)
    print("Fitness:", queens.calculate_fitness(solution))

    queens.print_board(solution)

#Dit algoritme is niet de juiste keuze om dit probleem op te lossen,
#aangezien elke mutatie compleet random is en op een random plaats.
#Wanneer dat er nog 24 of 25 juiste paren zijn vind het algoritme nog redelijk snel 
#1 of 2 extra juiste paren maar zeker wanneer er nog maar 1 paar gevonden moet worden
#is het bijna onmogelijk. Vooral omdat dan de kans bestaat dat je een volledig 
#nieuwe start configuratie zou moeten verkrijgen maar dat doet dit algoritme niet.
#Het onthoud de vorige configuraties die het al had gevonden met een hoge fittnes score
#dus de 28 halen is zo goed als onmogelijk; Misschien vind je die ooit met een beetje
#heel veel geluk.