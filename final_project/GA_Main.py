import GA_Initializer
import GA_Mutator
import GA_Recombiner
import GA_Selector

class GA:

    def __init__(self,initializer,selector,recombiner,mutator,terminator):
        self.initializer = initializer
        self.recombiner = recombiner
        self.mutator = mutator
        self.selector = selector
        #self.terminator = terminator
        #self.pop = self.initializer.initialize()


    def run(self):

        pop = self.initializer.initialize_partially_random()

        while not terminator.terminates():
            new_offspring = self.recombiner.recombine(pop)
            mutated_offspring = self.mutator.mutate(new_offspring)
            self.pop = self.selector.select(mutated_offspring)




