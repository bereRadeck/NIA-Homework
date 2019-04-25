
# coding: utf-8

# Ant Coloncy Optimization for Nature-Inspired Algorithms for solving Traveling Salesman Problem
#
# Create an Object of ACO and name one module for each required component in constructor
#  (Taskinitializer, Initializer, Solutiongenerator, Evaporator, Intensificator)
# once initialized, run run() for ACO Object


import random
import numpy as np
import matplotlib.pyplot as plt

from ACO_Initializer import ACO_Initializer
from ACO_SolutionGenerator import SolutionGenerator
from ACO_Evaporator import Evaporator
from ACO_Intensificator import Intensificator


class ACO:
    def __init__(self, distance_matrix, initializer, solutiongenerator, evaporator, intensificator, iterations, printing=True):

        self.initializer = initializer
        self.solutiongenerator = solutiongenerator
        self.evaporator = evaporator
        self.intensificator = intensificator
        self.printing = printing
        self.iterations = iterations
        self.distance_matrix = distance_matrix

        self.solutions_generations = list()
        self.evaluations_generations = list()
        self.best_solutions_scores = list()

    #cuts the rows and columns from the distance matrix that belong to customers which numbers aren't in customers_to_visit
    #do customers start with 0 or 1 ??
    def _cut_matrix(self, customers_to_visit):

        task_matrix = self.distance_matrix
        customers = np.arange(task_matrix.shape[0])
        customers_not_needed = [c for c in customers if c not in customers_to_visit]
        #for customer in range(len(task_matrix)):
            #if not customer in customers_to_visit:
        task_matrix = np.delete(task_matrix, customers_not_needed, axis=0)
        task_matrix = np.delete(task_matrix, customers_not_needed, axis=1)
        return task_matrix

    def run(self,customers_to_visit,detailed_return = False):

        self.pheromone_matrix = self.initializer.initialize(customers_to_visit)
        self.task_matrix = self._cut_matrix(customers_to_visit)
        #todo: consitently same name
        self.solutiongenerator.set_task_matrix(self.task_matrix)

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

        if (detailed_return):
            return np.array(self.best_solutions_scores), np.array(self.solutions_generations), np.array(self.evaluations_generations)
        else:
            return self.best_solutions_scores[-1]

