import random
import string

class WordPuzzle:
    def __init__(self, target_phrase, population_size=100, mutation_rate=0.01, num_generations=10000):
        self.target_phrase = target_phrase
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations
        self.allowed_chars = string.ascii_letters + string.punctuation + " " + "àáâäçèéêëîïôöùûüÿñ"

    # Functie om een willekeurige zin te genereren
    def generate_phrase(self, length):
        return "".join(random.choice(self.allowed_chars) for _ in range(length))

    # Functie om de fitness van een zin te berekenen
    def calculate_fitness(self, phrase):
        score = sum(1 for a, b in zip(phrase, self.target_phrase) if a == b)
        return score / len(self.target_phrase)

    # Functie om een populatie te genereren
    def generate_population(self, size, phrase_length):
        return [self.generate_phrase(phrase_length) for _ in range(size)]

    # Functie om een kruising te doen tussen twee zinnen
    def crossover(self, phrase1, phrase2):
        midpoint = random.randint(0, len(phrase1) - 1)
        return phrase1[:midpoint] + phrase2[midpoint:]

    # Functie om een mutatie toe te passen op een zin
    def mutate(self, phrase, rate):
        phrase_list = list(phrase)
        for i in range(len(phrase_list)):
            if random.random() < rate:
                phrase_list[i] = random.choice(self.allowed_chars)
        return "".join(phrase_list)

    # Functie om de beste zin uit de populatie te selecteren
    def select_best(self, population):
        scored = [(p, self.calculate_fitness(p)) for p in population]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0][0], scored[0][1]

    # Functie om de genetische algoritme uit te voeren
    def genetic_algorithm(self):
        population = self.generate_population(self.population_size, len(self.target_phrase))
        for generation in range(self.num_generations):
            new_population = []
            for _ in range(self.population_size):
                parent1 = self.select_best(random.sample(population, 10))[0]
                parent2 = self.select_best(random.sample(population, 10))[0]
                child = self.crossover(parent1, parent2)
                child = self.mutate(child, self.mutation_rate)
                new_population.append(child)

            population = new_population
            best_phrase, best_fitness = self.select_best(population)

            if generation % 100 == 0:
                print(f"Generatie {generation}: {best_phrase} (fitness: {best_fitness:.3f})")

            if best_phrase == self.target_phrase:
                print(f"Perfecte match gevonden in generatie {generation}!")
                return best_phrase, generation

        return self.select_best(population)[0]

# Hoofdfunctie om de genetische algoritme te testen
def main():
    target_phrase = "De basiswetten van de robotica werden ontwikkeld door Asimov"
    population_size = 100
    mutation_rate = 0.01
    num_generations = 10000

    puzzle = WordPuzzle(target_phrase, population_size, mutation_rate, num_generations)
    best_phrase, found_gen = puzzle.genetic_algorithm()
    print(f"Beste zin na {found_gen} generaties: {best_phrase}")

# Uitvoeren van de hoofdfunctie
if __name__ == "__main__":
    main()
