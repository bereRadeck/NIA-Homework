from final_project.GA_Replacer import *
from final_project.GA_Initializer import *
import numpy as np


popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
initializer = RandomInitializer(popsize,demands,capacities)
offspring_size = 5
replacer = Replacer()
pop = initializer.initialize()

for individual in pop:
    individual['fitness'] = np.random.randint(1,10)

offspring = np.random.choice(pop,offspring_size)

pop = replacer.replace(pop, offspring)
