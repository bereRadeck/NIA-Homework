
#from GA_Taskinitializer import *
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
        pop = self.initializer.initialize(True)
        print('...done')

        # calculate the initial fitnesses of the individuals
        pop, best_score, mean_score = self.evaluator.re_evaluate(pop)

        while not self.terminator.terminates():


            # select parents based on their fitness
            parents = self.selector.select(pop)
            # recombine the  parents  to create offspring
            new_offspring = self.recombiner.recombine(parents)

            # mutate the offspring
            mutated_offspring = self.mutator.mutate(new_offspring)

            # recalculate the fitness of the offspring
            mutated_offspring, _, _ = self.evaluator.re_evaluate(mutated_offspring)
            # replace the weak individuals with the offspring
            pop = self.replacer.replace(pop, mutated_offspring)

            best, worst, mean = self.evaluator.evaluate_statistics(pop)

            print('   -mean score: {}'.format(np.round(mean,2)))
            print('   -best score: {}'.format(best))
            print('   -worst score: {}'.format(worst))

"""
def __main__():
    print("Main")

    aco_iterations = 10
    
    #GA
    popsize = 12

    taskinitializer = Taskinitializer()
    distance_matrix, capacities, transportation_costs, demands = taskinitializer.initialize_task()

    aco_initializer = ACO_Initializer()
    aco_solutiongenerator = SolutionGenerator()
    aco_evaporator = Evaporator()
    aco_intensificator = Intensificator()
    aco = ACO(distance_matrix, aco_initializer, aco_solutiongenerator, aco_evaporator, aco_intensificator, aco_iterations, True)

    initializer = PartiallyRandomInitializer(popsize, demands, capacities, aco)
    evaluator = Evaluator(transportation_costs, distance_matrix, aco)
    selector = Tournament_Selector(offspring_size= 6)
    recombiner = Ordered_Recombiner(initializer.capacities) #TODO capacities für verschiedene Dinge benutzt
    mutator = Mutator(initializer.capacities)
    replacer = Replacer_All()
    terminator = Terminator(limit = 100)

    ga = GA(initializer, evaluator, selector, recombiner, mutator, replacer, terminator, aco)
    ga.run()

#__main__()"""
  

