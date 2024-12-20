import random

from individual import Individual


def mutation1(individual: Individual):
    # TODO: this method applies mutation on an individual
    checker = list(range(30))

    # check for duplicates
    for i in range(len(individual.genome)):
        for j in range(i + 1, len(individual.genome)):
            if individual.genome[j] == individual.genome[i]:
                individual.genome[j] = -1

        if individual.genome[i] in checker:
            checker.remove(individual.genome[i])

    # replace duplicates with valid genes
    for i in range(len(individual.genome)):
        if individual.genome[i] == -1:
            individual.genome[i] = checker[0]
            checker.pop(0)

    num1, num2 = sorted(random.sample(range(len(individual.genome)), 2))
    individual.genome[num1], individual.genome[num2] = individual.genome[num2], individual.genome[num1]
