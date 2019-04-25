import random
import numpy as np
from copy import deepcopy



class Evaluator:

    def __init__(self, trans_cost, dist_matrix, aco):
        self.trans_cost = trans_cost
        self.dist_matrix = dist_matrix
        self.aco = aco


    def evaluate_statistics(self,pop):
        fitnesses = [p['fitness'] for p in pop]
        best_score = np.min(fitnesses)
        mean_score = np.mean(fitnesses)
        worst_score = np.max(fitnesses)
        return best_score,worst_score,mean_score



    def re_evaluate(self,pop,verbose=False):
        """
        evaluates each individual of a population, by finding the bests routes for the car-customer assignments with ACO and summing up the route-costs
        :param pop: the population
        :return: population with updated fitness values
        """
        dummy_individual = pop[0]
        best_score = np.inf
        all_scores = []
        for individual in pop:
            if individual['fitness'] != 0:
                continue
            else:
                v_c =  np.array(individual['vehicle_capacities'])
                c_d =  np.array(individual['customer_demands'])
                assert len(dummy_individual['vehicle_capacities']) == len(v_c)
                assert len(v_c) >= 1
                assert len(v_c) == len(c_d), 'v_c: {}c_d: {}'.format(len(v_c),len(c_d))

                costs =  []
                for vehicle in np.unique(v_c):
                    #print('c_d[v_c==vehicle]',c_d[v_c==vehicle])
                    customers_to_visit = np.unique(c_d[v_c==vehicle])
                    # make sure car starts from depot and ands with depot
                    if not customers_to_visit[0] == 0:
                        customers_to_visit = np.append(0,customers_to_visit)


                    assert len(customers_to_visit) >= 1
                    if len(customers_to_visit) == 1:
                        route_length = 0
                    else:
                        route_length = self.aco.run(customers_to_visit)

                    route_costs = route_length * self.trans_cost[vehicle]

                    costs.append(route_costs)

                fitness = np.sum(costs)
                assert fitness != 0
                individual['fitness'] = fitness
                if fitness < best_score:
                    best_score = fitness
                all_scores.append(fitness)
                if verbose:
                    print('Evaluator: ')

                    print('     fitness: {}',format(fitness))



        return pop, best_score, np.mean(all_scores)


