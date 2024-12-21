import random

import crossover
import mutation
import termination_condition
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
    # print("start")
    # for individual in population:
    #     print(individual.genome)
    #     print(individual.fitness)
    evaluate_all(population, distance_matrix=distance_matrix)

    i = 0
    while True:
        i += 1
        # cross over
        generated_individuals = []
        for _ in range(int(generation_size / 2)):
            parent1, parent2 = select_two_individual_for_crossover(population)
            if i % 1000 == 1:
                print(f"parent1: {parent1.genome}:{parent1.fitness}, parent2: {parent2.genome}:{parent2.fitness}")

            child1, child2 = crossover.cross_over(parent1=parent1, parent2=parent2)
            generated_individuals.append(child1)
            generated_individuals.append(child2)

        # mutation
        for individual in generated_individuals:
            mutation.mutation1(individual, MUTATION_RATE)

        # TODO: evaluate generated_individuals
        evaluate_all(generated_individuals, distance_matrix=distance_matrix)

        # TODO: select next generation by use of 'next_generation_selection' method
        next_generation = next_generation_selection(population, generated_individuals)

        # TODO: check termination condition on generated individuals
        if termination_condition.terminate1(next_generation):
            break

        # TODO: redefine 'population' for the next iteration
        population = next_generation

        # don't change following codes
        best_individual = best_fitness(population)
        best_fitness_list.append(best_individual)
        avg_fitness_list.append(avg_fitness(population))
        random.shuffle(population)
        # print("end")
        # for individual in population:
        #     print(individual.genome)
        #     print(individual.fitness)

    return best_individual, best_fitness_list, avg_fitness_list


def primary_population_creator(
        population_size: int, genome_size: int
) -> list[Individual]:
    # TODO: this method create primary individual based on input population size and return them as list of individuals
    return [Individual(genome_length=genome_size, generate_random_genome=True) for _ in range(population_size)]


def next_generation_selection(population: list[Individual], generated_individuals: list[Individual])\
        -> list[Individual]:
    combined_population = population + generated_individuals

    combined_population.sort(key=lambda ind: ind.fitness, reverse=True)

    next_generation_size = len(population)
    next_generation = combined_population[:next_generation_size]

    return next_generation


def avg_fitness(
        population: list[Individual]
) -> float:
    # TODO: this method calculates average of individuals fitness
    total_fitness = sum(individual.fitness for individual in population)
    return total_fitness / len(population) if population else 0


def best_fitness(
        population: list[Individual]
) -> float:
    # TODO: this method finds best fitness in the population
    return max(individual.fitness for individual in population) if population else float('-inf')
