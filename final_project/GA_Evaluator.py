import random
import numpy as np
from copy import deepcopy



class Evaluator:

    def __init__(self, trans_cost, dist_matrix, aco):
        self.trans_cost = trans_cost
        self.dist_matrix = dist_matrix
        self.aco = aco


    def evaluate(self,pop):
        """
        evaluates each individual of a population, by finding the bests routes for the car-customer assignments with ACO and summing up the route-costs
        :param pop: the population
        :return: population with updated fitness values
        """
        dummy_individual = pop[0]

        for individual in pop:
            v_c =  np.array(individual['vehicle_capacities'])
            c_d =  np.array(individual['customer_demands'])
            assert len(dummy_individual['vehicle_capacities']) == len(v_c)
            assert len(v_c) != 0


            costs =  []
            for vehicle in np.unique(v_c):

                customers_to_visit = np.unique(c_d[v_c[v_c==vehicle]])

                route_costs = self.aco.run(customers_to_visit) * self.trans_cost[vehicle]
                assert route_costs != 0


                costs.append(route_costs)

            assert np.sum(costs) != 0
            individual['fitness'] = np.sum(costs)



        return pop


