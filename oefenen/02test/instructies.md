Je gaat een 4x4 sudoku oplossen.

## Het sudoku-probleem

Je krijgt een rooster van 4x4 dat deels is ingevuld met cijfers 1 tot en met 4 (0 = lege cel).

- In elke **rij** moet elk cijfer 1 tot en met 4 exact één keer voorkomen.
- In elke **kolom** moet elk cijfer 1 tot en met 4 exact één keer voorkomen.
- In elk **2x2 blok** moet elk cijfer 1 tot en met 4 exact één keer voorkomen.
- De gegeven cijfers zijn **vaste** cellen: deze mag je niet meer wijzigen.

De startpuzzel in de code heeft exact één geldige oplossing.

## De aanpak

In `sudoku-opgave_2026.py` staat de klasse `SudokuSASolver`. De hulpmethodes krijg je cadeau:

- `_initialize_grid()` vult elke lege cel zodat elk 2x2 blok alle cijfers 1 tot en met 4 bevat.
- `_compute_cost(grid)` telt het aantal duplicaten in rijen en kolommen (kost = 0 betekent een perfecte oplossing).
- `_get_neighbor()` verwisselt twee niet-vaste cijfers **binnen een willekeurig 2x2 blok**.

Jouw taak is om in `solve()` de kern van simulated annealing te implementeren, net zoals bij de TSP-oefening, met een kleine aanpassing: **check vroegtijdig of de huidige oplossing al perfect is (kost = 0) en stop dan.**
Pas de temperatuur aan door dit stukje code : `temperature *= self.alpha`. Zorg dat er macimum `max_iter` iteraties plaatsvinden.

Je mag extra hulpmethodes toevoegen als dat nodig is. De eindgebruiker wil in de console zien wat er gebeurt (bv. de beste kost of het finale bord). Hoe je dit precies laat printen kan je zelf kiezen.

## Indicatieve puntenverdeling (totaal 20p)

- Vroegtijdig stoppen indien opgelost - 4p
- implementatie rest algoritme: 14p
- Resultaat wordt op een duidelijke manier geprint - 2p
