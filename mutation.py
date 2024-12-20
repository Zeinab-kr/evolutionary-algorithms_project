import random

from individual import Individual


def mutation1(individual: Individual, mutation_rate: float):
    # TODO: this method applies mutation on an individual

    for _ in range(int(mutation_rate * len(individual.genome) / 2)):
        num1, num2 = sorted(random.sample(range(len(individual.genome)), 2))
        temp = individual.genome[num1]
        individual.genome[num1] = individual.genome[num2]
        individual.genome[num2] = temp
