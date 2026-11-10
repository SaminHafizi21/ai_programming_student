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
                # TODO 1:
                # Controleer of queens i en j in dezelfde kolom staan.
                # individual[i] bevat kolom van rij i.
                # Hint: gewone vergelijking volstaat.

                if individual[i] == individual[j]:
                    non_attacking -= 1


                # TODO 2:
                # Controleer of queens i en j op dezelfde DIAGONAAL staan.
                # Queens staan diagonaal als het hoogteverschil gelijk is
                # aan het kolomverschil.
                # Hint: gebruik abs()

                if abs(i-j) == abs(individual[i]-individual[j]): 
                    non_attacking -= 1
                pass

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
        #TODO
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:]

    # -------------------------------------------------------
    # 5. Mutatie
    # -------------------------------------------------------
    def mutate(self, individual):
        # TODO
        # schrijf code die bij het individu, op basis van de mutation rate, af en toe een queen van plaats verandert.
        # doe dit door voor elke waarde van de array 'individual' met bepaalde kans een random getal te kiezen tussen 0 en 7
        
        resultaat = []
        for queen in individual:
            if random.random() < self.mutation_rate:
                resultaat.append(random.randint(0, 7))
            else:
                resultaat.append(queen)
        return resultaat


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
        #TODO
        # schrijf een algoritme dat met behulp van genetic programming dit probleem oplost.
        # gebruik de parameters zoals ze zijn meegegeven in de klasse (helemaal bovenaan deze file als parameter)
        # pas de code aan om vroeger uit een lus/loop te stappen indien nodig - gebruik daarvoor een conditie op je eigen fitness functie
        
        population = self.generate_population()
        
        for gen in range(self.num_generations):
            population.sort(key=self.calculate_fitness, reverse=True)
            best_pop = population[0]
            
            if gen % 10 == 0:
                print(f"Gen {gen}: fitness: {self.calculate_fitness(best_pop)}")
                

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
