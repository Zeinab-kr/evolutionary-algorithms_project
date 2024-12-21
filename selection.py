import random

from individual import Individual


def select_two_individual_for_crossover(
    individual_list: list[Individual]
) -> tuple[Individual, Individual]:

    # TODO: this method selects two individuals for the crossover algorithm
    generation_size = len(individual_list)
    # max_fitness = 0.0
    # for individual in individual_list:
    #     if -individual.fitness > max_fitness:
    #         max_fitness = -individual.fitness

    ranked_individuals = sorted(individual_list, key=lambda ind: ind.fitness)

    total_ranks = sum(i for i in range(len(individual_list)))
    total_fitness = sum(-ind.fitness for ind in ranked_individuals)

    fitness_probabilities = [(total_fitness + ind.fitness) / total_fitness for ind in ranked_individuals]
    rank_probabilities = [(generation_size - i) / total_ranks for i in range(generation_size)]
    weights = [fitness_probabilities[i] * rank_probabilities[i] for i in range(generation_size)]

    parent1 = random.choices(ranked_individuals, weights=fitness_probabilities)[0]
    parent2 = random.choices(ranked_individuals, weights=fitness_probabilities)[0]

    return parent1, parent2
