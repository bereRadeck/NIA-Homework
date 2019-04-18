from final_project.GA_Evaluator import *
from final_project.GA_Initializer import *

from ACO_Initializer import ACO_Initializer
from ACO_SolutionGenerator import SolutionGenerator
from ACO_Evaporator import Evaporator
from ACO_Intensificator import Intensificator
from ACO_Main import ACO

import numpy as np
from collections import Counter



popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
initializer = PartiallyRandomInitializer(popsize,demands,capacities)

popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
initializer = RandomInitializer(popsize,demands,capacities)

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


#####################################################################
v_c = []
for i,value in enumerate(capacities):
    for j in range(value):
        v_c.append(i)

counter_0 = Counter(v_c)
unique_vehicles = np.append(0,np.unique(initializer.capacities))
for p in pop:
    #test wether the same amount of cars are in the vehicle capacities
    assert len(np.unique(p['vehicle_capacities'])),len(unique_vehicles)

    # test whether each cars occurs the same amount of times
    counter1 = Counter(p['vehicle_capacities'])
    for value in np.unique(p['vehicle_capacities']):
        assert counter_0[value] == counter1[value]
########################################################################

pop = evaluator.evaluate(pop)

#####################################################################
v_c = []
for i,value in enumerate(capacities):
    for j in range(value):
        v_c.append(i)

counter_0 = Counter(v_c)
unique_vehicles = np.append(0,np.unique(initializer.capacities))
for p in pop:
    #test wether the same amount of cars are in the vehicle capacities
    assert len(np.unique(p['vehicle_capacities'])),len(unique_vehicles)

    # test whether each cars occurs the same amount of times
    counter1 = Counter(p['vehicle_capacities'])
    for value in np.unique(p['vehicle_capacities']):
        assert counter_0[value] == counter1[value]
########################################################################