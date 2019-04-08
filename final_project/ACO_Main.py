
# coding: utf-8

# Ant Coloncy Optimization for Nature-Inspired Algorithms for solving Traveling Salesman Problem
#
# Create an Object of ACO and name one module for each required component in constructor
#  (Taskinitializer, Initializer, Solutiongenerator, Evaporator, Intensificator)
# once initialized, run run() for ACO Object


import random
import numpy as np
import matplotlib.pyplot as plt

from ACO_Initializer import Initializer
from ACO_SolutionGenerator import SolutionGenerator
from ACO_Evaporator import Evaporator
from ACO_Intensificator import Intensificator


class ACO:
    def __init__(self, distance_matrix, customers_to_visit, initializer, solutiongenerator, evaporator, intensificator, iterations, printing=True):

        self.initializer = initializer
        self.solutiongenerator = solutiongenerator
        self.evaporator = evaporator
        self.intensificator = intensificator
        self.printing = printing
        self.iterations = iterations


        self.solutions_generations = list()
        self.evaluations_generations = list()
        self.best_solutions_scores = list()

        #todo: consitently same name
        self.solutiongenerator.set_distance_matrix(self.task_matrix)

    #cuts the rows and columns from the distance matrix that belong to customers which numbers aren't in customers_to_visit
    #do customers start with 0 or 1 ??
    def _cut_matrix(self, customers_to_visit):
        for customer in range(len(distance_matrix)):
            if not customer in customers_to_visit:
                distance_matrix = numpy.delete(self.distance_matrix, (customer), axis=0)
                distance_matrix = numpy.delete(self.distance_matrix, (customer), axis=1)
        return distance_matrix

    def run(self,customers_to_visit):
        self.pheromone_matrix = self.initializer.initialize(customers_to_visit)
        self.task_matrix = self._cut_matrix(customers_to_visit)

        iteration_best = list()

        for iteration in range(self.iterations):
            solutions, evaluations = self.solutiongenerator.collecting_solutions(self.pheromone_matrix)

            self.solutions_generations.append(solutions[0])
            self.evaluations_generations.append(evaluations)

            #value of best solution
            self.best_solutions_scores.append(evaluations[0])

            iteration_best.append(min(evaluations))

            #updating pheromone matrix
            self.pheromone_matrix = self.evaporator.evaporate(self.pheromone_matrix)
            self.pheromone_matrix = self.intensificator.intensify(self.pheromone_matrix,solutions)

        return np.array(self.best_solutions_scores), np.array(self.solutions_generations), \
               np.array(self.evaluations_generations)

#Instanciates ACO object and runs it with default parameters
def run_default(distance_matrix, customers_to_visit):
    initializer = Initializer()
    solutiongenerator = SolutionGenerator(alpha=1, beta=1, num_of_ants=20)
    evaporator = Evaporator(rho=0.1)
    intensificator = Intensificator(delta=0.5)

    antco = ACO(distance_matrix, customers_to_visit, initializer, solutiongenerator, evaporator, intensificator, 30, printing=False)

    best_solutions_scores, best_solutions, all_scores = antco.run()
    """
    plt.plot(best_solutions)
    plt.ylabel('')
    plt.xlabel('Iteration')
    plt.show()
    """

    best_score = max(best_solutions_scores)
    best_solutions_scores = list(best_solutions_scores)

    best_solution = best_solutions[best_solutions_scores.index(best_score)]
    return best_score, best_solution

