from GA_Initializer import Partially_random_Initializer
from GA_Mutator import Mutator
from GA_Recombiner import Recombiner
from GA_Selector import Selector
from GA_Main import GA


#get problem:
# capacities =
# demands =
# trans_cost =
# dist_matrix =

mutate_prob =

initializer = Partially_random_Initializer(capacities,demands,popsize)
mutator =  Mutator(mutate_prob)
recombiner = Recombiner(recombine_prob)
selector = Selector(tran_cost,dist_matrix)

GA = GA(initializer,recombiner,mutator,selector)

result = GA.run()