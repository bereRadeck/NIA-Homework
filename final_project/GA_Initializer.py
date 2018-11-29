import numpy as np
class Initializer():

    def __init__(self,popsize,demands,capacities):
        self.popsize = popsize
        self.customers = np.range(1,len(demands))
        self.demands = demands
        self.vehicles = np.range(1,len(capacities))
        self.capacities = capacities
        self.total_capacity = sum(capacities)
        self.total_demand = sum(demands)


    def generate_vehicle_capacity(self, vehicles, capacities):
        """
        generates a array out of the vehicle- and capacitiy-array
        where each vehicle appears asa many times as its capacities big is
        vehicles = [car1,car2,car3]
        capacities = [1,3,2]
        vecicle_capacity = [car1,car2,car2,car2,car3,car3]
        :return: vehicle_capacity array and its length
        """
        vehicle_capacity = []
        for i, vehicle in enumerate(vehicles):
            for c in range(capacities[i]):
                vehicle_capacity.append(vehicle)
        return vehicle_capacity


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
        return customer_demand



    def initialize_totally_random(self):
        """
        initializes totally randomly sorted vehicle_capacity arrays
        where car apperances could be apart [car3,car2,car2,car1,car2,car3]
        :return: a population of size popsize
        """
        v_c = self.generate_vehicle_capacity(self.vehicles, self.capacities)
        c_d = self.generate_customer_demand(self.customer,self.demands)

        population = [dict() for x in range(popsize)]
        l = self.total_capacity

        for i in range(self.popzize):
            # mixing up the vehicle_capacity
            sort_array = np.random.rand(low=0, high=l, size=l)
            population[i]['vehicle_capacities'] = v_c[sort_array]
            population[i]['customer_demands'] = c_d
            #population[i]['capacities_list']= self.capacities

    def initialize_partially_random(self):
        """
        initializes randomly sorted vehicle_capacity arrays where
        each car-apperance stays together [car3,car3,car1,car2,car2,car2]
        :return: a population of size popsize
        """

        population = [dict() for x in range(popsize)]
        for i in range(self.popsize):
            #randomly change order of vehicles
            sort_array_v = np.random.rand(low=0,high=self.vehicles,size=self.vehicles)
            sort_array_c = np.random.rand(low=0, high=self.customers, size=self.customers)

            mixed_up_vehicles = self.vehicles[sort_array_v]
            mixed_up_customers = self.customers[sort_array_c]
            population[i]['vehicle_capacities'] = self.generate_vehicle_capacity(mixed_up_vehicles, self.capacities)
            population[i]['customer_demands'] = self.generate_customer_demand(mixed_up_customers,self.demands)
            population[i]['capacities_list'] = self.capacities


    def calc_fitness(self,individual):
        pass

    """"
    def calc_splitted_customers(self,vehicle_capacity,customer_demand):
        """

        #:param vehicle_capacity:
        #:param customer_demand:
        #:return: number of customers that are served by more than one car

        """
        n=0
        for i,c in enumerate(customer_demand):
            if c != customer_demand[i+1]:
                if vehicle_capacity[i] == vehicle_capacity[i-1]:
                    n += 1
        for i,v in enumerate(vehicle_capacity):
            if v != vehicle_capacity[i+1]:
                if customer_demand[i] != customer_demand[i+1]:
                    n += 1
        return n"""
