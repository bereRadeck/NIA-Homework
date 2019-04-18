from GA_Initializer import *
from GA_Selector import *
from GA_Recombiner import *



popsize = 10
demands = [10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10,10,20,10,14,30,20,10]
capacities = [100,100,100,300,500,1000,100,100,300]
offspringsize = 5
from collections import Counter


selector = Roulette_Selector(offspringsize)
initializer = PartiallyRandomInitializer(popsize,demands,capacities)
pop = initializer.initialize()

all_c = np.sum(capacities)

for individual in pop:
    individual['fitness'] = np.random.randint(1,10)

for p in pop:
    assert len(p['vehicle_capacities']) == all_c


parents = selector.select(pop)
recombiner = Ordered_Recombiner(initializer.capacities)


# make a default vehicle_capacity list
v_c = []
for i,value in enumerate(capacities):
    for j in range(value):
        v_c.append(i)


counter_0 = Counter(v_c)

unique_vehicles = np.append(0,np.unique(initializer.capacities))
for parent_pair in parents:
    for p in parent_pair:
        #test wether the same amount of cars are in the vehicle capacities
        assert len(np.unique(p['vehicle_capacities'])),len(unique_vehicles)

        # test whether each cars occurs the same amount of times
        counter1 = Counter(p['vehicle_capacities'])
        for value in np.unique(p['vehicle_capacities']):
            assert counter_0[value] == counter1[value]


offspring = recombiner.recombine(parents)

for o in offspring:
    assert len(o['vehicle_capacities']) == all_c
#oder:
#assert len(offspring) == offspringsize #(je nachdem ob wir zwei oder ein kind pro elternpaar machen)

