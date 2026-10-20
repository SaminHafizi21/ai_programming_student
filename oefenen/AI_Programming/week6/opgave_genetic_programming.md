# Oefeningen Genetic Programming

1. Herbekijk het Travelling Salesman Problem. Maak een nieuwe oplossing:
    - Representatie: elk individu is een mogelijke route
    - Fitness functie: de totaal afgelegde afstand, dewelke je wil minimaliseren
    - Crossover: kijk naar order crossover (OX), of partially mapped crossover (PMX) - zelf op te zoeken
    - Mutatie: het wisselen van steden kan je houden als een mutatie
2. Knapsack problem:
Het Knapsack probleem is een optimalisatieprobleem waarbij een set voorwerpen, elk met een gewicht en een waarde, in een rugzak met beperkte capaciteit moet worden gepakt. Het doel is om de totale waarde van de voorwerpen in de rugzak te maximaliseren zonder de capaciteit te overschrijden.

    - Representatie: Elk individu in de populatie vertegenwoordigt een mogelijke selectie van voorwerpen, die kan worden gecodeerd als een binaire string waar elke bit aangeeft of een voorwerp is opgenomen (1) of niet (0).
    - Fitness Functie: De fitness van een selectie kan worden berekend als de totale waarde van de opgenomen voorwerpen, met een straf voor het overschrijden van de capaciteit.
    - Kruising: Eenpunts- of meervoudige kruising kan worden gebruikt om delen van twee ouderoplossingen te combineren.
    - Mutatie: Bit-flip mutatie, waarbij een bit willekeurig wordt omgekeerd, kan worden gebruikt om variabiliteit in te voeren.