# Labo week 7-8 - Adversarial Search
# Tic Tac Toe verbeteringen
## Alpha beta pruning

Pas je code van Tic Tac Toe aan, zodat er ook alpha-beta pruning plaatsvindt. Je vindt een aanzet op de slides.

## Depth-limited minimax

### Depth parameter
Pas je code van Tic Tac Toe aan, zodat je wanneer je deze aanroept, je een maximale diepte kan aangeven. Wanneer die diepte is bereikt, dient het algoritme te stoppen en aan te geven dat het niet meer verder kan.

### Aanpassen evaluate functie
Pas de evaluatie functie aan, zodat als de maximale depth is bereikt, er toch een waarde kan worden teruggeven, zelfs al is de state niet terminaal. Geef in dat geval simpelweg 0 terug.

### Introduceer een kanselement in je spel
Pas je spelletje als volgt aan:
- de computer gaat nu in plaats van elke zet optimaal te kiezen, 1 zet optimaal kiezen, de volgende volledig willekeurig, dan terug optimaal, ... De computer weet dit van zichzelf. Maw in de implementatie van zijn ideale zet, houdt de computer rekening met het feit dat hij de volgende keer random gaat kiezen.
- je kan indien nodig `random.shuffle()` gebruiken om een lijst van opties door mekaar te haspelen
- Kijk of je kunt winnen van deze computer.

# Othello (reversi)

### Spelregels Othello
De spelregels van Othello vind je hier : https://www.mastersofgames.com/rules/reversi-othello-rules.htm. We spelen Othello, geen Reversi.

Bekijk de code die het spel Othello implementeert (Digitap `othello_opgave.py`). Pas de code aan zodat de computer door een AI-algoritme wordt bediend. Schrijf een minimax algoritme met depth-parameter, en een zinvolle evaluatiefunctie van de status van het bord. Test of het goed werkt bij verschillende depths.
### stappenplan
- schrijf eerst een code om een random move te doen (random, maar wel geldig!)
- pas vervolgens de `play` code aan zodat de computer hiermee speelt
- schrijf nu een minimax algoritme met depth parameter zodat je de computer 5 (of andere willekeurig getal) stappen diep kan laten kijken
- zorg dat de computer een 'best_move' kan kiezen op basis van deze minimax. Hoe diep kun je in de praktijk de computer laten vooruitkijken ?
- nu heb je een evaluatiefunctie nodig. `count_pieces` geeft al een eerste kandidaat. Maar er zijn nog andere kandidaten die je kan testen:
    - lorem
    - ipsum
    - dolor

# The Monty Hall Problem
Het Monty Hall probleem is een puzzel gabaseerd op een Amerikaanse spelshow uit de jaren '50. Op Wikipedia (https://nl.wikipedia.org/wiki/Driedeurenprobleem) kan je lezen: Stel dat je deelneemt aan een spelprogramma en je mag kiezen uit drie deuren: achter een van de deuren staat een auto, achter de andere twee staan geiten. Je kiest een deur, zeg nr. 1, en de presentator, die weet wat er achter de deuren staat, opent een andere deur, zeg nr. 3, met een geit erachter. Hij zegt dan tegen je: "Zou je deur nr. 2 willen kiezen?" Is het in je voordeel om van deur te wisselen? 

- Schrijf een klasse om de de staat van het spel voor te stellen. Vertrek van `montyhall_opgave.py`
- Als je implementatie goed werkt moet je de `test()` code goed kunnen uitvoeren.
- Schrijf de expectimax simulator. Die is losjes gebaseerd op het idee van expectimax, maar iets anders: We weten niet precies of het een goed idee is om te switchen of niet, dus we gaan die percentages door een simulatie proberen te achterhalen
    - in een simulatie laat je het Monty Hall probleem dan lopen, waarbij je aangeeft als parameter of je gaat wisselen of niet.
    - vergelijk de winstpercentages. Nu weet je wat de optimale strategie is voor deit probleem

Deze techniek (simulaties op grote schaal) gaan we volgende week verder bekijken.

# Extra oefening: andere spelletjes die je kan implementeren:

- Dammen 
- 3D chess (Star Trek, the Big Bang Theory):  https://bigbangtheory.fandom.com/wiki/Tri_Dimensional_Chess
- Go - https://en.wikipedia.org/wiki/Go_(game) 
- Nim (dit heb ik in de les tegen jullie gespeeld met stokjes)
- ...

# Extra: libraries om spelletjes fancier te maken
Je kan zelf eens kijken naar libraries als  `art` (ASCII art), `colorama` (kleurtjes), `tqdm` (progress bars, voor als berekeningen even duren), `curses` (cursor in terminal, maakt dingen wat vlotter).
