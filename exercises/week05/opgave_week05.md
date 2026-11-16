# Week 5 — Oefeningen: Genetische Algoritmes

## Leerdoelen
- Je implementeert een **genetisch algoritme** van nul, voor tekstgeneratie.
- Je lost het **knapsack probleem** op met een GA.

## Overzicht

| # | Oefening | Tijd |
|---|----------|------|
| 1 | Word Generator (GA) | 45 min |
| 2 | Knapsack Probleem | 30 min |

---

# Oefening 1: Word Generator

Open `word_generator_start.py`. De klasse `WordPuzzle` heeft al de methodes, jij vult ze in.

**Doel:** laat een populatie van willekeurige zinnen evolueren naar een doelzin.

## Stappenplan

### Stap 1: `generate_phrase(length)`
Genereeer een willekeurig karakter op elke positie (gebruik `string.printable`).

### Stap 2: `calculate_fitness(phrase)`
Geef een score: hoeveel karakters op de juiste positie, gedeeld door de lengte.

### Stap 3: `generate_population(size, length)`
Maak een lijst van willekeurige zinnen.

### Stap 4: Crossover & mutatie
- `crossover(p1, p2)`: split beide zinnen op een willekeurig punt en combineer.
- `mutate(phrase, rate)`: vervang elk karakter met kans `rate`.

### Stap 5: `genetic_algorithm()`
1. Genereeer startpopulatie.
2. Voor elke generatie: bereken fitness, selecteer de beste, maak kinderen via crossover + mutatie.
3. Toon de beste zin om de paar generaties.

### Stap 6: Test
Draai het script en kijk hoe de zin evolueert.

---

# Oefening 2: Knapsack Probleem

**Probleem:** je hebt een rugzak met capaciteit `C` en voorwerpen met gewicht `w` en waarde `v`.  
Kies voorwerpen zodanig dat de totale waarde max is, binnen de capaciteit.

**Representatie in een GA:** elk individu is een binaire string (1 = in de rugzak).

## Stappenplan

### Stap 1: Fitness functie
`fitness = totale waarde`, **tenzij** het totale gewicht > C → geef een lage strafscore (bv. `-1000` of `waarde - zware straf`).

### Stap 2: Los op met `pygad`
Gebruik `pygad.GA` zoals in `OneMax.py` uit de cursus:
- `num_genes` = aantal voorwerpen
- `fitness_func` = jouw knapsack fitness
- `mutation_percent_genes` = 10

### Stap 3: Test
Test met deze data (capaciteit 10):

| Voorwerp | Gewicht | Waarde |
|----------|---------|--------|
| 0 | 5 | 10 |
| 1 | 4 | 40 |
| 2 | 6 | 30 |
| 3 | 3 | 50 |

*(Optimaal: neem voorwerpen 1 en 3 → gewicht 7, waarde 90)*

---

## Klaar?
- Commit. Bekijk alvast **week 6** (tictactoe met minimax en alpha-beta).