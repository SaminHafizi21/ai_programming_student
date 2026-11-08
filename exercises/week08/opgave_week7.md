# Week 7 — Oefening: Mini Othello met Minimax & Utility

## Leerdoelen
- Je gebruikt een bestaande **Othello**-spelcode.
- Je implementeert een **minimax** met **evaluatiefunctie** (utility).
- Je laat de computer spelen met depth-limited search.

## Overzicht

| # | Oefening | Tijd |
|---|----------|------|
| 1 | Random move | 15 min |
| 2 | Evaluatiefunctie | 20 min |
| 3 | Minimax met depth | 45 min |

---

## De code

Open `othello_start.py`. Het bord-gedeelte is al geschreven:

- `is_valid_move(row, col, player)`
- `make_move(row, col, player)`
- `count_pieces()`
- `opponent()`

Jij voegt de **AI** toe.

## Stappenplan

### Stap 1: Random move
Implementeer `random_move()`: kies een **geldige** zet via `random.shuffle()` over alle velden.

### Stap 2: Evaluatiefunctie
Schrijf `evaluate(player)` die een score geeft:

- Begin met `count_pieces()`: `(eigen_stenen - opponent_stenen)`.
- Probeer minimaal deze uitbreiding: tel **mobiliteit** (aantal geldige zetten) mee.

### Stap 3: Minimax
Schrijf `minimax(self, depth, is_maximizing)`:

- Diepte 0 of einde → `evaluate()`.
- Max-knoop: max over `<zelf>_move()`, Min-knoop: min over `opponent_move()`.
- Belangrijk: roep de zetmethodes **simuleren** op een kopie van het bord (of pas aan/werk terug).

### Stap 4: Best move
Schrijf `best_move()` die alle geldige zetten evalueert en de beste kiest.

### Stap 5: Pas `play()` aan
Laat speler `'X'` de computer zijn (met `best_move()`), `'O'` de mens.

### Stap 6: Experimenteer met depth
Test `best_move()` met depth 2, 3, 4. Hoe diep kan de computer praktisch denken in Othello?

---

## Klaar?
- Commit. Bekijk **week 8** (linear programming).