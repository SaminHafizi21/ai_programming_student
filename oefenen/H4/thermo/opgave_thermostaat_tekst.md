# **Opgave: Thermostaat – Simulated Annealing (20 punten)**

In deze opdracht pas je **simulated annealing** toe op een eenvoudig zoekprobleem:

> **Vind in een rij van 20 plaatsen de plaats met de laagste kost.** Je start op plaats 0 en mag bij elke stap maar **één plaats naar links of naar rechts**.

Je krijgt een reeds voorbereide Python-klasse `Landschap`, waarin jij zelf
**de kostfunctie, de buur, de aanvaardingskans en de simulated annealing-loop** moet implementeren.

Het doel is om het algoritme zo te laten werken dat het **het globale minimum vindt**,
en niet blijft steken in het **lokale minimum**.


## Het landschap

```
plaats:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
kost:    9  7  5  3  4  6  8  7  5  3  1  2  4  6  8  9  7  6  8  9
```

* Vanaf plaats 0 gaat het bergaf tot **plaats 3 (kost 3)**: een **lokaal minimum**.
* Daarna gaat het eerst omhoog (tot kost 8 op plaats 6).
* Het **globale minimum** ligt op **plaats 10 (kost 1)**.

De klasse bevat een functie `greedy()` die altijd naar de laagste buur gaat en stopt als er geen lagere is.
Deze functie hoef je **niet te programmeren**, enkel te gebruiken om te vergelijken.

---

## **Kostfunctie invullen (2 punten)**

In de functie `cost()` geef je de kost op een gegeven plaats terug.


## **Buur maken (4 punten)**

In de functie `random_neighbor()` geef je willekeurig de plaats links of rechts terug.

* een buur ligt altijd **binnen** de rij (0 tot 19)
* plaats 0 heeft enkel een rechterbuur, plaats 19 enkel een linkerbuur


## **Aanvaardingskans implementeren (3 punten)**

* gebruik de formule uit de les: `P = exp(−Δ / T)`
* `Δ` = hoeveel slechter de nieuwe plaats is, `T` = de temperatuur


## **Simulated annealing schrijven (8 punten)**

Schrijf het algoritme met de parameters uit de klasse:

* start op `start`, met temperatuur `initial_temperature`
* doe `num_iterations` stappen
* een betere buur aanvaard je **altijd**, een slechtere **met kans** `P`
* koel af met `T = T × cooling_rate`
* hou de **beste plaats ooit** bij
* geef een tuple terug: `(beste_plaats, beste_kost)`


## **Korte beschrijving in comment (3 punten)**

Voeg onderaan je code commentaar toe over wat je in de output ziet:

* Werkt het? Vindt simulated annealing een betere plaats dan greedy? Leg kort uit waarom.
* Zet `cooling_rate` op `0.99`. Wat verandert er? Waarom?
* Zet `initial_temperature` op `0.1`. Op welk algoritme lijkt simulated annealing dan? Waarom?


# **Puntenverdeling (20 punten)**

| Onderdeel                                    | Punten |
| -------------------------------------------- | ------ |
| Kostfunctie correct                          | **2**  |
| Buur correct (ook aan de randen)             | **4**  |
| Aanvaardingskans correct                     | **3**  |
| Simulated annealing correct opgebouwd        | **8**  |
| Kort uitleggen wat de code uiteindelijk doet | **3**  |
| **Totaal**                                   | **20** |


# **Uiteindelijk resultaat**

Wanneer je code correct is, zal het programma iets tonen zoals:

```
Greedy: plaats 3, kost 3

Stap 0: T = 10.00, plaats 1, kost 7
Stap 250: T = 2.86, plaats 12, kost 4
Stap 500: T = 0.82, plaats 10, kost 1
Stap 750: T = 0.23, plaats 10, kost 1
...
Simulated annealing: plaats 10, kost 1
```

De plaatsen onderweg verschillen per run door het toeval. In ongeveer 19 van de 20 runs vindt simulated annealing plaats 10.
