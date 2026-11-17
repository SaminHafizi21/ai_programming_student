# **Opgave: Eerlijke teams (20 punten)**

Een sportleraar wil **16 leerlingen** verdelen over **2 teams van 8** voor een voetbalwedstrijd.
Elke leerling heeft een **skillscore**.

> **Verdeel de leerlingen zo dat beide teams precies 8 spelers hebben en hun totale skill zo dicht mogelijk bij elkaar ligt.**

Er zijn 12 870 manieren om 8 spelers uit 16 te kiezen. De leraar wil dat niet allemaal met de hand proberen.

Je krijgt een reeds voorbereide Python-klasse `EerlijkeTeams`, waarin jij zelf
**de fitness, crossover, mutatie en de hoofdloop** verder moet implementeren.

Het doel is om het algoritme zo te laten werken dat het **een perfect eerlijke verdeling vindt**,
of op zijn minst een **zeer goede fitness** bereikt.


## De leerlingen

| Index | Naam   | Skill |   | Index | Naam    | Skill |
| ----- | ------ | ----- | - | ----- | ------- | ----- |
| 0     | Amira  | 60    |   | 8     | Ilias   | 46    |
| 1     | Bram   | 49    |   | 9     | Jana    | 63    |
| 2     | Chloé  | 65    |   | 10    | Kobe    | 77    |
| 3     | Dries  | 81    |   | 11    | Lotte   | 43    |
| 4     | Elif   | 43    |   | 12    | Mehdi   | 98    |
| 5     | Femke  | 44    |   | 13    | Nora    | 72    |
| 6     | Gilles | 92    |   | 14    | Omar    | 53    |
| 7     | Hanne  | 74    |   | 15    | Pauline | 42    |

De totale skill van alle leerlingen samen is **1002**. Een perfect eerlijke verdeling geeft dus **501 per team**.


## Representatie van een oplossing

Een oplossing is een **lijst van 16 bits**:

* Index = **leerling**
* Waarde = **team**: `0` = team A, `1` = team B

Voorbeeld:

```python
voorbeeld = [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1]
```

Amira (0) zit in team A, Bram (1) in team B, Chloé (2) in team A, …

De klasse bevat een functie `print_teams(oplossing)` die beide teams toont met namen, aantal spelers en totale skill.
Deze functie hoef je **niet te programmeren**, enkel te gebruiken. Dit kan nuttig zijn voor debugging.

---

## **Welk algoritme? (2 punten)**

Beantwoord bovenaan je code in commentaar:

* Welk algoritme uit de cursus gebruik je hier? Je kan het afleiden uit de parameters van de klasse.
* Waarom past het bij dit probleem? Noem één algoritme uit de cursus dat **niet** past, en waarom niet.


## **Fitness functie invullen (6 punten)**

In de functie `calculate_fitness()` bereken je hoe **eerlijk** een verdeling is.

* Bereken het **verschil** in totale skill tussen team A en team B (altijd positief).
* Heeft team B niet precies 8 spelers? Tel dan een **straf** van 100 bij het verschil.
* Fitness = **min** (verschil + straf). Hoe dichter bij 0, hoe beter.
* Maximale fitness = **0** (perfect eerlijk, 8 tegen 8).

Hints zijn in de code voorzien.


## **Crossover implementeren (3 punten)**

Schrijf een eenvoudige crossover, analoog met wat we in de les hebben gedaan.


## **Mutatie implementeren (3 punten)**

* met kans `mutation_rate`
* zet je een leerling in het **andere** team


## **Hoofdalgoritme schrijven (5 punten)**

Schrijf het algoritme met de parameters uit de klasse, en zorg dat het **vroegtijdig stopt** als er een perfect eerlijke verdeling gevonden is.


## **Korte beschrijving in comment (1 punt)**

Voeg onderaan je code commentaar toe over wat je in de output ziet.
Kijk ook naar de beste fitness per generatie: wordt die soms **slechter**? Waarom kan dat, en wat zou je kunnen veranderen om dat te voorkomen?


# **Puntenverdeling (20 punten)**

| Onderdeel                                    | Punten |
| -------------------------------------------- | ------ |
| Algoritme benoemen en verantwoorden          | **2**  |
| Fitness functie correct afgewerkt            | **6**  |
| Crossover correct geïmplementeerd            | **3**  |
| Mutatie correct geïmplementeerd              | **3**  |
| Hoofdalgoritme correct opgebouwd             | **5**  |
| Kort uitleggen wat de code uiteindelijk doet | **1**  |
| **Totaal**                                   | **20** |


# **Uiteindelijk resultaat**

Wanneer je code correct is, zal het programma iets tonen zoals:

```
Gen 0: beste fitness = -4
Gen 5: beste fitness = -8
Gen 10: beste fitness = -4
Gen 15: beste fitness = -4
Gen 20: beste fitness = 0
Opgelost in generatie 20!
Beste oplossing: [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1]
Fitness: 0
```

En de teams:

```
Team A (8 spelers, skill 501): Amira, Chloé, Femke, Gilles, Hanne, Ilias, Kobe, Lotte
Team B (8 spelers, skill 501): Bram, Dries, Elif, Jana, Mehdi, Nora, Omar, Pauline
```

* Het aantal generaties verschilt per run door het toeval. Meestal vind je een perfecte verdeling binnen 100 generaties.
* Soms blijft het hangen op **−2**: dat is ook een heel goede verdeling (500 tegen 502).
