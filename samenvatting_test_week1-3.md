# Samenvatting AI Programming — voorbereiding test (week 1–3)

Bronnen: `course-text/01–03`, `slides/Slides_AI_Programming_les1.md`, `slides/Slides_AI_Programming_week03_zoekalgos.md`, `exercises/week01–03`.

> ⚠️ Labo-opdrachten/tests maak je **zonder AI-tools**. Je moet de code dus zelf kunnen schrijven: oefen de code-sjablonen hieronder **uit je hoofd**.

---

## DEEL 1 — Intelligente agents (H1)

### Basisbegrippen
| Begrip | Betekenis |
|---|---|
| **AI** | Rationele entiteiten die acties kiezen om een performantiemetriek te maximaliseren |
| **Narrow AI** | Eén specifieke taak goed (= deze cursus) |
| **AGI** | Alle menselijke intellectuele taken |
| **ML** ⊂ AI | Systemen die beter worden met ervaring |
| **Deep Learning** ⊂ ML | Gebaseerd op neurale netwerken |
| Dit vak | Algoritmes met **specifieke logica**, *niet* ML |

### Agentmodel
```
Omgeving --(sensors)--> AGENT (agent program) --(actuators)--> Omgeving
```
- **Sensors** observeren, **agent program** beslist, **actuators** ageren.
- Sensors **én** actuators kunnen falen. Voorbeeld: **Boeing 737 MAX**: één foutieve sensor (AoA) = *single point of failure*, 2 crashes, ±350 doden. Les: **redundantie** + intern redeneren over je sensoren.

### Agent function vs. agent program
- **Agent function** = theoretisch: een **state-action tabel** voor elke mogelijke input-reeks.
  - Onhaalbaar groot: schaken ±**10¹⁵⁴** entries (atomen in het universum ±**10⁸⁰**). Het is een "fata morgana".
- **Agent program** = de **concrete code** die de agent function benadert, geschreven voor een **agent architecture** (een specifieke set sensors/actuators).
- **Taak van AI** = een agent program ontwerpen. (Beeldherkenning heeft geen zin zonder camera!)

### Rationele agent
- Handelt zo dat de **doelfunctie (performance measure)** gemaximaliseerd wordt.
- Gebruikt **geobserveerde data + ingebouwde kennis**.
- **Rationeel ≠ alleswetend!**
- Kan **leren** uit de historiek en werkt **autonoom**.
- Voorbeeld: een grasmaaier die in rondjes rijdt en stukken overslaat is **niet** rationeel. Doelfunctie = % gemaaid gras.

### PEAS (task environment)
| | | Voorbeeld robotmaaier |
|---|---|---|
| **P** | Performance measure | Gras maaien, veiligheid, weinig energie, weinig menselijke tussenkomst |
| **E** | Environment | Grasveld, bomen, dieren, weer |
| **A** | Actuators | Sturen, wielen, maaier aan/uit, waarschuwingslicht |
| **S** | Sensors | Grashoogte, wielweerstand, navigatie, batterij, nabijheid, temperatuur |

👉 **Oefen**: maak zelf een PEAS voor een zelfrijdende auto, een stofzuigrobot en een schaakcomputer.

### Soorten omgevingen (6 assen), KENNEN MET VOORBEELDEN
| As | Opties | Voorbeelden |
|---|---|---|
| Observeerbaarheid | Volledig / Partieel | Schaken, Go / **Poker**, Patience |
| Aantal agents | Single / Multi (competitief of coöperatief) | Kruiswoordraadsel / Schaken (comp.), zelfrijdende auto's (coöp.) |
| Zekerheid | Deterministisch / Stochastisch | Schaken / Mens-erger-je-niet, Monopoly (dobbelsteen) |
| Tijdsverloop | Episodisch / Sequentieel | Schaar-steen-papier, roulette / Lotto zonder teruglegging |
| Dynamiek | Statisch / Dynamisch / **Semi-dynamisch** | Puzzel / Racespel / Schaken **met klok** (enkel score verandert met tijd) |
| Waarden | Discreet / Continu | Bordspellen / Autonoom rijden (camera is strikt discreet, 256³ kleuren, maar praktisch continu) |

