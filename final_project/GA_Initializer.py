import numpy as np
from abc import ABC, abstractmethod


class Initializer(ABC):

    def __init__(self,popsize,demands,capacities):
        self.popsize = popsize
        self.customers = np.arange(1,len(demands)+1)
        self.demands = demands
        self.vehicles = np.arange(0,len(capacities))
        self.capacities = capacities
        self.total_capacity = sum(capacities)
        self.total_demand = sum(demands)


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
        for i, vehicle in enumerate(vehicles):
            for c in range(capacities[i]):
                vehicle_capacity.append(vehicle)
        return np.array(vehicle_capacity)


    def generate_customer_demand(self, customers, demands):
        """
        generates an array out of customers and their demands
        each customer appears as many times as his demand big is

        :return: customer_demand array
        """

        customer_demand = []
        for i, customer in enumerate(customers):
            for d in range(demands[i]):
                customer_demand.append(customer)
        return np.array(customer_demand)


class RandomInitializer(Initializer):

    def initialize(self):
        """
        initializes totally randomly sorted vehicle_capacity arrays
        where car apperances could be apart [car3,car2,car2,car1,car2,car3]
        :return: a population of size popsize
        """
        v_c = self.generate_vehicle_capacity(self.vehicles, self.capacities)
        c_d = self.generate_customer_demand(self.customers,self.demands)

        while len(c_d) < len(v_c):
            c_d.append(0)
        
        population = [dict() for x in range(self.popsize)]
        sort_array = np.arange(0,self.total_capacity)


        for i in range(self.popsize):
            np.random.shuffle(sort_array)
            population[i]['vehicle_capacities'] = v_c[sort_array]
            population[i]['customer_demands'] = c_d
            #population[i]['capacities_list'] = self.capacities
            population[i]['fitness'] = 0
        return population

class PartiallyRandomInitializer(Initializer):

    def initialize(self):
        """
        initializes randomly sorted vehicle_capacity arrays where
        each car-apperance stays together [car3,car3,car1,car2,car2,car2]
        :return: a population of size popsize
        """

        population = [dict() for x in range(self.popsize)]
        for i in range(self.popsize):

            mixed_up_vehicles = np.copy(self.vehicles)
            np.random.shuffle(mixed_up_vehicles)
            mixed_up_customers = np.copy(self.customers)
            np.random.shuffle(mixed_up_customers)

            population[i]['vehicle_capacities'] = self.generate_vehicle_capacity(mixed_up_vehicles, self.capacities)
            population[i]['customer_demands'] = self.generate_customer_demand(mixed_up_customers,self.demands)
            #population[i]['capacities_list'] = self.capacities
            population[i]['fitness'] = 0

        return population



