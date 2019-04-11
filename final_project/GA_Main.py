
from GA_Initializer import *
from GA_Evaluator import *
from GA_Selector import *
from GA_Recombiner import *
from GA_Mutator import *
from GA_Replacer import *
from GA_Terminator import *
from ACO_Main import ACO as aco


class GA:

    def __init__(self, initializer, evaluator, selector, recombiner, mutator, replacer, terminator, aco):
        self.initializer = initializer
        self.evaluator = evaluator
        self.selector = selector
        self.recombiner = recombiner
        self.mutator = mutator
        self.replacer = replacer
        self.terminator = terminator
        self.aco = aco
        #self.pop = self.initializer.initialize()

    def run(self):

        pop = self.initializer.initialize_partially_random()

        while not terminator.terminates():
            pop = self.evaluator.evaluate(pop)

            pop = self.selector.select(mutated_offspring)
            new_offspring = self.recombiner.recombine(pop)
            mutated_offspring = self.mutator.mutate(new_offspring)
            pop = self.replacer.replace(pop, mutated_offspring)

def __main__():

    aco = aco()
    initializer = PartiallyRandomInitializer()
    evaluator = Evaluator(aco)
    selector = Tournament_Selector(offspring_size= 10)
    recombiner = Ordered_Recombiner(initializer.capacities)
    mutator = Mutator(initializer.capacities)
    replacer = Replacer_All()
    terminator = Terminator(limit = 500)

    ga = GA(initializer, evaluator, selector, recombiner, mutator, replacer, terminator, aco))
    ga.run()
  

