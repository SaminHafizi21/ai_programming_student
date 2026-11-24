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
| 6 | Trainingstijd (5 variabelen) | 20 min |

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

## Oefening 6: Trainingstijd (5 variabelen)

Een coach verdeelt **exact 25 trainingsuren** over **5 disciplines**: kracht (`k`),
snelheid (`s`), uithouding (`u`), lenigheid (`l`) en balans (`b`). De atleet wil
zijn ideale profiel **zo dicht mogelijk** benaderen. Dat ideale profiel is (in uren):

```
t = [8, 6, 5, 6, 5]
```

Merk op: het doelprofiel somt tot 30 uur, maar er zijn maar 25 uur beschikbaar.
Het doel is dus **onbereikbaar** en daar gaat OSQP het werk doen.

We minimaliseren de som van de kwadratische afwijkingen:

```
min ||x - t||²  =  min (k-8)² + (s-6)² + (u-5)² + (l-6)² + (b-5)²
```

met `x = [k, s, u, l, b]`.

### Stap 1: matrices opstellen

Elke afstand (`k-8`, `s-6`, ...) telt apart, dus de matrix `A` in `||A x - t||²`
is hier gewoon de eenheidsmatrix `I`. Zoals in het stappenplan voor type 2:

```
P = 2 · AᵀA = 2 · I
q = -2 · Aᵀt = -2 · t
```

Implementeer `verdeling_matrices(doelen)` die `(P, q)` teruggeeft.

### Stap 2: randvoorwaarden en oplossen

- Elke discipline tussen 0 en 10 uur, dus `0 ≤ xᵢ ≤ 10`.
- Het totaal is exact 25 uur, dus `k + s + u + l + b = 25`.

Implementeer `optimaliseer_verdeling(doelen, grenzen, totaal)` die de 5 uren
`[k, s, u, l, b]` teruggeeft, met `grenzen` een lijst van `(min, max)` per
discipline.

### Stap 3: controleer je oplossing

Omdat het doel telt tot 30 en er maar 25 uur is, verdeelt OSQP het tekort van
`25 - 30 = -5` uur evenredig over de 5 disciplines: elke discipline krijgt
`-5 / 5 = -1` uur. Geen enkele grens (`0 ≤ x ≤ 10`) wordt actief, dus:

```
x = [7, 5, 4, 5, 4]
```

De kwadratische afwijking is dan `(-1)² + (-1)² + (-1)² + (-1)² + (-1)² = 5`.

---

## Klaar?
- Commit. Beschrijf kort hoe P en q voor oefening 4 tot stand komen.
