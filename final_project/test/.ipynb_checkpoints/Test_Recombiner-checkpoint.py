from GA_Initializer import *
from GA_Selector import *
from GA_Recombiner import *



popsize = 10
demands = [10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10]
capacities = [100,100,100,300,500,1000,100,100,300]
offspringsize = 5


selector = Roulette_Selector(offspringsize)
initializer = PartiallyRandomInitializer(popsize,demands,capacities)
pop = initializer.initialize()
parents = selector.select(pop)

recombiner = Ordered_Recombiner(initializer.capacities)

offspring = recombiner.recombine(parents)

print(offspring)
#oder:
#assert len(offspring) == offspringsize #(je nachdem ob wir zwei oder ein kind pro elternpaar machen)

