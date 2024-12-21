import random

from individual import Individual


def select_two_individual_for_crossover(
    individual_list: list[Individual]
) -> tuple[Individual, Individual]:

    # TODO: this method selects two individuals for the crossover algorithm
    ranked_individuals = sorted(individual_list, key=lambda ind: ind.fitness)

    total_ranks = sum(i for i in range(len(individual_list)))
    probabilities = [(len(individual_list) - i) / total_ranks for i in range(len(individual_list))]

    # parent1 = ranked_individuals[probabilities.index(max(probabilities))]
    # parent2 = random.choices(ranked_individuals, weights=probabilities, k=1)[0]

    parent1 = random.choices(ranked_individuals, weights=probabilities)[0]
    parent2 = random.choices(ranked_individuals, weights=probabilities)[0]

    return parent1, parent2
