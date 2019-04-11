
class GA_Initializer:

    def __init__(self, popsize, demands, capacities):
        self.popsize = popsize
        self.demands = demands
        self.capacities = capacities


    def initialize(self):
        """

        :return: a list of dictionaries(individuals) that have a vehicle_capacity_list, a customer_demand_list
        and a list of capacities
        """
        return pop


class GA_Recombiner:

    def __init__(self, combine_probability=0.5):
        self.combine_probability = combine_probability

    def recombine(pop):
        """

        :return:
        """
        return off_spring


class GA_Mutator:

    def __init__(self, mutate_probability=0.5):
        self.mutate_probability = mutate_probability

    def mutate(offspring):
        """

        :return:
        """
        return mutated_offspring


class Selector:

    def __init__(self, trans_cost, dist_matrix, pool_size, aco_distance_matrix, aco_initializer, aco_solutiongenerator,
                 aco_evaporator, aco_intensificator, aco_iterations):
        self.trans_cost = trans_cost
        self.dist_matrix = dist_matrix
        self.pool_size = pool_size
        self.aco_distance_matrix = aco_distance_matrix
        self.aco_initializer = aco_initializer
        self.aco_solutiongenerator = aco_solutiongenerator
        self.aco_evaporator = aco_evaporator
        self.aco_intensificator = aco_intensificator
        self.aco_iterations = aco_iterations


    def select(self,mutated_offspring):
        """

        :return:
        """


        for pop_individual in mutated_offspring:

            #
            costumers_to_visit_per_car = self.create_costumers_to_visit_per_car(pop_individual)

            fitness = 0
            for customer_list in costumers_to_visit_per_car:
                # think about how to vizualize a good result.
                fitness +=  self.calc_fitness(customer_list)

        #### blbablabdasls select

        return new_pop



    def create_costumers_tovisit(self, mutated_offspring):

        return costumers_tovisit


    def calc_fitness(self,customer_list):

        ACO = ACO(self.aco_distance_matrix,self.aco_initializer,
                  self.aco_solutiongenerator, self.aco_evaporator, self.aco_intensificator,
                  self.aco_iterations)


        #berechne fitness mit ACO
        return fitness



class ACO:

    def __init__(self,distance_matrix, initializer, solutiongenerator, evaporator, intensificator,
                 iterations, printing=True):
        self.distance_matrix = distance_matrix
        self.initializer = initializer
        self.solutiongenerator = solutiongenerator
        self.intensificator = intensificator
        self.evaporator = evaporator
        self.iterations = iterations
        self.printing = printing

