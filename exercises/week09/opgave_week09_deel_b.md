# Week 9 - Oefeningen: Kwadratische kost en 'dichtste bij' (deel B)

## Leerdoelen
- Je vertaalt een **kwadratische kostenfunctie** naar de `P`- en `q`-matrices.
- Je herkent een **'dichtste bij'-probleem**: je minimaliseert de afstand tot een doel.
- Je bouwt een **wrapper-klasse** rond OSQP voor een specifiek probleem.

> Volg eerst het algemene stappenplan in `stappenplan_osqp.md`. Het vertelt je
> hoe je het juiste kostfunctietype herkent en hoe je elke opgave naar matrices
> omzet.

## Overzicht

| # | Oefening | Tijd |
|---|----------|------|
| 4 | Macronutriënten | 35 min |
| 5 | Portefeuille-optimalisatie | 30 min |

---

## Oefening 4: Macronutriënten in maaltijden

Een topatleet wil een maaltijd samenstellen die zo dicht mogelijk bij een gewenste
verhouding van macronutriënten ligt. De beschikbare ingrediënten zijn broccoli (`B`),
kalkoenfilet (`K`) en aardappelen (`A`). De hoeveelheden worden in eenheden van
100 gram uitgedrukt.

Per 100 g:

| Ingrediënt | proteïne | koolhydraten | vet |
|-----------|----------|--------------|-----|
| Broccoli  | 2.8 | 7 | 0.4 |
| Kalkoen   | 29  | 0 | 7   |
| Aardappel | 2   | 17 | 0.1 |

Doelen: `P = 37`, `C = 41`, `F = 20`.

We minimaliseren de som van de kwadratische afwijkingen:

```
|| doelen - N x ||²
```

met `N` de nutriëntmatrix (3 variabelen, 3 macro's) en `x = [x_B, x_K, x_A]`.

### Stap 1: matrices opstellen
Merk op dat `||t - Nx||² = xᵀ Nᵀ N x - 2 tᵀ N x + const`, dus:

```
P = 2 · (Nᵀ N)
q = -2 · (Nᵀ t)
```

Implementeer `maaltijd_matrices(nutriënten, doelen)` die `(P, q)` teruggeeft.

### Stap 2: randvoorwaarden en oplossen
- Hoeveelheden zijn niet-negatief.
- De atleet eet in totaal exact 700 g, dus `x_B + x_K + x_A = 7`.
- Broccoli tussen 2 en 3, kalkoen tussen 1 en 2, aardappelen tussen 2 en 4 (in 100 g).

Implementeer `optimize_meal(nutriënten, doelen, grenzen, totaal=7.0)` die `(x_B, x_K, x_A)`
teruggeeft, met `grenzen` een lijst van `(min, max)` per ingrediënt.

---

## Oefening 5: Portefeuille-optimalisatie

Open `portfolio_start.py`. We verdelen een budget over meerdere aandelen. De
portefeuille wordt beschreven door gewichten `w` (één per asset). Het risico is de
gewogen variantie `wᵀ Σ w`, met `Σ` de covariance-matrix.

Bouw een wrapper-klasse `PortfolioOptimizer` rond OSQP:

- `__init__(expected_returns, covariance_matrix)`: sla de gegevens op.
- `fit()`: minimaliseer het risico `wᵀ Σ w` met als randvoorwaarden
  `Σ wᵢ = 1` en `0 ≤ wᵢ ≤ 1`, en geef `w` terug.

Dit is een **'dichtste bij'-probleem**: we zoeken de portefeuille met het minste
risico, gegeven dat al ons geld belegd moet zijn.

---

## Klaar?
- Commit. Beschrijf kort hoe P en q voor oefening 4 tot stand komen.
