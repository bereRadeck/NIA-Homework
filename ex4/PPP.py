# Power Plant Problem
import numpy as np
import math


class PPP:

    def __init__(self, problem_number):

        #kwhPerPlant for each type of plant == k in slides
        self.kwh_p1 = 50000
        self.kwh_p2 = 600000
        self.kwh_p3 = 4000000
        
        #costPerPlant for each type of plant == c in slides
        self.cost_p1 = 10000
        self.cost_p2 = 80000
        self.cost_p3 = 400000
        
        #sets values according to the problem that was asked for (the three different problems from the lecture
        #we know that we could have vectorized this but we choosed this stile for better overview
        if (problem_number == 1):
            #maximum number of Plants for each type of plant == m in slides
            self.max_number_p1 = 100
            self.max_number_p2 = 50
            self.max_number_p3 = 3
            #maximum price for each market == p in slides 
            self.max_price_p1 = 0.45
            self.max_price_p2 = 0.25
            self.max_price_p3 = 0.2
            #maximum demand for each market == d in slides
            self.max_demand_p1 = 2000000
            self.max_demand_p2 = 30000000
            self.max_demand_p3 = 20000000
            #price at which energy isn to buy if more sold then produced
            self.cost_price = 0.6
        
        if (problem_number == 2):
            #maximum number of Plants for each type of plant == m in slides
            self.max_number_p1 = 100
            self.max_number_p2 = 50
            self.max_number_p3 = 3
            #maximum price for each market == p in slides 
            self.max_price_p1 = 0.45
            self.max_price_p2 = 0.25
            self.max_price_p3 = 0.2
            #maximum demand for each market == d in slides
            self.max_demand_p1 = 2000000
            self.max_demand_p2 = 30000000
            self.max_demand_p3 = 20000000
            #price at which energy isn to buy if more sold then produced
            self.cost_price = 0.1
            
        if (problem_number == 3):
            #maximum number of Plants for each type of plant == m in slides
            self.max_number_p1 = 100
            self.max_number_p2 = 50
            self.max_number_p3 = 3
            #maximum price for each market == p in slides
            self.max_price_p1 = 0.5
            self.max_price_p2 = 0.3
            self.max_price_p3 = 0.1
            #maximum demand for each market == d in slides
            self.max_demand_p1 = 1000000
            self.max_demand_p2 = 5000000
            self.max_demand_p3 = 5000000
            #price at which energy isn to buy if more sold then produced
            self.cost_price = 0.6
            
        #generates xmax for initializing the vectors (xmin is zero) depending on the problem that was selected
        self.upper_bound_array = [(self.max_number_p1*self.kwh_p1), (self.max_number_p2*self.kwh_p2), (self.max_number_p3*self.kwh_p3),
                             self.max_demand_p1, self.max_demand_p2, self.max_demand_p3,
                             self.max_price_p1, self.max_price_p2, self.max_price_p3]
        

    def production_cost_per_planttype(self, kwhPerPlant, costPerPlant, maxPlants, energy):
        #if nothing is requested, return 0
        if(energy <= 0):
            return 0;
        
        #if more energy is requested then can be generated, return very large value
        if(energy > kwhPerPlant*maxPlants):
            large = 10000000000000
            return large
        
        #determine number of plants needed to generate requested energy
        plantsNeeded = math.ceil(energy / kwhPerPlant)
        
        return plantsNeeded*costPerPlant        

    def cost_total(self,vector_array):
        cost_plants_type1 = self.production_cost_per_planttype(self.kwh_p1,self.cost_p1, self.max_number_p1, vector_array[0])
        cost_plants_type2 = self.production_cost_per_planttype(self.kwh_p2,self.cost_p2, self.max_number_p2, vector_array[1])
        cost_plants_type3 = self.production_cost_per_planttype(self.kwh_p3,self.cost_p3, self.max_number_p3, vector_array[2])
        #keeps track of the difference between energy produced and sold
        energy_tobuy = (vector_array[3]+vector_array[4]+vector_array[5])-(vector_array[0]+vector_array[1]+vector_array[2])
        purchasing_cost = 0
        #evaluates costs if more energy sold then produced
        if(energy_tobuy > 0):
            purchasing_cost = energy_tobuy*self.cost_price
        
        return cost_plants_type1+cost_plants_type2+cost_plants_type3+purchasing_cost

    def demand(self, price, maxPrice, maxDemand):
        #if price is greater then max price, return 0
        if(price > maxPrice):
            return 0
        
        #if product is free return max demand(ignore negative prices)
        if(price <= 0):
            return maxDemand
        
        #else determine demand based on price
        demand = maxDemand - price**2 * maxDemand / maxPrice**2
        
        return demand
        
        
    def create_vector(self):
        """
        creates an individual (chromosome) within the problem dependent boundaries
        :return: a chromosome
        """
        self.vector_array = np.zeros(9)
        #initializes this member of the population as array randomly within given boundarys
        for i in range(9):
            self.vector_array[i] = (np.random.uniform(0.0, self.upper_bound_array[i]))
        return self.vector_array
    
    def revenue(self,vector_array):
        #calculate revenue
        revenue_1 = min(self.demand(vector_array[6], self.max_price_p1, self.max_demand_p1),vector_array[3])*vector_array[6]
        revenue_2 = min(self.demand(vector_array[7], self.max_price_p2, self.max_demand_p2),vector_array[4])*vector_array[7]
        revenue_3 = min(self.demand(vector_array[8], self.max_price_p3, self.max_demand_p3),vector_array[5])*vector_array[8]
        return revenue_1+revenue_2+revenue_3

    def profitself(self):
        return self.revenue(vector_array=self.vector_array)-self.cost_total(vector_array=self.vector_array)
    
    def profit(self, vector_array):
        return self.revenue(vector_array=vector_array)-self.cost_total(vector_array=vector_array)
