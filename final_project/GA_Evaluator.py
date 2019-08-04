import random
import numpy as np
from copy import deepcopy
from datetime import datetime



class Evaluator:

    def __init__(self, trans_cost, dist_matrix, aco):
        self.trans_cost = trans_cost
        self.dist_matrix = dist_matrix
        self.aco = aco

        self.fitnesses=None


    def evaluate_statistics(self,pop):
        fitnesses = [p['fitness'] for p in pop]
        best_score = np.min(fitnesses)
        mean_score = np.mean(fitnesses)
        worst_score = np.max(fitnesses)
        self.fitnesses = fitnesses
        return best_score, worst_score, mean_score, fitnesses

    def evaluate_simple(self,pop):
        for individual in pop:
            v_c = np.array(individual['vehicle_capacities'])
            c_d = np.array(individual['customer_demands'])
            costs = 0
            for vehicle in np.unique(v_c):
                customers_to_visit = np.unique(c_d[v_c == vehicle])
                customers_to_visit = np.append(customers_to_visit,0)
                cost = np.array(self.dist_matrix)[customers_to_visit[:-1],customers_to_visit[1:]].sum()
                costs += cost
            individual['fitness'] = costs

        return pop

    def evaluate_greedy(self,pop):
        for individual in pop:
            dist_matrix = np.array(self.dist_matrix)
            v_c = np.array(individual['vehicle_capacities'])
            c_d = np.array(individual['customer_demands'])
            costs = 0
            for vehicle in np.unique(v_c):
              #  print(len(c_d),len(v_c))
                customers_to_visit = np.sort(np.unique(c_d[v_c == vehicle]))

                if len(customers_to_visit) == 0:
                    costs += 0

                else:

                    if not 0 in customers_to_visit:
                        customers_to_visit =  np.append(0,customers_to_visit)

                    if len(customers_to_visit) > 2:
                        route = self.find_route_greedy(customers_to_visit,0,[0])

                    else:
                        route = np.append(customers_to_visit,0)

                    assert (route[0] == 0) & (route[-1] == 0)
                    cost = np.array(dist_matrix)[route[:-1], route[1:]].sum() * self.trans_cost[vehicle]
                    costs += cost
            assert costs
            individual['fitness'] = costs
        return pop


    def find_route_greedy(self, customers_to_visit: object, current_stop: object = 0, route: object = []) -> object:

        dist_matrix = deepcopy(np.array(self.dist_matrix))

        assert current_stop in customers_to_visit

        customers_to_visit = customers_to_visit[customers_to_visit != current_stop]

        choice = dist_matrix[current_stop,np.array(customers_to_visit)]

        next_stop_candidates = np.where(dist_matrix[current_stop,:] == np.min(choice))[0]
        for next_stop in next_stop_candidates:
            if next_stop in customers_to_visit:
                break

        route.append(next_stop)

        if len(customers_to_visit) <= 1:
            route.append(0)
            return route

        else:
            return self.find_route_greedy(customers_to_visit,next_stop,route)



    def evaluate_with_aco(self,pop,verbose=False):
        """
        evaluates each individual of a population, by finding the bests routes for the car-customer assignments with ACO and summing up the route-costs
        :param pop: the population
        :return: population with updated fitness values
        """
        dummy_individual = pop[0]
        best_score = np.inf
        all_scores = []

        start = datetime.now()
        for individual in pop:
            #if individual['fitness'] != 0:
                #continue
            #else:
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


        stop = datetime.now()
        print('\t Evaluating took: {} seconds'.format((stop-start).seconds))
        return pop, best_score, np.mean(all_scores)