### Soorten agent programs
| Type | Kenmerk | Voorbeeld |
|---|---|---|
| **1. Simple reflex** | Enkel **huidige** input, IF→THEN-regels, **geen geheugen** | Hand terugtrekken van vuur; sphex-wesp. Faalt bij **partieel observeerbare** omgevingen |
| **2. Model-based reflex** | **Interne state** (geheugen) + **transition model** (effect van eigen acties) + **sensor model** (hoe de omgeving in metingen terechtkomt) | Maaier met kaart; stofzuigrobot; self-driving car die vorige afstand onthoudt |
| **3a. Goal-based** | Kent een **einddoel**, zoekt states dichter bij het doel | Pad Antwerpen → Parijs vinden |
| **3b. Utility-based** | **Utility-functie** die elke tussenpositie een score geeft en die gemaximaliseerd wordt | utility = **−d(huidige, nieuwe stad)** → kies kleinste afstand |

**Typische examenvraag:** *Waarom is een simple reflex agent gevaarlijk bij de Boeing?* → Hij vertrouwt blind op één huidige meting; geen geheugen om een sensor als defect te herkennen. Een model-based agent onthoudt vorige waarden en kan de inconsistente sensor uitsluiten.

---

## DEEL 2 — Sorteren & complexiteit (H2)

### Big O
| Notatie | Betekenis bij 2× zoveel input |
|---|---|
| O(1) | even snel |
| O(n) | 2× trager |
| O(n²) | 4× trager |
| O(n log n) | iets meer dan 2×, efficiënt |
| O(bᵈ) | b = branching factor, d = diepte → explodeert |

Big O vergelijkt **tijd** én **geheugen (space complexity)**.

### Sorteeralgoritmes
| Algoritme | Idee | Tijd (worst) | Geheugen | Stabiel |
|---|---|---|---|---|
| **Bubble sort** | Buren wisselen, herhalen | O(n²) | O(1) | ✅ |
| **Insertion sort** | Zoals kaarten in je hand: element invoegen in gesorteerd deel | O(n²) (best O(n) bij gesorteerde lijst) | O(1) | ✅ |
| **Merge sort** | Verdeel-en-heers, recursief splitsen + mergen | O(n log n) | O(n) | ✅ |
| **Quicksort** | Pivot, partitioneren | O(n log n) gemiddeld | | |
| **Tree sort** | Voor lijsten waar items worden toegevoegd | | | |
| **Timsort** (2002) | Standaard in Python & Java | O(n log n) | | |

### 🔑 Insertion sort: UIT JE HOOFD KENNEN
```python
def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        key = sequence[i]
        j = i - 1
        while j >= 0 and sequence[j] > key:
            sequence[j + 1] = sequence[j]   # schuif op naar rechts
            j -= 1
        sequence[j + 1] = key               # zet key op juiste plek
    return sequence
```
Manueel trace oefenen: `[5, 2, 4, 6, 1, 3]` → `[2,5]` → `[2,4,5]` → `[2,4,5,6]` → `[1,2,4,5,6]` → `[1,2,3,4,5,6]`.
Test-randgevallen: `[]`, `[42]`, al gesorteerd, omgekeerd, duplicaten.

### Bubble sort
```python
def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq
```

### Merge sort (idee)
1. Lijst > 1 element? Splits in `left = seq[:mid]`, `right = seq[mid:]`.
2. Recursief `merge_sort(left)`, `merge_sort(right)`.
3. Merge met 3 pointers `p, q, r`: kleinste van beide vooraan nemen, daarna de restjes kopiëren.

### Timen (decorator)
```python
from time import time
def timer_func(func):
    def wrap(*args, **kwargs):
        t1 = time(); result = func(*args, **kwargs); t2 = time()
        return result, t2 - t1
    return wrap
```

---

## DEEL 3 — Zoekalgoritmes (H3)

### Een zoekprobleem bestaat uit
1. **State space** (eindig)
2. **Initiële state**
3. Minstens één **goal state**
4. **Acties** + **transitiemodel** (resultaat van elke actie is gekend)
5. **Actie-kostfunctie**

- Volledig observeerbaar + deterministisch → oplossing = **pad** (reeks acties).
- **Optimale oplossing** = pad met **laagste totale kost**.
- Stappen: doel formuleren → probleem formuleren → zoeken → uitvoeren.
- "Vindalgoritme" is eigenlijk een betere naam.

**Voorbeeld Antwerpen → Parijs:** states = steden, initial = Antwerpen, goal = Parijs, acties = naar verbonden stad rijden, transitiemodel = graaf, kost = afstand/reistijd/energie/CO₂/combinatie.

### Ongeïnformeerd vs. geïnformeerd
| Ongeïnformeerd | Geïnformeerd |
|---|---|
| Kent enkel de graaf, algemeen | Kent ook een **heuristiek**, sneller maar specifieker |
| BFS, DFS, Dijkstra | Best-first (greedy), A* |

