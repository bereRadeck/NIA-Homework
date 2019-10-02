
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

    def __init__(self, initializer, evaluator, selector, recombiner, mutator, replacer, terminator, aco,  n, evaluate='greedy'):
        self.initializer = initializer
        self.evaluator = evaluator
        self.selector = selector
        self.recombiner = recombiner
        self.mutator = mutator
        self.replacer = replacer
        self.terminator = terminator
        self.aco = aco
        self.n = n
        self.record_best = []
        self.record_worst = []
        self.record_mean = []
        self.record_fitnesses = []
        self.evaluate=evaluate
        #self.pop = self.initializer.initialize()

    def run(self):
        print('initializing population')
        pop = self.initializer.initialize()#True)
        print('...done')


        # calculate the initial fitnesses of the individuals
        #print('calculate initial fitness-scores for each pop-individual with ACO ')
        #pop, best_score, mean_score = self.evaluator.evaluate_with_aco(pop)
        #print('\t initial best score: ',best_score)
        #print('\t initial mean score: ', mean_score)
        print('calculate initial fitness-scores for each pop-individual with Greedy ')
        pop = self.evaluator.evaluate_greedy(pop)
        best, worst, mean,fitnesses = self.evaluator.evaluate_statistics(pop)

        print('\t   -initial mean score: {}'.format(np.round(mean, 2)))
        print('\t   -initial best score: {}'.format(best))
        print('\t   -initial worst score: {}'.format(worst))
        self.record_mean.append(mean)
        self.record_best.append(best)
        self.record_worst.append(worst)
        self.record_fitnesses.append(fitnesses)

        iter_count = 0

        while not self.terminator.terminates():



            # select parents based on their fitness
            print('\tselecting parents')
            parents = self.selector.select(pop)

            # recombine the  parents  to create offspring
            print('\trecombine parents')
            new_offspring = self.recombiner.recombine(parents)

            # mutate the offspring
            print('\tmutate offspring')
            mutated_offspring = self.mutator.mutate(new_offspring)


            #if iter_count % self.n == 0:

                # recalculate the fitness of the offspring
                #print('\tcalculate fitness of offspring (with ACO)')
                #mutated_offspring, _, _ = self.evaluator.evaluate_with_aco(mutated_offspring)



            #else:
            print('\tcalculate fitness of offspring (greedy)')
            if self.evaluate == 'greedy':
                mutated_offspring = self.evaluator.evaluate_greedy(mutated_offspring)
            if self.evaluate == 'aco':
                mutated_offspring = self.evaluator.evaluate_with_aco(mutated_offspring)
            else:
                mutated_offspring = self.evaluator.evaluate_simple(mutated_offspring)
            #pop = self.evaluator.evaluate_greedy(pop)

            # recalculate the fitness of the offspring
            #print('\tcalculate fitness of offspring')
            #mutated_offspring, _, _ = self.evaluator.evaluate_with_aco(mutated_offspring)


            # replace the weak individuals with the offspring
            print('\treplace weak individuals with offspring')
            pop = self.replacer.replace(pop, mutated_offspring)
            #if iter_count % self.n == 0:
            #pop, best_score, mean_score = self.evaluator.evaluate_with_aco(pop)
            best, worst, mean, fitnesses = self.evaluator.evaluate_statistics(pop)

            print('\t   -mean score: {}'.format(np.round(mean, 2)))
            print('\t   -best score: {}'.format(best))
            print('\t   -worst score: {}'.format(worst))
            self.record_mean.append(mean)
            self.record_best.append(best)
            self.record_worst.append(worst)
            self.record_fitnesses.append(fitnesses)
            iter_count += 1



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
  

