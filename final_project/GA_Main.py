
from GA_Initializer import *
from GA_Evaluator import *
from GA_Selector import *
from GA_Recombiner import *
from GA_Mutator import *
from GA_Replacer import *
from GA_Terminator import *
from ACO_Main import ACO


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
        print('initializing population')
        pop = self.initializer.initialize()
        print('...done')

        while not self.terminator.terminates():

            # calculate the fitnesses of the individuals
            pop = self.evaluator.evaluate(pop)
            # select parents based on their fitness
            parents = self.selector.select(pop)
            # recombine the  parents  to create offspring
            new_offspring = self.recombiner.recombine(parents)

            # mutate the offspring
            mutated_offspring = self.mutator.mutate(new_offspring)

            # recalculate the fitness of the offspring
            mutated_offspring = self.evaluator.evaluate(mutated_offspring)
            # replace the weak individuals with the offspring
            pop = self.replacer.replace(pop, mutated_offspring)

def __main__():

    aco = ACO()
    initializer = PartiallyRandomInitializer()
    evaluator = Evaluator(aco)
    selector = Tournament_Selector(offspring_size= 10)
    recombiner = Ordered_Recombiner(initializer.capacities)
    mutator = Mutator(initializer.capacities)
    replacer = Replacer_All()
    terminator = Terminator(limit = 10)

    ga = GA(initializer, evaluator, selector, recombiner, mutator, replacer, terminator, aco)
    ga.run()
  

