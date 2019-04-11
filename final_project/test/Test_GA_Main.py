from GA_Main import *

from GA_Initializer import *
from GA_Evaluator import *
from GA_Selector import *
from GA_Recombiner import *
from GA_Mutator import *
from GA_Replacer import *
from GA_Terminator import *
from ACO_Main import ACO

from ACO_Initializer import ACO_Initializer
from ACO_SolutionGenerator import SolutionGenerator
from ACO_Evaporator import Evaporator
from ACO_Intensificator import Intensificator

aco_initializer = ACO_Initializer()
solutiongenerator = SolutionGenerator()
evaporator = Evaporator()
intensificator = Intensificator()



popsize = 10
demands = [10,20,10,14,30,20,10]
capacities = [50,100,100,200]
dist_matrix =

initializer = PartiallyRandomInitializer()
aco = ACO()
evaluator = Evaluator(aco)
selector = Tournament_Selector(offspring_size= 10)
recombiner = Ordered_Recombiner(initializer.capacities)
mutator = Mutator(initializer.capacities)
replacer = Replacer_All()
terminator = Terminator(limit = 10)

ga = GA(initializer, evaluator, selector, recombiner, mutator, replacer, terminator, aco)
ga.run()