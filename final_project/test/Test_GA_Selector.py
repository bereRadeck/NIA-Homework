from final_project.GA_Selector import *
from final_project.GA_Initializer import *
import numpy as np


popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
initializer = RandomInitializer(popsize,demands,capacities)
pop = initializer.initialize()

for individual in pop:
    individual['fitness'] = np.random.randint(1,10)



offspringsize = 5
selector = Roulette_Selector(offspringsize)

parents = selector.select(pop)
assert len(parents) == offspringsize
assert not np.allclose(parents[0][0]['vehicle_capacities'],parents[0][1]['vehicle_capacities'])
assert not np.allclose(parents[1][0]['vehicle_capacities'],parents[0][0]['vehicle_capacities'])


selector = Tournament_Selector(offspringsize)

parents = selector.select(pop)
assert len(parents) == offspringsize
#assert not np.allclose(parents[0][0]['vehicle_capacities'],parents[0][1]['vehicle_capacities'])
#assert not np.allclose(parents[1][0]['vehicle_capacities'],parents[0][0]['vehicle_capacities']), print(parents[1][0]['vehicle_capacities'], '\n',parents[0][0]['vehicle_capacities'])