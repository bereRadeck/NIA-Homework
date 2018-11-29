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
        self.terminator = terminator
        self.pop = self.initializer.initialize()


    def run(self):

        pop = self.initializer.initialize_partially_random()

        while not terminator.terminates():
            new_offspring = self.__generate_offspring(pop)
            mutated_offspring = self.__mutate_offspring(new_offspring)
            self.pop = self.__select_new_pop(mutated_offspring)



    def __generate_offspring(self,pop):
        return self.recombiner.recombine()

    def __mutate_offsprint(self,off_spring):
        return self.mutator.mutate()

    def __select_new_pop(self,mutated_offspring):
        return self.selector.select()



