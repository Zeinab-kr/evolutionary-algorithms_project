import random

from individual import Individual


def select_two_individual_for_crossover(
    individual_list: list[Individual]
) -> tuple[Individual, Individual]:

    # TODO: this method selects two individuals for the crossover algorithm
    generation_size = len(individual_list)
    max_fitness = 0.0
    # total_fitness = 0.0
    for individual in individual_list:
        # total_fitness += individual.fitness
        if individual.fitness > max_fitness:
            max_fitness = individual.fitness

    ranked_individuals = sorted(individual_list, key=lambda ind: ind.fitness)

    # total_ranks = sum(i for i in range(len(individual_list)))

    total_score = sum((generation_size - i) * (max_fitness - ranked_individuals[i].fitness)
                      for i in range(generation_size))

    probabilities = [(generation_size - i) * (max_fitness - ranked_individuals[i].fitness) / total_score
                     for i in range(generation_size)]
    print(probabilities)

    # parent1 = ranked_individuals[probabilities.index(max(probabilities))]
    # parent2 = random.choices(ranked_individuals, weights=probabilities, k=1)[0]

    parent1 = random.choices(ranked_individuals, weights=probabilities)[0]
    parent2 = random.choices(ranked_individuals, weights=probabilities)[0]

    return parent1, parent2
