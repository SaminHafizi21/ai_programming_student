# **Opgave: Bestelwagens laden (20 punten)**

Een koeriersbedrijf moet **15 pakketten** verdelen over **3 bestelwagens**.
De chauffeurs willen dat elke wagen ongeveer **even zwaar** beladen is.

> **Verdeel de pakketten over de 3 wagens zodat het verschil tussen de zwaarste en de lichtste wagen zo klein mogelijk is.**

Er zijn meer dan 14 miljoen manieren om 15 pakketten over 3 wagens te verdelen. Alles proberen is te traag.

Je krijgt een reeds voorbereide Python-klasse `Bestelwagens`, waarin jij zelf
**de fitness, crossover, mutatie en de hoofdloop** verder moet implementeren.

Het doel is om het algoritme zo te laten werken dat het **een perfect gelijke verdeling vindt**,
of op zijn minst een **zeer goede fitness** bereikt.


## De pakketten

| Pakket | Gewicht (kg) |   | Pakket | Gewicht (kg) |   | Pakket | Gewicht (kg) |
| ------ | ------------ | - | ------ | ------------ | - | ------ | ------------ |
| 0      | 8            |   | 5      | 9            |   | 10     | 24           |
| 1      | 35           |   | 6      | 17           |   | 11     | 26           |
| 2      | 29           |   | 7      | 22           |   | 12     | 5            |
| 3      | 30           |   | 8      | 26           |   | 13     | 31           |
| 4      | 31           |   | 9      | 10           |   | 14     | 12           |

Het totale gewicht is **315 kg**. Een perfect gelijke verdeling geeft dus **105 kg per wagen**.


## Representatie van een oplossing

Een oplossing is een **lijst van 15 getallen**:

* Index = **pakket**
* Waarde = **wagen** waarin het pakket zit: `0`, `1` of `2`

Voorbeeld:

```python
voorbeeld = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
```

Pakket 0 zit in wagen 0, pakket 1 in wagen 1, pakket 2 in wagen 2, pakket 3 weer in wagen 0, …

De klasse bevat een functie `print_wagens(oplossing)` die per wagen de pakketten en het totale gewicht toont.
Deze functie hoef je **niet te programmeren**, enkel te gebruiken. Dit kan nuttig zijn voor debugging.

---

## **Welk algoritme? (2 punten)**

Beantwoord bovenaan je code in commentaar:

* Welk algoritme uit de cursus gebruik je hier? Je kan het afleiden uit de parameters van de klasse.
* Waarom past het bij dit probleem? Noem één algoritme uit de cursus dat **niet** past, en waarom niet.


## **Fitness functie invullen (6 punten)**

In de functie `calculate_fitness()` bereken je hoe **gelijk** de wagens beladen zijn.

* Bereken voor elke wagen het **totale gewicht**.
* Bereken het verschil tussen de **zwaarste** en de **lichtste** wagen.
* Fitness = **minteken** voor dat verschil. Hoe dichter bij 0, hoe beter.
* Maximale fitness = **0** (alle wagens 105 kg).

Hints zijn in de code voorzien.


## **Crossover implementeren (3 punten)**

Schrijf een eenvoudige crossover, analoog met wat we in de les hebben gedaan.


## **Mutatie implementeren (3 punten)**

* met kans `mutation_rate`
* zet je een pakket in een **willekeurige** wagen (0, 1 of 2)


## **Hoofdalgoritme schrijven (5 punten)**

Schrijf het algoritme met de parameters uit de klasse, en zorg dat het **vroegtijdig stopt** als er een perfect gelijke verdeling gevonden is.


## **Korte beschrijving in comment (1 punt)**

Voeg onderaan je code commentaar toe over wat je in de output ziet:
werkt het? Draai je code een paar keer: vindt het altijd een perfecte verdeling? Wat zou je kunnen veranderen als dat niet lukt?


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
Gen 5: beste fitness = -3
Gen 10: beste fitness = -3
Gen 15: beste fitness = -3
Gen 20: beste fitness = -3
Gen 25: beste fitness = -2
Gen 30: beste fitness = -2
Opgelost in generatie 34!
Beste oplossing: [1, 2, 0, 0, 1, 1, 2, 0, 2, 2, 0, 1, 2, 1, 2]
Fitness: 0
```

En de wagens:

```
Wagen 0 (105 kg): pakketten 2, 3, 7, 10
Wagen 1 (105 kg): pakketten 0, 4, 5, 11, 13
Wagen 2 (105 kg): pakketten 1, 6, 8, 9, 12, 14
```

* Het aantal generaties verschilt per run door het toeval.
* In ongeveer 2 op de 3 runs vind je een perfecte verdeling. Soms blijft het hangen op −1 of −2: dat is ook een zeer goede verdeling.
