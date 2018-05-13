
# coding: utf-8

# Ant Coloncy Optimization for Nature-Inspired Algorithms for solving Traveling Salesman Problem
#
# Create an Object of ACO and name one module for each required component in constructor
#  (Taskinitializer, Initializer, Solutiongenerator, Evaporator, Intensificator)
# once initialized, run do() for ACO Object


import random
import numpy as np
import matplotlib.pyplot as plt

import Taskinitializer,Initializer,SolutionGenerator,Evaporator,Intensificator

class ACO:
    def __init__(self,taskinitializer,initializer,solutiongenerator,evaporator,intensificator):

        self.taskinitializer=taskinitializer
        self.initializer=initializer
        self.solutiongenerator=solutiongenerator
        self.evaporator=evaporator
        self.intensificator=intensificator

        self.pmatrix = self.initializer.initialize(self.taskinitializer)
        self.solutiongenerator.set_task(self.taskinitializer)


    def do(self):
        global Max_Iterations

        iteration_best = list()
        #iteration_best.append()

        for iteration in range(Max_Iterations):
            solutions, evaluations = self.solutiongenerator.collecting_solutions(self.pmatrix)
            self.pmatrix = self.evaporator.evaporate(self.pmatrix)

            #Save value of best solution for the diagram
            iteration_best.append(max(evaluations))

            self.pmatrix = self.intensificator.intensify(self.pmatrix,solutions)

        plt.plot(iteration_best)
        plt.ylabel('')
        plt.xlabel('Iteration')
        plt.show()


Max_Iterations = 100

g=ACO(Taskinitializer.Taskinitializer(1),Initializer.Initializer(),SolutionGenerator.SolutionGenerator(1, 1, 10),Evaporator.Evaporator(0.05),Intensificator.Intensificator(0.2))
g.do()

