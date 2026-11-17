

# **Opgave: Eight Queens – Genetisch Algoritme (20 punten)**

In deze opdracht pas je **genetic programming** toe op het klassieke **8 Queens Problem**:

> **Plaats 8 queens op een schaakbord zodanig dat geen enkele queen een andere aanvalt.** Voor de volledigheid herhalen we wat een Queen (koningin) op een schaakbord mag doen tijdens 1 beweging:
- Ofwel zo ver als ze wil horizontaal verplaatsen
- Ofwel zo ver als ze wil verticaal verplaatsen
- Ofwel zo ver als ze wil diagonaal verplaatsen

Je krijgt een reeds voorbereide Python‐klasse `EightQueens`, waarin jij zelf
**fitness, crossover, mutatie en de GA-loop** verder moet implementeren.

Het doel is om het genetisch algoritme zo te laten werken dat het **een geldige oplossing vindt**,
of op zijn minst een **zeer goede fitness** bereikt.



## Representatie van een individu

In deze opdracht wordt een oplossing (individu) voorgesteld als een **lijst van 8 getallen**:

* Index = **rij**
* Waarde = **kolom** waarin de queen staat

Voorbeeld:

```python
example_individu = [4, 2, 7, 3, 6, 0, 5, 1]
```

Dit betekent:

| Rij | Kolom |
| --- | ----- |
| 0   | 4     |
| 1   | 2     |
| 2   | 7     |
| 3   | 3     |
| 4   | 6     |
| 5   | 0     |
| 6   | 5     |
| 7   | 1     |

De klasse bevat een functie `print_board(individual)` waarmee je de oplossing als schaakbord ziet:

```
 .  .  .  .  Q  .  .  .
 .  .  Q  .  .  .  .  .
 .  .  .  .  .  .  .  Q
 ...
```

Deze functie hoef je **niet te programmeren**, enkel te gebruiken. Dit kan nuttig zijn voor eventuele debugging.

---

## **Fitness functie invullen (8 punten)**

In de functie `calculate_fitness()` schrijf je de checks die bepalen of twee queens elkaar aanvallen.
**Hints zijn in de code voorzien – vul enkel de ontbrekende blokken aan.**



## **Crossover implementeren (3 punten)**

Schrijf een eenvoudige crossover, analoog met wat we in de les hebben gedaan.


## **Mutatie implementeren (3 punten)**

* met kans `mutation_rate`
* vervang je de kolom door een willekeurige waarde tussen 0 en 7


## **Genetisch Algoritme schrijven (4 punten)**
Schrijf hier het genetisch algoritme en zorg dat het vroegtijdig stopt als je een oplossing voor 8 Queens bereikt.

## **Korte beschrijving in comment (2 punten)**
Voeg onderaan je code commentaar toe over wat je in de output van je code ziet (werkt het ? Zo ja, leg kort uit; zo nee, leg uit wat je misschien zou kunnen veranderen om het wél te doen werken)


# **Puntenverdeling (20 punten)**

| Onderdeel                                 | Punten |
| ----------------------------------------- | ------ |
| Fitness functie correct afgewerkt         | **8**  |
| Crossover correct geïmplementeerd         | **3**  |
| Mutatie correct geïmplementeerd           | **3**  |
| Genetisch algoritme correct opgebouwd     | **4**  |
| Kort uitleggen wat de code uiteindelijk doet | **2**  |
| **Totaal**                                | **20** |




# **Uiteindelijk resultaat**

Wanneer je code correct is, zal het programma iets tonen zoals:

```
Gen 40: beste fitness = 25
Opgelost in generatie 57!
Beste oplossing: [4, 2, 7, 3, 6, 0, 5, 1]
Fitness: 28
```

En het bord:

```
 .  .  .  .  Q  .  .  .
 .  .  Q  .  .  .  .  .
 .  .  .  .  .  .  .  Q
 ...
```

---

