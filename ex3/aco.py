
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
    def __init__(self,taskinitializer,initializer,solutiongenerator,evaporator,intensificator):

        self.taskinitializer=taskinitializer
        self.initializer=initializer
        self.solutiongenerator=solutiongenerator
        self.evaporator=evaporator
        self.intensificator=intensificator

        self.initializer.initialize(self.taskinitializer)

    def do(self):
        global Max_Iterations

        #pheromone matrix
        #pmatrix = self.initializer.do() #maybe different return variable

        iteration_best = list()
        #iteration_best.append()

        for iteration in range(Max_Iterations):
            pass
            #iteration_best.append()

        plt.plot(iteration_best)
        plt.ylabel('')
        plt.xlabel('Iteration')
        plt.show()


Max_Iterations = 100

g=ACO(Taskinitializer(1),Initializer(),SolutionGenerator(),Evaporator(),Intensificator())
g.do()

