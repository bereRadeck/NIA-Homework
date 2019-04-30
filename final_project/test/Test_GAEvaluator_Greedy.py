from final_project.GA_Evaluator import *
from final_project.GA_Initializer import *


import numpy as np
from collections import Counter

from ACO_Initializer import ACO_Initializer
from ACO_SolutionGenerator import SolutionGenerator
from ACO_Evaporator import Evaporator
from ACO_Intensificator import Intensificator
from ACO_Main import ACO


dummy_aco = []
popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
initializer = PartiallyRandomInitializer(popsize,demands,capacities,dummy_aco)

popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]

initializer = RandomInitializer(popsize,demands,capacities,dummy_aco)

pop = initializer.initialize()
dist_matrix = np.ones((8,8))
trans_cost = [2,3,4,5]


popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
dist_matrix = np.ones((8,8))
trans_cost = [2,3,4,5]
aco_iterations = 5
mutate_probability = 0.1

aco_initializer = ACO_Initializer()
solutiongenerator = SolutionGenerator()
evaporator = Evaporator()
intensificator = Intensificator()


dist_matrix = np.ones((8,8))

for i in range(dist_matrix.shape[0]):
    for j in range(dist_matrix.shape[1]):
        dist_matrix[i,j] = i*8+j

print(dist_matrix)

aco = ACO(dist_matrix,aco_initializer,solutiongenerator,evaporator,intensificator,aco_iterations,True)
evaluator = Evaluator(trans_cost,dist_matrix,aco)

pop = evaluator.evaluate_greedy(pop)