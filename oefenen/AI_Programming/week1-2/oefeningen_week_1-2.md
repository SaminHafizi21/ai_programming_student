# Oefeningen Labo 1 en 2

## Agents

- Wat is een agent ? Wat is rationaliteit ?

    Een agent is een programma dat info binnekrijgt via sensors en met die info de situatie probeert te verbeteren.

    rationaliteit in een agent is dat de agent probeert zijn doelfunctie te maximaliseren adhv de inputs.

- Stel voor volgende taken een POAS beschrijving op

    (a) Een gymnastische oefening uitvoeren op een trampoline. 

        P - Correcte uitvoering, geen botten breken.
        O - Trampoline.
        A - Benen, armen, rug
        S - Ogen, proprioceptie

    (b) De oceanen ontdekken. 
    
        P - Onbekende oceaan zien.
        O - Oceaan.
        A - Sturen, locatie bepalen.
        S - Ogen, GPS

    (c) Voetbal spelen.  

        P - Zo veel mogelijk scoren/zo weining mogelijk ballen binnenlaten.
        O - Voetbalveld.
        A - Benen, voeten.
        S - Ogen.

    (d) Automatisch gebruikte AI boeken vinden op het internet. 

        P - Gebruikt AI boek vinden.
        O - Internet.
        A - 

    (e) Tennis spelen tegen een muur.  

    (f) Een hoge sprong uitvoeren.  

    (g) Op een veiling bieden op een item.
- Veronderstel dat we een thermostaat hebben die de verwarming opzet wanneer de temperatuur minstens 3 graden kouder is dan een instelling en die de verwarming afzet wanneer de temperatuur minstens 3 graden warmer is dan die instelling. Is deze thermostaat een eenvoudige reflex agent, een model-based reflex agent of een goal-based agent? 

## Floor cleaning agent
- Bepaal voor volgende probleem een model-based reflex agent, die dus een interne state heeft, een transition model, sensormetingen kan doen en de state kan updaten. Het probleem is een tegenvloer in een woonkamer die moet worden gestofzuigd door een robotstofzuiger. Je krijgt volgende informatie:
    - Een tegel is altijd vuil of proper.
    - De stofzuiger is exact even groot en kuist precies 1 tegel
    - De stofzuiger kan ofwel zich verplaatsen, ofwel stofzuigen, ofwel blijven staan
    - De stofzuiger kent de ruimte (10 op 5 tegels) en weet dat hij in de hoek start, bij het laadstation
    - Uitbreidingen:
        - tegels zijn na 7 dagen niet poetsen zeker vuil
        - er kunnen obstakels op een tegel staan (de robot kan die met een bumper voelen, niet van ver zien)
        - de stofzuiger kent de ruimte niet, maar voelt met zijn bumper de muren - die je net als een obstakel kan aangeven door een 2D matrix te geven met bepaalde entries met een kruisje op, of het woord 'wall' of dergelijke
- Implementeer in Python een klasse die de interne state van deze robot voorstelt en alles wt de robot nodig heeft om deze ruimte te kuisen. Voorzie een methode `clean()`, `move_down()`, `clean_tile()`, ... Bedenk een goede strategie. Er zijn heel simpele strategiëen die zullen werken. Voorzie wat testcode om je werk te demonstreren.

## Self Driving car
Bouw je eigen model-based reflex agent (in Python) en pas het toe op het volgende probleem. Je agent moet zijn voorligger volgen op 10m afstand. Ga ervan uit dat er een LIDAR sensor ter beschikking is die als perceptie op elk moment de afstand toont tot je voorligger. De actuatoren ter beschikking geven de mogelijkheid om extra gas bij te geven of te remmen. Je moet remmen als de tijd tot collisie (botsing) minder dan 5 seconden is.

## Sortering

- Implementeer een klasse in python die lijsten kan sorteren. Opgelet, je schrijft zelf de sorting, en maakt dus geen gebruik van interne sorteringslibraries.
    - implementeer Insertion Sort: Hierbij wordt elk nieuw item dat wordt toegevoegd aan een lijst meteen op de juiste plaats gestoken, zo wordt een lijst item per item gesorteerd
    - implementeer Quick Sort. Bij Quick Sort kies je uit je ongeordende lijst een element (de zogenaamde pivot), en je maakt nu 2 deellijsten: de items kleiner dan de pivot, en de items groter dan de pivot. Vervolgens ga je deze 2 deellijsten op dezelfde manier ordenen.
    - vergelijk voor lijsten met 10, 100, 1000 en 100 000 items de snelheid van sortering tussen beiden.


