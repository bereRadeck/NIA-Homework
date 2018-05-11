
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

class ACO:
    def __init__(self,taskinitializer,initializer,solutiongenerator,evaporator,intensificator):

        self.taskinitializer=taskinitializer
        self.initializer=initializer
        self.solutiongenerator=solutiongenerator
        self.evaporator=evaporator
        self.intensificator=intensificator

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


#Superclass for the three different tasks (variance of jobtimes and machine amount)
class Taskinitializer:
    pass

class Task1(Taskinitializer):
    pass
    
class Task2(Taskinitializer):
    pass

class Task3(Taskinitializer):
    pass


class Initializer:
    pass

class Initializer1(Initializer):
    pass


class Solutiongenerator:
    pass

class Solutiongenerator1(Solutiongenerator):
    pass


class Evaporator:
    pass


class Intensificator:
    pass


Max_Iterations = 100

g=ACO(Task1(),Initializer1(),Solutiongenerator1(),Evaporator(),Intensificator())
g.do()