- **Search tree**: opgebouwd uit de state graph; kinderen = direct verbonden states.
- **Frontier**: bereikte, nog niet opengeklapte nodes.
- **Explored/visited**: al opengeklapte nodes (voorkomt lussen).

### BFS vs DFS (kennen!)
| | **BFS** | **DFS** |
|---|---|---|
| Datastructuur | **Queue (FIFO)**: `deque.popleft()` | **Stack (LIFO)**: `list.pop()` of recursie |
| Volgorde | Niveau per niveau | Eerst de diepte in |
| Volledig | Ja, systematisch | Ja (eindige graaf met visited), niet optimaal |
| Optimaal | **Ja, als alle kosten gelijk zijn** (minst aantal stappen) | **Nee** |
| Geheugen | **Veel** | **Weinig** |
| Complexiteit | **O(bᵈ)** | Afhankelijk van het pad |

⚠️ BFS vindt het pad met de **minste steden**, niet per se de **kortste in km**. Daarvoor heb je **Dijkstra** nodig.
BFS-pad in de slides: Antwerpen → Gent → Brussel → Namen → Luxemburg → Metz → Dijon → Parijs.

### 🔑 BFS met pad-reconstructie (parent-tracking)
```python
from collections import deque

def bfs(start, goal, neighbors):
    frontier = deque([start])
    parent = {start: None}            # dient ook als 'explored'
    while frontier:
        node = frontier.popleft()     # FIFO
        if node == goal:
            path = []
            while node is not None:   # terugwandelen via parents
                path.append(node)
                node = parent[node]
            return path[::-1]
        for nb in neighbors(node):
            if nb not in parent:
                parent[nb] = node
                frontier.append(nb)
    return None
```

### 🔑 DFS met stack (maze)
```python
def dfs(start, goal, neighbors):
    stack = [(start, [start])]        # node + pad tot daar
    visited = set()
    while stack:
        node, path = stack.pop()      # LIFO
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for nb in neighbors(node):
            if nb not in visited:
                stack.append((nb, path + [nb]))
    return None
```

**Maze `valid_moves`**: 4 richtingen `(±1,0),(0,±1)`, check binnen grid (`0 <= r < rows`, `0 <= c < cols`) en geen muur `'#'`.

### 🔑 Dijkstra (gewogen graaf, kortste pad)
Idee: neem telkens de onbezochte node met **laagste gekende afstand**, update buren als je een korter pad vindt.
```python
import heapq

def dijkstra(graph, start, goal):          # graph[u] = [(v, kost), ...]
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        dist, node, path = heapq.heappop(pq)   # kleinste afstand eerst
        if node == goal:
            return dist, path
        if node in visited:
            continue
        visited.add(node)
        for nb, w in graph[node]:
            if nb not in visited:
                heapq.heappush(pq, (dist + w, nb, path + [nb]))
    return None
```
- Dijkstra = BFS als alle gewichten gelijk zijn.
- **A\***: zelfde code, maar prioriteit **f = g + h** (g = kost tot nu, h = heuristiek tot doel, bv. vogelvlucht of Manhattan).
- **Greedy best-first**: prioriteit = enkel h → snel maar niet optimaal.

### Schuifpuzzel (8-puzzle)
- **State** = configuratie (3×3, `0` = leeg vakje). **Doel** = `[[1,2,3],[4,5,6],[7,8,0]]`.
- **Acties** = leeg vakje omhoog/omlaag/links/rechts schuiven.
- `possible_new_configurations()`: zoek positie van 0, voor elke geldige richting kopieer het bord (**deepcopy!**) en wissel 0 met de buur.
- **Heuristiek: Manhattan-distance** = Σ over tegels (niet 0) van `|rij_doel − rij| + |kol_doel − kol|`.
- Voor `visited`: zet het bord om naar iets **hashbaars**, bv. `tuple(tuple(r) for r in board)`.

```python
def manhattan(board):
    total = 0
    for r in range(3):
        for c in range(3):
            v = board[r][c]
            if v != 0:
                gr, gc = (v - 1) // 3, (v - 1) % 3
                total += abs(gr - r) + abs(gc - c)
    return total
```

---

## DEEL 4 — Labo-patronen (week 1–2) die je moet kunnen schrijven

### Floor cleaning agent (model-based reflex)
- Grid **10 kolommen × 5 rijen**, start linksboven (0,0).
- Interne state: `x, y` + 2D-grid vuil/proper.
- `move_up/down/left/right` **met grenscontrole**; `clean_tile()` markeert proper.
- Strategie **zigzag**: even rijen naar rechts, oneven rijen naar links.
```python
for row in range(self.rows):
    cols = range(self.cols) if row % 2 == 0 else range(self.cols - 1, -1, -1)
    for col in cols:
        self.move_to(row, col)
        self.clean_tile()
```

