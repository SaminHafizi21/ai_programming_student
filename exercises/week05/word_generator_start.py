"""
Oefening 1: Word Generator (Genetisch Algoritme)
==================================================
Evolueer een populatie van willekeurige zinnen naar een doelzin.
"""
import random
import string


class WordPuzzle:
    def __init__(self, target_phrase, population_size=100, mutation_rate=0.01, num_generations=10000):
        self.target_phrase = target_phrase
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations

    def generate_phrase(self, length):
        new_phrase = ""
        for i in range(length):
            new_phrase += random.choice(string.printable)
        return new_phrase

    def calculate_fitness(self, phrase):
        score = 0
        for i in range(len(phrase)):
            if phrase[i] == self.target_phrase[i]:
                score += 1
        
        return score / len(self.target_phrase)

    def generate_population(self, size, phrase_length):
        population = []
        for p in range(size):
            population.append(self.generate_phrase(phrase_length))
        return population

    def crossover(self, phrase1, phrase2):
        point = random.randint(1, len(phrase1)-1)
        return phrase1[:point] + phrase2[point:]

    def mutate(self, phrase, rate):
        chars = list(phrase)
        for i in range(len(chars)):
            if random.random() < rate:
                chars[i] = random.choice(string.printable)
        
        return ''.join(chars)

    def select_best(self, population):
        population.sort(key=self.calculate_fitness, reverse = True)
        return population[:10]

    def genetic_algorithm(self):
        population = self.generate_population(self.population_size, len(self.target_phrase))
    
        for gen in range(self.num_generations):
            parents = self.select_best(population)
            best_parent = parents[0]
            
            if gen % 20 == 0:
                print(f"{gen} || {best_parent} || {self.target_phrase}")
            
            if self.calculate_fitness(best_parent) == 1.0:
                return best_parent
                
            children = []
            while len(children) < self.population_size:
                p1, p2 = random.sample(parents, 2)
                child = self.crossover(p1, p2)
                child = self.mutate(child, self.mutation_rate)
                
                children.append(child)
            
            population= children
        return self.select_best(population)[0]
            
                    


def main():
    target_phrase = "De basiswetten van de robotica werden ontwikkeld door Asimov"
    puzzle = WordPuzzle(target_phrase)
    best_phrase = puzzle.genetic_algorithm()
    print(f"Beste zin: {best_phrase}")


if __name__ == "__main__":
    main() 