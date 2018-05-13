
# coding: utf-8

# Ant Coloncy Optimization for Nature-Inspired Algorithms for solving Traveling Salesman Problem
#
# Create an Object of ACO and name one module for each required component in constructor
#  (Taskinitializer, Initializer, Solutiongenerator,Evaporator,Intensificator)
# once initialized, run do() for ACO Object
# Taskinitializer initializes one of the 3 given tasks

import random
import numpy as np
import matplotlib.pyplot as plt

import Initializer,Taskinitializer,SolutionGenerator,Evaporator,Intensificator

class ACO:
    def __init__(self, taskinitializer, initializer, solutiongenerator, evaporator, intensificator, iterations, printing=True):

        self.taskinitializer = taskinitializer
        self.initializer = initializer
        self.solutiongenerator = solutiongenerator
        self.evaporator = evaporator
        self.intensificator = intensificator
        self.printing = printing
        self.iterations = iterations

        self.pheromone_matrix = self.initializer.initialize(self.taskinitializer)
        self.solutions_generations = list()
        self.evaluations_generations = list()
        self.best_solutions_scores = list()


    def run(self):
        #global Max_Iterations

        for iteration in range(self.iterations):

            generation = self.solutiongenerator.collecting_solutions(self.pheromone_matrix)
            self.solutions_generations.append(generation[0])
            self.evaluations_generations.append(generation[1])
            self.best_solutions_scores.append(generation[1][0])
            if self.printing:
                print('Interation: ', iteration, ' best solution: ', generation[1][0])

            #updating pheromone matrix
            self.pheromone_matrix = self.evaporator.evaporate(self.pheromone_matrix)
            self.pheromone_matrix = self.intensificator.intensify(self.pheromone_matrix,generation[0])

        return np.array(self.best_solutions_scores), np.array(self.solutions_generations), \
               np.array(self.evaluations_generations)



        #plt.plot(iteration_best)
        #plt.ylabel('')
        #plt.xlabel('Iteration')
        #plt.show()


#Max_Iterations = 100
"""
from Initializer import Initializer
from Taskinitializer import Taskinitializer
from SolutionGenerator import SolutionGenerator
from Evaporator import Evaporator
from Intensificator import Intensificator
from aco import ACO
import numpy as np
#import matplotlib as mpl

taskinitializer = Taskinitializer(1)
initializer = Initializer()
solutiongenerator = SolutionGenerator(alpha=1,beta=1,num_of_ants=20,task = taskinitializer)
evaporator = Evaporator(rho=0.5)
intensificator = Intensificator(delta=1)

antco = ACO(taskinitializer, initializer, solutiongenerator, evaporator, intensificator, 50, printing=True)
solutions, scores, best_solutions = antco.do()"""