### Self-driving car (model-based reflex)
- Interne state: `vorige_afstand`.
- `snelheid = vorige − huidige` (positief = komt dichter).
- Als `snelheid > 0` en `afstand / snelheid < 5` → `Brake()`, anders `Nothing()`. **Update de vorige afstand!**

### Foute sensor / Boeing (model-based + sensor model)
- Beide sensoren `|A − B| < TOLERANCE` → gemiddelde.
- Uiteenlopend → vertrouw de sensor die het dichtst bij de **vorige waarde** ligt (`abs`), markeer de andere als verdacht (interne state) en negeer die voortaan.
- Daling > 10 m tussen metingen → corrigeren.

### Routeplanner (utility-based, greedy)
- `utility(a, b) = -afstand(a, b)`.
- `choose_next`: onbezochte buur met **max utility** (`max(..., key=...)`), anders `None`.
- Greedy is **niet optimaal**: kan in doodlopende weg of langere route belanden, want hij kijkt maar 1 stap vooruit. Daarom heb je Dijkstra nodig.

---

## Zelftest: vragen (antwoorden onderaan)
1. Wat is het verschil tussen agent function en agent program?
2. Geef PEAS voor een zelfrijdende taxi.
3. Classificeer **poker** op de 6 assen.
4. Wat is semi-dynamisch? Geef een voorbeeld.
5. Waarom faalt een simple reflex agent in een partieel observeerbare omgeving?
6. Wat heeft een model-based agent wat een simple reflex agent niet heeft? (3 dingen)
7. Verschil goal-based vs. utility-based?
8. Lijst verdubbelt: hoeveel trager is O(n²)? En O(n)?
9. Welk sorteeralgoritme heeft O(n) in het beste geval en wanneer?
10. Welke datastructuur gebruiken BFS en DFS?
11. Wanneer is BFS optimaal? Wanneer niet?
12. Waarom gebruikt DFS minder geheugen?
13. Wat is de vijfdelige definitie van een zoekprobleem?
14. Wat is f in A*? Wat gebeurt er als h = 0?
15. Waarom is de greedy routeplanner geen vervanging voor Dijkstra?

<details>
<summary>Antwoorden</summary>

1. Function = theoretische, gigantische state-action tabel; program = concrete code voor een architectuur die de function benadert.
2. P: veilig, snel, comfortabel, legaal, winst. E: wegen, verkeer, voetgangers, weer. A: stuur, gas, rem, richtingaanwijzer, claxon. S: camera, LIDAR, GPS, snelheidsmeter, radar.
3. Partieel observeerbaar, multi-agent (competitief), stochastisch, sequentieel, statisch, discreet.
4. Omgeving verandert niet, maar de performantiescore wel met de tijd: schaken met klok.
5. Hij heeft geen geheugen en kan dus niets onthouden over wat hij nu niet ziet.
6. Interne state, transition model, sensor model.
7. Goal: enkel "doel bereikt of niet". Utility: score voor elke (tussen)state, die je maximaliseert.
8. 4× trager; 2× trager.
9. Insertion sort, bij een al gesorteerde lijst.
10. BFS: queue (FIFO). DFS: stack (LIFO) / recursie.
11. Optimaal als alle actiekosten gelijk zijn; niet bij verschillende kosten (km).
12. Het onthoudt maar één pad (+ zijtakken), niet een heel niveau van de boom.
13. State space, initiële state, goal state(s), acties + transitiemodel, actie-kostfunctie.
14. f = g + h; met h = 0 wordt A* gewoon Dijkstra.
15. Greedy kijkt maar 1 stap vooruit en garandeert geen kortste of zelfs geen geldig pad; Dijkstra wel.
</details>

---

## Studieplan (± 1 week)
| Dag | Wat |
|---|---|
| 1 | Deel 1 (agents) lezen + PEAS en omgevingsclassificatie oefenen |
| 2 | Deel 2: insertion/bubble sort **uit het hoofd** schrijven op papier en in Python, merge sort tracen |
| 3 | Deel 3: BFS & DFS met de hand tracen op de stedengraaf, daarna coderen zonder te kijken |
| 4 | Dijkstra + A* coderen, schuifpuzzel `possible_new_configurations` + Manhattan |
| 5 | Labo's week 1–3 opnieuw maken **zonder hulp**, met `pytest tests/test_week01.py` enz. controleren |
| 6 | Zelftest + zwakke punten herhalen |
