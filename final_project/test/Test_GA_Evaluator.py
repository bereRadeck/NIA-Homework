from final_project.GA_Evaluator import *
from final_project.GA_Initializer import *

from ACO_Initializer import ACO_Initializer
from ACO_SolutionGenerator import SolutionGenerator
from ACO_Evaporator import Evaporator
from ACO_Intensificator import Intensificator
from ACO_Main import ACO

import numpy as np


popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
initializer = PartiallyRandomInitializer(popsize,demands,capacities)
pop = initializer.initialize()
dist_matrix = np.ones((8,8))
trans_cost = [2,3,4,5]


aco_initializer = ACO_Initializer()
solutiongenerator = SolutionGenerator()
evaporator = Evaporator()
intensificator = Intensificator()



popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
dist_matrix = np.ones((8,8))
trans_cost = [2,3,4,5]
aco_iterations = 5
mutate_probability = 0.1

aco = ACO(dist_matrix,aco_initializer,solutiongenerator,evaporator,intensificator,aco_iterations,True)
evaluator = Evaluator(trans_cost,dist_matrix,aco)

pop = evaluator.evaluate(pop)
#print(pop[0]['fitness'])