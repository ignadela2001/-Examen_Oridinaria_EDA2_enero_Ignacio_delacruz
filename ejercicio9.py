import itertools

class Planeta:
    def __init__(self, name):
        self.name = name
names = ["Alderaan", "Endor", "Dagobah", "Hoth", "Tatooine", "Kamino", "Naboo", "Mustafar", "Scarif", "Bespin", "Eadu", "Exegol", "Felucia", "Christopsis", "Concord down", "Corellia", "Coruscant"]

n = len(names)
distances = [[0 for _ in range(n)] for _ in range(n)]

distances[0][1] = distances[1][0] = 1234
distances[0][2] = distances[2][0] = 2345
distances[0][3] = distances[3][0] = 3456
distances[0][4] = distances[4][0] = 4567
distances[0][5] = distances[5][0] = 5678
distances[0][6] = distances[6][0] = 6789
distances[0][7] = distances[7][0] = 7890
distances[0][8] = distances[8][0] = 8901
distances[0][9] = distances[9][0] = 9012
distances[0][10] = distances[10][0] = 123
distances[0][11] = distances[11][0] = 234
distances[0][12] = distances[12][0] = 345
distances[0][13] = distances[13][0] = 456
distances[0][14] = distances[14][0] = 567
distances[0][15] = distances[15][0] = 678
distances[0][16] = distances[16][0] = 789

for i in range(1, n):
    for j in range(i + 1, n):
        distances[i][j] = distances[j][i] = i + j

def crear_planetas(names, distances):
    planetas = []
    for i in range(len(names)):
        planeta= Planeta(names[i], distances[i])
        planetas.append(planeta)
    return planetas

class TouristSolver:
    def __init__(self, planetas, distances):
        self.planetas = planetas
        self.distances = distances
    
    
    def solve(self):
        best_distance = float('inf')
        best_permutation = None
        
        for permutation in itertools.permutations(self.planetas[1:]):
            permutation = [self.planetas[0]] + list(permutation) + [self.planetas[0]]
            distance = 0
            for i in range(len(permutation) - 1):
                planeta1 = permutation[i]
                planeta2 = permutation[i + 1]
                planeta1_index = self.planetas.index(planeta1)
                planeta2_index = self.planetas.index(planeta2)
                distance += self.distances[planeta1_index][planeta2_index]
            if distance < best_distance or (distance == best_distance):
                best_distance = distance
                best_permutation = permutation

                print('Mejor permutación:', [Planeta.name for Planeta in best_permutation])
                print('Distancia total:', best_distance)
              

def create_cities(names, distances, costs):
    planetas = []
    for i in range(len(names)):
        planeta = Planeta(names[i], distances[i], costs[i])
        planetas.append(planeta)
    return planetas