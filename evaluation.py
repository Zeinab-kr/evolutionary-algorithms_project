from individual import Individual


def evaluate_all(individual_list: list[Individual], distance_matrix: list[list[float]]):
    for individual in individual_list:
        evaluate(individual, distance_matrix)


def evaluate(individual: Individual, distance_matrix: list[list[float]]):
    # TODO: this method computes fitness (based on the TSP problem) and updates the fitness attribute of the
    #  individual parameter (individual.fitness=new_fitness) hint: as taught by Dr. Ebadzadeh in the class,
    #  you may use -c to reverse the fitness value c
    total_distance = 0.0
    for i in range(len(individual.genome) - 1):
        total_distance += distance_matrix[individual.genome[i]][individual.genome[i+1]]

    individual.fitness = 1 / total_distance
