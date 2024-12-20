import random

from individual import Individual


def cross_over(parent1: Individual, parent2: Individual) -> tuple[Individual, Individual]:
    crossover_point = int(len(parent1.genome) / 2) - 1
    child1_genome = parent1.genome[:crossover_point] + parent2.genome[crossover_point:]
    child2_genome = parent2.genome[:crossover_point] + parent1.genome[crossover_point:]

    child1 = Individual(generate_random_genome=False)
    child2 = Individual(generate_random_genome=False)

    child1.genome = fix_genome(child1_genome)
    child2.genome = fix_genome(child2_genome)

    return child1, child2


def fix_genome(genome: list) -> list:
    checker = list(range(len(genome)))

    # check for duplicates
    for i in range(len(genome)):
        for j in range(i + 1, len(genome)):
            if genome[j] == genome[i] and genome[j] != -1:
                genome[j] = -1

        if genome[i] in checker:
            checker.remove(genome[i])

    # replace duplicates with valid genes
    for i in range(len(genome)):
        if genome[i] == -1:
            genome[i] = checker[0]
            checker.pop(0)

    return genome
