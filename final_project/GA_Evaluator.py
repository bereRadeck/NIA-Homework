import random
import numpy as np
from copy import deepcopy



class Evaluator:

    def __init__(self, trans_cost, dist_matrix, pool_size, ACO):
        self.trans_cost = trans_cost
        self.dist_matrix = dist_matrix
        self.pool_size = pool_size


    def evaluate(self,individual):
        v_c =  np.array(individual['vehicle_capacities'])
        c_d =  np.array(individual['customer_demands'])

        for vehicle in np.unique(v_c):

            customers_to_visit = np.unique(c_d[v_c[v_c==vehicle]])
            fitness, best_route = ACO(customers_to_visit).run()
