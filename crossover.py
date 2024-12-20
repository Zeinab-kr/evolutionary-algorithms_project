import random

from individual import Individual


def cross_over(parent1: Individual, parent2: Individual) -> tuple[Individual, Individual]:
    crossover_point = random.randint(1, len(parent1.genome) - 1)
    child1_genome = parent1.genome[:crossover_point] + parent2.genome[crossover_point:]
    child2_genome = parent2.genome[:crossover_point] + parent1.genome[crossover_point:]

    child1 = Individual(generate_random_genome=False)
    child2 = Individual(generate_random_genome=False)

    child1.genome = child1_genome
    child2.genome = child2_genome

    return child1, child2
