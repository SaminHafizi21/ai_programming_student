class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        pass

    def display(self):
        print("Gesorteerde Array:")
        for element in self.array:
            print(element, " ")
        print()


if __name__ == "__main__":
    input_array = [12, 11, 13, 5, 6]
    sorter = InsertionSort(input_array)
    print("Originele Array:")
    for element in input_array:
        print(element," ")
    print("\n")
    sorter.sort()
    sorter.display()