"""
Oefening: Bubble Sort
=====================
Implementeer bubble sort volgens het stappenplan hieronder.

Stap 1: Begrijp het algoritme
    Bubble sort vergelijkt telkens 2 buren.
    Is het linkse getal groter dan het rechtse? Dan wissel je ze.
    Na elke ronde staat het grootste getal achteraan.
"""


def bubble_sort(sequence):
    """
    Sorteer een lijst van klein naar groot met behulp van bubble sort.
    """
    n = len(sequence)
    temp = 0
    counter = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if sequence[j] > sequence[j + 1]:
                temp = sequence[j]
                sequence[j] = sequence[j + 1]
                sequence[j + 1] = temp
                counter += 1
    return sequence, counter


if __name__ == "__main__":
    # Test je implementatie met deze voorbeelden
    test_lijsten = [
        [],
        [42],
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 1, 3],
        [5, 2, 8, 1, 4],
    ]

    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd, counter = bubble_sort(lijst)
        print(
            f"Origineel: {origineel} -> Gesorteerd: {gesorteerd} => aantal swaps {counter}"
        )

    # Stap 4: tel de wissels
    # for lijst in test_lijsten:
    #     gesorteerd, wissels = bubble_sort_met_teller(lijst.copy())
    #     print(f"{lijst} -> {wissels} wissels")

    # Stap 5 (uitbreiding): meet de tijd
    # import time
    # ...


"""


Stap 4: Tel de wissels
    Pas bubble_sort_met_teller aan.
    Ze geeft 2 dingen terug: de gesorteerde lijst en het aantal wissels.
    Hoeveel wissels heeft [5, 4, 3, 2, 1] nodig? En [1, 2, 3, 4]?

Stap 5 (Uitbreiding): Stop vroeger
    Als er in een ronde GEEN wissel gebeurt, is de lijst al gesorteerd.
    Pas bubble_sort_vroeg_stoppen aan zodat de functie dan stopt.
    Vergelijk met de tijd van bubble_sort voor een lijst die al
    gesorteerd is (10, 100, 1000 items). Gebruik de time-module.


"""


def bubble_sort_met_teller(sequence):
    """
    Zoals bubble_sort, maar tel ook hoeveel keer je wisselt.

    Returns:
        tuple: (gesorteerde lijst, aantal wissels)
    """
    # TODO: kopieer je bubble_sort en voeg een teller toe
    pass


def bubble_sort_vroeg_stoppen(sequence):
    """
    Zoals bubble_sort, maar stop zodra een ronde geen wissel had.

    Returns:
        list: De gesorteerde lijst.
    """
    # TODO: Stap 5 (uitbreiding)
    pass
