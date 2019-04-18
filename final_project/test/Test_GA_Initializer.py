from final_project.GA_Initializer import *
import numpy as np

popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
initializer = RandomInitializer(popsize,demands,capacities)

assert initializer.popsize == popsize
assert initializer.capacities == capacities
assert initializer.demands == demands
assert np.allclose(initializer.vehicles, np.array([0,1,2,3]))
assert np.allclose(initializer.customers, np.array([1,2,3,4,5,6,7]))
assert initializer.total_capacity == 450
assert initializer.total_demand == 114

pop = initializer.initialize()
assert len(pop) == popsize
assert len(pop[0]['vehicle_capacities']) == 450
#assert len(pop[0]['customer_demands']) == 114 #nullen werden appended
assert len(pop[0]['customer_demands']) == 450

assert len(np.unique(pop[0]['vehicle_capacities'])) == len(capacities)
#assert len(np.unique(pop[0]['customer_demands'])) == len(demands) #nullen werden appended
assert len(np.unique(pop[0]['customer_demands'])) == len(demands) +1

assert pop[0]['fitness'] == 0

assert not np.allclose(pop[0]['vehicle_capacities'], pop[1]['vehicle_capacities'])
assert np.allclose(pop[0]['customer_demands'], pop[1]['customer_demands'])
print('test partially random initializer')

initializer = PartiallyRandomInitializer(popsize,demands,capacities)
pop = initializer.initialize()
assert len(pop) == popsize
assert len(pop) == popsize
assert len(pop[0]['vehicle_capacities']) == 450
assert len(pop[0]['customer_demands']) == 114
#print(pop[0])
#print(np.unique(pop[0]['vehicle_capacities']))
assert len(np.unique(pop[0]['vehicle_capacities'])) == len(capacities)
assert len(np.unique(pop[0]['customer_demands'])) == len(demands)

assert not np.allclose(pop[0]['vehicle_capacities'], pop[1]['vehicle_capacities'])
assert not np.allclose(pop[0]['customer_demands'], pop[1]['customer_demands'])