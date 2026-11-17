"""
Oefening 1: Insertion Sort
===========================
Implementeer insertion sort volgens het stappenplan in opgave_week1.md.
"""


def insertion_sort(sequence):

    for i in range(1, len(sequence)):
        key = sequence[i]
        print(f"--- nieuwe ronde: key = {key}, i = {i}, lijst = {sequence}")
        while i > 0 and sequence[i - 1] > sequence[i]:
            temp = sequence[i - 1]
            sequence[i - 1] = sequence[i]
            sequence[i] = temp
            i -= 1
            print(f"    na wissel:   key = {key}, i = {i}, lijst = {sequence}")

    return sequence


if __name__ == "__main__":
    # Test je implementatie met deze voorbeelden
    test_lijsten = [
        [5, 2, 3, 1, 4],
        [3, 1, 2, 1, 3],
        [5, 2, 4, 6, 1, 3],
    ]

    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd = insertion_sort(lijst)
        print(f"Origineel: {origineel} -> Gesorteerd: {gesorteerd}")

    # Stap 5 (uitbreiding): vergelijk met bubble sort en merge sort
    # Kopieer bubble_sort en merge_sort uit de cursus en test hier:
    # import random
    # import time
    # ...
