import math


def create_distance_matrix(input_path: str):
    with open(input_path, 'r') as file:
        cities = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]

    num_cities = len(cities)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    return distance_matrix
