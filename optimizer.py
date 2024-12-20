import random

import crossover
from individual import Individual
from evaluation import evaluate, evaluate_all
from selection import select_two_individual_for_crossover


def run_algorithm(
    distance_matrix,
    population_size=20,
    generation_size=30,
):
    MUTATION_RATE = 0.3
    best_fitness_list = []
    avg_fitness_list = []
    best_individual = None
    genome_size = len(distance_matrix)

    # create primary population
    population = primary_population_creator(population_size, genome_size)

    while True:
        # cross over
        generated_individuals = []
        for _ in range(int(generation_size / 2)):
            parent1, parent2 = select_two_individual_for_crossover(population)
            child1, child2 = crossover.cross_over(parent1=parent1, parent2=parent2)
            generated_individuals.append(child1)
            generated_individuals.append(child2)

        # mutation
        for individual in generated_individuals:
            # TODO: by using a random number and 'MUTATION_RATE', decide whether to mutate the individual or not    
            pass

        # TODO: evaluate generated_individuals

        # TODO: select next generation by use of 'next_generation_selection' method

        # TODO: check termination condition on generated individuals

        # TODO: redefine 'population' for the next iteration

        # don't change following codes
        best_fitness_list.append(best_fitness(population))
        avg_fitness_list.append(avg_fitness(population))
        random.shuffle(population)

    return best_individual, best_fitness_list, avg_fitness_list


def primary_population_creator(
    population_size: int, genome_size: int
) -> list[Individual]:
    # TODO: this method create primary individual based on input population size and return them as list of individuals
    return [Individual(genome_length=genome_size, generate_random_genome=True) for _ in range(population_size)]


def avg_fitness(
        population:list[Individual]
) -> float:
    # TODO: this method calculates average of individuals fitness
    pass


def best_fitness(
        population:list[Individual]
) -> float:
    # TODO: this method finds best fitness in the population
    pass