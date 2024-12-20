import random

from individual import Individual


def select_two_individual_for_crossover(
    individual_list: list[Individual]
) -> tuple[Individual, Individual]:

    # TODO: this method selects two individuals for the crossover algorithm

    total_fitness = sum(individual.fitness for individual in individual_list)
    print(total_fitness)
    probabilities = [((total_fitness - individual.fitness) / total_fitness) for individual in individual_list]
    print(probabilities)
    sorted_indices = sorted(range(len(probabilities)), key=lambda i: probabilities[i], reverse=True)
    parent1_index = sorted_indices[0]
    parent2_index = sorted_indices[1]
    parent1 = individual_list[parent1_index]
    parent2 = individual_list[parent2_index]
    return parent1, parent2
