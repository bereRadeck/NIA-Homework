from GA_Initializer import *
from GA_Mutator import *


popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [100,100,100,300,500,1000,100,100,300]
offspringsize = 5

initializer = PartiallyRandomInitializer(popsize,demands,capacities)
pop = initializer.initialize()

#create test offspring by just randomly choosing some pop individuals
offspring = np.random.choice(pop,offspringsize)
mutator = Mutator(initializer.capacities)
mutated_offspring = mutator.mutate(offspring)


assert mutated_offspring == offspringsize


#check wether the shapes are the same
for i, individual in enumerate(mutated_offspring):
    assert len(offspring[i]['vehicle_capacities']) == len(mutated_offspring[i]['vehicle_capacities'])
    assert len(offspring[i]['customer_demands']) == len(mutated_offspring[i]['customer_demands'])