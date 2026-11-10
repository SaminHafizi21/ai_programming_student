import numpy as np
import random
import math

class TSPSolver:
    def __init__(self, distance_matrix, initial_temperature=1000, cooling_rate=0.995, num_iterations=10000):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.num_iterations = num_iterations

    def total_distance(self, tour):
        distance = 0
        for i in range(len(tour) - 1):
            distance += self.distance_matrix[tour[i]][tour[i + 1]]
        distance += self.distance_matrix[tour[-1]][tour[0]]  # Terug naar start
        return distance

    def simulated_annealing(self):
        current_tour = list(range(self.num_cities))
        current_distance = self.total_distance(current_tour)

        best_tour = current_tour.copy()
        best_distance = current_distance

        temperature = self.initial_temperature

        for _ in range(self.num_iterations):
            i, j = random.sample(range(self.num_cities), 2) # twee steden kiezen om te verwisselen
            
            new_tour = current_tour.copy()
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i] # twee steden effectief verwisselen
            
            new_distance = self.total_distance(new_tour)
            delta = new_distance - current_distance

            if delta < 0 or random.random() < math.exp(-delta / temperature):
                current_tour = new_tour
                current_distance = new_distance

                if current_distance < best_distance:
                    best_tour = current_tour
                    best_distance = current_distance

            temperature *= self.cooling_rate

        return best_tour, best_distance
    
def realistic_example():
    european_cities = ['Paris', 'Madrid', 'Barcelona', 'Berlin', 'Rome', 'Athens', 'Lisbon',
       'Vienna', 'Brussels', 'Warsaw', 'Budapest', 'Stockholm', 'Prague',
       'Helsinki', 'Zürich', 'Copenhagen', 'Dublin', 'Amsterdam', 'Oslo',
       'Ljubljana']

    distance_array = [[   0., 1054.,  832.,  877., 1106., 2098., 1453., 1034.,  261.,
                        1366., 1248., 1546.,  885., 1908.,  489., 1026.,  777.,  428.,
                        1341.,  966.],
                    [1054.,    0.,  505., 1869., 1361., 2368.,  503., 1808., 1315.,
                        2290., 1976., 2596., 1774., 2949., 1247., 2073., 1451., 1481.,
                        2389., 1598.],
                    [ 832.,  505.,    0., 1499.,  857., 1877., 1007., 1348., 1063.,
                        1863., 1499., 2281., 1354., 2603.,  836., 1759., 1470., 1236.,
                        2143., 1117.],
                    [ 877., 1869., 1499.,    0., 1183., 1803., 2312.,  524.,  652.,
                        516.,  689.,  813.,  281., 1105.,  668.,  355., 1316.,  575.,
                        838.,  723.],
                    [1106., 1361.,  857., 1183.,    0., 1052., 1862.,  764., 1172.,
                        1317.,  812., 1979.,  923., 2202.,  684., 1532., 1883., 1294.,
                        2007.,  490.],
                    [2098., 2368., 1877., 1803., 1052.,    0., 2852., 1282., 2089.,
                        1600., 1123., 2409., 1533., 2469., 1617., 2137., 2853., 2161.,
                        2605., 1175.],
                    [1453.,  503., 1007., 2312., 1862., 2852.,    0., 2298., 1710.,
                        2759., 2473., 2991., 2246., 3360., 1723., 2477., 1639., 1862.,
                        2738., 2097.],
                    [1034., 1808., 1348.,  524.,  764., 1282., 2298.,    0.,  915.,
                        557.,  217., 1245.,  250., 1440.,  590.,  871., 1681.,  933.,
                        1352.,  276.],
                    [ 261., 1315., 1063.,  652., 1172., 2089., 1710.,  915.,    0.,
                        1160., 1132., 1285.,  721., 1649.,  491.,  767.,  773.,  173.,
                        1087.,  918.],
                    [1366., 2290., 1863.,  516., 1317., 1600., 2759.,  557., 1160.,
                        0.,  545.,  809.,  515.,  913., 1042.,  670., 1825., 1091.,
                        1061.,  834.],
                    [1248., 1976., 1499.,  689.,  812., 1123., 2473.,  217., 1132.,
                        545.,    0., 1319.,  443., 1459.,  791., 1013., 1896., 1145.,
                        1482.,  383.],
                    [1546., 2596., 2281.,  813., 1979., 2409., 2991., 1245., 1285.,
                        809., 1319.,    0., 1056.,  393., 1470.,  524., 1630., 1128.,
                        417., 1497.],
                    [ 885., 1774., 1354.,  281.,  923., 1533., 2246.,  250.,  721.,
                        515.,  443., 1056.,    0., 1301.,  527.,  635., 1466.,  710.,
                        1118.,  447.],
                    [1908., 2949., 2603., 1105., 2202., 2469., 3360., 1440., 1649.,
                        913., 1459.,  393., 1301.,    0., 1773.,  883., 2023., 1502.,
                        786., 1712.],
                    [ 489., 1247.,  836.,  668.,  684., 1617., 1723.,  590.,  491.,
                        1042.,  791., 1470.,  527., 1773.,    0.,  963., 1237.,  610.,
                        1401.,  477.],
                    [1026., 2073., 1759.,  355., 1532., 2137., 2477.,  871.,  767.,
                        670., 1013.,  524.,  635.,  883.,  963.,    0., 1238.,  621.,
                        483., 1078.],
                    [ 777., 1451., 1470., 1316., 1883., 2853., 1639., 1681.,  773.,
                        1825., 1896., 1630., 1466., 2023., 1237., 1238.,    0.,  757.,
                        1265., 1689.],
                    [ 428., 1481., 1236.,  575., 1294., 2161., 1862.,  933.,  173.,
                        1091., 1145., 1128.,  710., 1502.,  610.,  621.,  757.,    0.,
                        914.,  986.],
                    [1341., 2389., 2143.,  838., 2007., 2605., 2738., 1352., 1087.,
                        1061., 1482.,  417., 1118.,  786., 1401.,  483., 1265.,  914.,
                        0., 1561.],
                    [ 966., 1598., 1117.,  723.,  490., 1175., 2097.,  276.,  918.,
                        834.,  383., 1497.,  447., 1712.,  477., 1078., 1689.,  986.,
                        1561.,    0.]]

    distance_matrix = np.array(distance_array)

    # check op symmetrie van de matric
    transpose = distance_matrix.transpose()
    if distance_matrix.shape == transpose.shape:
        # comparing the arrays using == and all() method
        if (distance_matrix == transpose).all():
            print("The distance matrix is Symmetric")
        else:
            print("The distance matrix is not Symmetricc")
    else:
        print("The distance matrix is not Symmetric")

    print("Cities:", european_cities)

    tsp_solver = TSPSolver(distance_matrix)
    best_tour, best_distance = tsp_solver.simulated_annealing()

    print(distance_matrix.shape)
    print((european_cities), (best_tour))
    print("Best Tour:", [european_cities[index] for index in best_tour])
    print("Best Distance:", best_distance)

if __name__ == "__main__":
    # Define the distance matrix (distances between cities)
    # Replace this with your own distance matrix.
    distance_matrix = np.array([
        [0, 29, 20, 21],
        [29, 0, 15, 18],
        [20, 15, 0, 25],
        [21, 18, 25, 0]
    ])

    tsp_solver = TSPSolver(distance_matrix)
    best_tour, best_distance = tsp_solver.simulated_annealing()

    print("Best Tour:", best_tour)
    print("Best Distance:", best_distance)

    realistic_example()
