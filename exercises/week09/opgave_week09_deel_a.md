# Week 9 - Oefeningen: Lineair Programmeren met OSQP (deel A)

## Leerdoelen
- Je stelt een **quadratic programming**-probleem op als matrices.
- Je gebruikt **OSQP** om een optimalisatie op te lossen.
- Je zet een opgave met enkel bovenlimieten om naar de vorm `l ≤ A x ≤ u`.

> Volg eerst het algemene stappenplan in `stappenplan_osqp.md`. Het vertelt je
> hoe je het juiste kostfunctietype herkent en hoe je elke opgave naar matrices
> omzet.

## Overzicht

| # | Oefening | Tijd |
|---|----------|------|
| 1 | OSQP basis | 20 min |
| 2 | `Gx ≤ h` omzetten | 20 min |
| 3 | Fabrieksoptimalisatie | 25 min |

---

## Oefening 1: OSQP basis

Open `osqp_start.py`. OSQP lost problemen op van de vorm:

```
Minimaliseer:  ½ xᵀ P x + qᵀ x
met:           l ≤ A x ≤ u
```

Los het standaardvoorbeeld uit de cursus op:

```python
P = [[4, 1], [1, 2]]
q = [1, 1]
A = [[1, 1], [-1, 2], [2, 1]]
l = [1, 0, 2]
u = [2, 2, 3]
```

Gebruik `csc_matrix(P)` voor sparse matrices. Implementeer `solve_qp(P, q, A, l, u)` zodat die de optimale `x` teruggeeft.

---

## Oefening 2: `Gx ≤ h` omzetten

Soms wordt een probleem gegeven met enkel bovenlimieten: `G x ≤ h`. OSQP verwacht
`l ≤ A x ≤ u`, dus moeten we zelf nog een ondergrens voorzien.

Implementeer `solve_linear(c, G, h)` die het volgende oplost:

```
Minimaliseer:  cᵀ x
met:           G x ≤ h  en  x ≥ 0
```

Stappenplan:
1. Er is geen kwadratisch deel, dus `P` is een vierkante nul-matrix.
2. De vector `q` is `c` (het lineaire deel).
3. `A` is `G`, maar de rijen van `G` hebben geen ondergrens: vul `l` daar met `-∞`.
4. Voeg voor elke variabele een rij toe met `0 ≤ xᵢ ≤ +∞` (gebruik een eenheidsmatrix).
5. Los op met OSQP. Daarna leer je te herkennen of een probleem überhaupt een oplossing heeft.

---

## Oefening 3: Fabrieksoptimalisatie

Een bedrijf maakt twee producten:

- **AquaSparkle**: 2 eenheden X, 1 eenheid Y, winst €5
- **BioBurst**: 1 eenheid X, 3 eenheden Y, winst €8

Voorraad: 100 X, 90 Y.

We zoeken het aantal AquaSparkles `a` en BioBursts `b` dat de winst maximaliseert.

Maak een klasse `FabriekOptimizer` die bij initialisatie de parameters kan aanpassen:

- `x_limit`: beperking op de voorraad X
- `y_limit`: beperking op de voorraad Y
- `profit_a`: winst per AquaSparkle
- `profit_b`: winst per BioBurst

De methode `optimize()` stelt de matrices op en geeft `(a, b)` terug.

Hint: om winst te **maximaliseren** minimaliseer je `-(5a + 8b)`. De beperkingen zijn
`2a + b ≤ 100`, `a + 3b ≤ 90` en `a, b ≥ 0`.

Wat is het optimale productieplan?

---

## Klaar?
- Commit. Werk daarna deel B af (kwadratische kost en 'dichtste bij').
