import GA_Initializer
import GA_Mutator
import GA_Recombiner
import GA_Selector
import GA_Replacer

class GA:

    def __init__(self, initializer, evaluator, selector, recombiner, mutator, replacer, terminator):
        self.initializer = initializer
        self.evaluator = evaluator
        self.selector = selector
        self.recombiner = recombiner
        self.mutator = mutator
        self.replacer = replacer
        self.terminator = terminator
        #self.pop = self.initializer.initialize()

    def run(self):

        pop = self.initializer.initialize_partially_random()

        while not terminator.terminates():
            pop = self.evaluator.evaluate(pop)

            pop = self.selector.select(mutated_offspring)
            new_offspring = self.recombiner.recombine(pop)
            mutated_offspring = self.mutator.mutate(new_offspring)
            pop = self.replacer.replace(pop, mutated_offspring)


