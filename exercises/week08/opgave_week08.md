# Week 7-8 — Oefening: Othello, Monty Hall en TicTacToe met Expectimax

## Leerdoelen
- Je gebruikt een bestaande **Othello**-spelcode en voegt een **minimax** met
  **evaluatiefunctie** (utility) toe.
- Je implementeert het **Monty Hall**-probleem met een **simulatie**.
- Je breidt **minimax** uit naar **expectimax** met een **chance-knoop** voor
  TicTacToe.

## Overzicht

| # | Oefening | Tijd |
|---|----------|------|
| 1 | Othello: random move, evaluate, minimax | 45 min |
| 2 | Monty Hall: simulatie | 30 min |
| 3 | TicTacToe met expectimax (kans-element) | 45 min |

---

# Oefening 1: Othello met Minimax & Utility

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

# Oefening 2: Monty Hall

## De code

Open `montyhall_opgave.py`. Vouw de klasse `MontyHallGame` uit:

- `__init__(self)`: drie deuren (`'geit', 'geit', 'auto'`), geschud met
  `random.shuffle`. Houd de keuze van de speler en de onthulde deur bij.
- `choose_door(door_number)`: accepteer 0, 1 of 2; andere getallen worden genegeerd.
- `host_reveal()`: geef een deur vrij die een geit heeft, maar **niet** de keuze van de speler.
- `switch_choice()`: laat de speler wisselen naar de enige overblijvende dichte deur.
- `is_player_winner()`: controleer of er een auto achter de gekozen deur staat.
- `play_game(switch=False)`: speel een volledig spel en geef een bool terug.

## Stappenplan

### Stap 1: Implementeer de spelmechanica
Vul `choose_door`, `host_reveal`, `switch_choice` en `is_player_winner` in en
test met de functie `test()`.

### Stap 2: Simulatie (expectimax)
Schrijf `expectimax_simulation(switch)` die het spel `num_simulations` keer
simuleert en het **winstpercentage** teruggeeft. Voeg indien nodig een
parameter `num_simulations` toe.

### Stap 3: Vergelijk
Implementeer `compare()`: bereken het winstpercentage met en zonder wisselen en
print beide. Wat is de beste strategie?

**Vraag:** waarom is wisselen (of niet) in je voordeel? Hoe zit het verwachte
resultaat in elkaar (vergelijk met een verwachte waarde)?

---

# Oefening 3: TicTacToe met Expectimax (kans-element)

## De code

Open `tictactoe_expectimax_start.py`. Het bord-gedeelte is al geschreven:

- `make_move(x, y, player)`
- `is_valid_move(x, y)`
- `evaluate()` (1 = X wint, -1 = O wint, 0 = gelijkspel)
- `is_full()`, `number_empty()`, `copy()`

Jij voegt de **AI** toe.

## Achtergrond: waarom een kans-element?

Bij een **perfecte** tegenstander kiest die steeds de beste zet, dus gebruik je
**min** op de knopen van de tegenstander. Maar de tegenstander kan ook
**willekeurig** spelen. Dan weet je niet welke zet er komt: je moet het
**gemiddelde** nemen over alle mogelijke zetten.

Dat heet een **chance-knoop**. Een boom met MAX-, MIN- en chance-knopen heet
**expectimax**.

## Stappenplan

### Stap 1: Random move
Implementeer `random_move()`: verzamel alle **lege** velden en kies er willekeurig
één uit via `random.shuffle()`.

### Stap 2: Minimax (MAX/MIN)
Zet eerst een gewone minimax neer in `minimax(depth, is_maximizing)`:

- Diepte 0 of einde van het spel → geef `evaluate()` terug.
- **MAX-knoop**: `max` over alle zetten van X.
- **MIN-knoop**: `min` over alle zetten van O.
- Belangrijk: simuleer elke zet op een **kopie** (`copy()`) zodat het bord niet
  wijzigt.

Test met `find_best_move()` die alle zetten evalueert en de beste kiest.

### Stap 3: Expectimax (chance-knoop)
Voeg de parameter `is_chance` toe. Bij `is_chance=True` speelt de tegenstander
**willekeurig**: neem het **gemiddelde** over alle mogelijke zetten.

```python
total = 0
aantal = 0
for elke lege cel:
    kopie = self.copy()
    kopie.board[i][j] = 'O'          # tegenstander zet willekeurig
    total += kopie.minimax(depth - 1, not is_maximizing, not is_chance)
    aantal += 1
return total / aantal               # gemiddelde over alle zetten
```

Let op: bij een chance-knoop mag je **geen** alpha-beta-pruning toepassen, want
een willekeurige tegenstander kiest niet de min- of max-zet maar elke zet even
vaak.

### Stap 4: Best move
Zorg dat `find_best_move()` de beste zet kiest op basis van expectimax.

### Stap 5: Afwisselend perfect/random
Pas `play()` aan zodat X de **computer** is en O de **mens**. Laat de computer
**afwisselend** een perfecte zet (`find_best_move()`) en een willekeurige zet
(`random_move()`) doen. De computer weet dat hij de volgende keer willekeurig
speelt en houdt daar via de chance-knoop rekening mee.

### Stap 6: Experimenteer
- Kun je winnen van deze computer? Verandert dat als de computer vaker random
  speelt?
- Wat gebeurt er als je de chance-knoop vervangt door een `min`?
- Vergelijk met de oplossing in een `modeloplossing` als je vast zit.

---

## Klaar?
- Commit. Kijk naar **week 9** (linear programming).