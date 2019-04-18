
import numpy as np
from collections import Counter
from GA_Alternative_recombiner import *
from GA_Selector import *
from GA_Initializer import *

dict = {1:3,2:4,3:6,4:4,5:6}

parent1 = []
for key in dict.keys():
    for value in range(dict[key]):
        parent1.append(key)

keys = list(dict.keys())
np.random.shuffle(keys)

parent2 = []
for key in keys:
    for value in range(dict[key]):
        parent2.append(key)

vehicles = np.unique(parent1)
vehicle_1,vehicle_2 = np.random.choice(vehicles,2,replace=False)

parent1 = np.array(parent1)
parent2 = np.array(parent2)
parent1_copy = np.array(parent1)
parent2_copy = np.array(parent2)

# put vehicles at their new place
parent1[parent2 == vehicle_1] = parent1[parent1 == vehicle_1]
parent2[parent1_copy == vehicle_2] = parent2_copy[parent2_copy == vehicle_2]

# replace the old vehicleindices with values that were at the place of the car before
parent1[parent1_copy == vehicle_1] = parent1_copy[parent2_copy == vehicle_1]
parent2[parent2_copy == vehicle_2] = parent2_copy[parent1_copy == vehicle_2]

counter1 = Counter(parent1)
for value in np.unique(parent1):
    assert counter1[value] == dict[value]

counter2 = Counter(parent2)
for value in np.unique(parent2):
    assert counter2[value] == dict[value]

popsize = 10
demands = [10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10]
capacities = [100,100,100,300,500,1000,100,100,300]
offspringsize = 5


selector = Roulette_Selector(offspringsize)
initializer = PartiallyRandomInitializer(popsize,demands,capacities)
pop = initializer.initialize()

all_c = np.sum(capacities)
print(all_c)

for individual in pop:
    individual['fitness'] = np.random.randint(1,10)

for p in pop:
    assert len(p['vehicle_capacities']) == all_c


parents = selector.select(pop)
recombiner = Recombiner()
offspring = recombiner.recombine(parents)

for o in offspring:
    print(len(o['vehicle_capacities']))
    assert len(o['vehicle_capacities']) == all_c