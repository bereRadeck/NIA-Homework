from ACO_Initializer import ACO_Initializer
from ACO_SolutionGenerator import SolutionGenerator
from ACO_Evaporator import Evaporator
from ACO_Intensificator import Intensificator
from ACO_Main import ACO
from final_project.GA_Initializer import *

import numpy as np


#popsize = 10
#demands = [10,20,10,14,30,20,10]
#capacities = [50,100,100,200]
#initializer = RandomInitializer(popsize,demands,capacities)
#pop = initializer.initialize()
#dist_matrix = np.ones((8,8))
#trans_cost = [2,3,4,5]


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

initializer = PartiallyRandomInitializer(popsize,demands,capacities)
aco = ACO(dist_matrix,aco_initializer,solutiongenerator,evaporator,intensificator,aco_iterations,True)

customers_to_visit = [2,4,5]

route_legth = aco.run(customers_to_visit)

assert np.array(route_legth).shape == ()