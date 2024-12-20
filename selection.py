import random

from individual import Individual


def select_two_individual_for_crossover(
    individual_list: list[Individual], population_size: int
) -> tuple[Individual, Individual]: # you can change return type based on your implementation

    # TODO: this method selects two individuals for the crossover algorithm

    total_fitness = sum(individual.fitness for individual in individual_list)
    probabilities = [individual.fitness / total_fitness for individual in individual_list]
    parent1 = random.choices(individual_list, weights=probabilities)[0]
    parent2 = random.choices(individual_list, weights=probabilities)[0]
    return parent1, parent2
