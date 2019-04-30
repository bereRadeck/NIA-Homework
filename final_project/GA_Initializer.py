import numpy as np
from abc import ABC, abstractmethod
from collections import Counter
from copy import deepcopy


class Initializer(ABC):
    def __init__(self, popsize, demands, capacities, aco):
        self.popsize = popsize
        self.customers = np.arange(1, len(demands) + 1)
        self.demands = demands
        self.vehicles = np.arange(0, len(capacities))
        self.capacities = capacities
        self.total_capacity = sum(capacities)
        self.total_demand = sum(demands)
        self.aco = aco

    def generate_vehicle_capacity(self, vehicles, capacities):
        """
        generates a array out of the vehicle- and capacitiy-array
        where each vehicle appears as many times as its capacities big is
        vehicles = [car1,car2,car3]
        capacities = [1,3,2]
        vecicle_capacity = [car1,car2,car2,car2,car3,car3]
        :return: vehicle_capacity array and its length
        """
        vehicle_capacity = []
        for i, value in enumerate(capacities):
            for j in range(value):
                vehicle_capacity.append(i)

        #    for c in range(capacities[i]):
        #        vehicle_capacity.append(vehicle)
        return np.array(vehicle_capacity)

    def generate_customer_demand(self, customers, demands):
        """
        generates an array out of customers and their demands
        each customer appears as many times as his demand big is

        :return: customer_demand array
        """

        customer_demand = []
        for i, customer in enumerate(customers):
            for d in range(demands[customer-1]):
                customer_demand.append(customer)
        return np.array(customer_demand)

    '''
    wouldn't this make more sense?
        customer_demand = []
        for i, customer in enumerate(customers):

            for d in range(demands[customer]):
                customer_demand.append(customer)

        return np.array(customer_demand)
    '''


class RandomInitializer(Initializer):

    def initialize(self):
        """
        initializes totally randomly sorted vehicle_capacity arrays
        where car apperances could be apart [car3,car2,car2,car1,car2,car3]
        :return: a population of size popsize
        """
        v_c = self.generate_vehicle_capacity(self.vehicles, self.capacities)
        c_d = self.generate_customer_demand(self.customers, self.demands)

        while len(c_d) < len(v_c):
            c_d = np.append(c_d, 0)

        population = [dict() for x in range(self.popsize)]
        sort_array = np.arange(0, self.total_capacity)

        for i in range(self.popsize):
            np.random.shuffle(sort_array)
            population[i]['vehicle_capacities'] = v_c[sort_array]
            population[i]['customer_demands'] = c_d
            # population[i]['capacities_list'] = self.capacities
            population[i]['fitness'] = 0
        return population


class PartiallyRandomInitializer(Initializer):

    def initialize(self, heuristic=False):
        """
        initializes randomly sorted vehicle_capacity arrays where
        each car-apperance stays together [car3,car3,car1,car2,car2,car2]
        :return: a population of size popsize
        """

        dummy_v_c = self.generate_vehicle_capacity(self.vehicles, self.capacities)
        counter_0 = Counter(dummy_v_c)

        assert len(dummy_v_c) != 0
        population = [dict() for x in range(self.popsize)]

        # only one order of customer demands for all individuals
        mixed_up_customers = deepcopy(self.customers)

        if heuristic == False:
            np.random.shuffle(mixed_up_customers)
        else:
            best_solutions_scores, solutions_generations, evaluations_generations = self.aco.run(
                range(1, len(self.demands) + 1), True)  # TODO start from depot?

            best_solution = [customer_n + 1 for customer_n in solutions_generations[-1]]  # TODO Maybe last is not best
            print("Init:", best_solution, evaluations_generations[-1][0], best_solutions_scores[-1])
            print("", self.customers)
            mixed_up_customers = best_solution

        assert np.allclose(np.unique(mixed_up_customers), np.unique(self.customers))
        assert len(mixed_up_customers) == len(self.customers)

        c_d = self.generate_customer_demand(mixed_up_customers, self.demands)

        for i in range(self.popsize):

            mixed_up_vehicles = deepcopy(self.capacities)
            np.random.shuffle(mixed_up_vehicles)

            assert np.allclose(np.unique(mixed_up_vehicles), np.unique(self.capacities))

            # assert not np.allclose(mixed_up_customers,self.customers)
            # assert not np.allclose(mixed_up_vehicles, self.capacities)

            assert len(mixed_up_vehicles) == len(self.vehicles)

            # population[i]['vehicle_capacities'] = self.generate_vehicle_capacity(mixed_up_vehicles, self.capacities)
            v_c = self.generate_vehicle_capacity(mixed_up_vehicles, self.capacities)

            counter_1 = Counter(v_c)
            for value in np.unique(self.vehicles):
                assert counter_0[value] == counter_1[value]

            assert len(dummy_v_c) == len(v_c)

            while len(c_d) < len(v_c):
                c_d = np.append(c_d, 0)
            assert len(c_d) == len(v_c)
            # population[i]['customer_demands'] = self.generate_customer_demand(mixed_up_customers,self.demands)
            population[i]['vehicle_capacities'] = v_c
            population[i]['customer_demands'] = c_d
            # population[i]['capacities_list'] = self.capacities
            population[i]['fitness'] = 0

        return population


class GreedyInitializer(Initializer):

    def initialize(self,distance_matrix):
        """
        initializes totally randomly sorted vehicle_capacity arrays
        where car apperances could be apart [car3,car2,car2,car1,car2,car3]
        :return: a population of size popsize
        """

        customers = []
        pos = 0
        for x in range(1, len(distance_matrix)):
            customers.append(pos)
            ind = pos
            # print(pos == ind, ind in customers2, pos in customers2, ind, pos)
            dm_copy = deepcopy(distance_matrix)
            while pos in customers:
                pos = np.argmin(dm_copy[ind])
                dm_copy[ind][pos] = np.amax(dm_copy)
        for x in range(1, len(distance_matrix)):
            if x not in customers:
                customers.append(x)

        v_c = self.generate_vehicle_capacity(self.vehicles, self.capacities)
        c_d = self.generate_customer_demand(self.customers[1:], self.demands)

        while len(c_d) < len(v_c):
            c_d = np.append(c_d, 0)

        population = [dict() for x in range(self.popsize)]

        sort_array = np.arange(0, self.total_capacity)
        for i in range(self.popsize):
            np.random.shuffle(sort_array)
            population[i]['vehicle_capacities'] = v_c[sort_array]
            population[i]['customer_demands'] = c_d
            # population[i]['capacities_list'] = self.capacities
            population[i]['fitness'] = 0

        return population

