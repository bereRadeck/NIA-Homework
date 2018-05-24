# Power Plant Problem
import numpy as np


class PPP:

    def __init__(self,problem_number):
        #self.xmin = xmin
        #self.xmax = xmax
        # initialize chromosome vector randomly  within the search space
        # constrained by the prescribed minimum and maximum bounds:

        #d = len(xmin)
        #self.x = xmin + (xmax-xmin) * np.random.uniform(0, 1, d)

        #alternative:
        #self.x = np.zeros(d)
        #for i in range(d):
           # self.x[i] = np.random.uniform(xmin[i], xmax[i])
        
        #kwhPerPlant for each type of plant == k in slides
        self.kwh_p1 = 50000
        self.kwh_p2 = 600000
        self.kwh_p3 = 4000000
        
        #costPerPlant for each type of plant == c in slides
        self.cost_p1 = 10000
        self.cost_p2 = 80000
        self.cost_p3 = 400000
        
        #sets values according to the problem that was asked for
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
            
        self.upper_bound_array = [(self.max_number_p1*self.kwh_p1), (self.max_number_p2*self.kwh_p2), (self.max_number_p3*self.kwh_p3),
                             self.max_demand_p1, self.max_demand_p2, self.max_demand_p3,
                             self.max_price_p1, self.max_price_p2, self.max_price_p3]
        
        print("upper_bound_array: ",self.upper_bound_array)
        
        self.vector_array = np.zeros(9)
        i = 0
        #first 6 vectors get initialized as int with 0 as lower bound and max as higher bound
        while i <= 5:
            self.vector_array[i] = int(np.random.uniform(0.0, self.upper_bound_array[i]+1))
        #last 3 vectors get initialized as float with 0 as lower bound and max as higher bound
        while i <= 8:
            self.vector_array[i] = float(np.random.uniform(0.0, self.upper_bound_array[i]+0.1))
        
        print("vector_array: ",self.vector_array)
        
        #self.profit()
        self.return_vector()

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

    def cost_total(self):
        cost_plants_type1 = production_cost_per_planttype(self.kwh_p1,self.cost_p1, self.max_number_p1, vector_array[0])
        cost_plants_type2 = production_cost_per_planttype(self.kwh_p2,self.cost_p2, self.max_number_p2, vector_array[1])
        cost_plants_type3 = production_cost_per_planttype(self.kwh_p3,self.cost_p3, self.max_number_p3, vector_array[2])
        #keeps track of the difference between energy produced and sold
        energy_tobuy = (self.vector_array[3]+self.vector_array0[4]+self.vector_array[5])-(self.vector_array[0]+self.vector_array[1]+self.vector_array[2])
        purchasing_cost = 0
        #evaluates costs if more energy sold then produced
        if(energy_tobuy > 0):
            purchasing_cost = energy_tobuy*self.cost_price
        
        return cost_plants_type1+cost_plants_type2+cost_plants_type3+purchasing_cost

    def demand(price, maxPrice, maxDemand):
        #if price is greater then max price, return 0
        if(price > maxPrice):
            return 0
        
        #if product is free return max demand(ignore negative prices)
        if(price <= 0):
            return maxDemand
        
        #else determine demand based on price
        demand = maxDemand - price**2 * maxDemand / maxPrice**2
        
        return demand
        
        
    def return_vector(self):
        return self.vector_array
    
    def revenue(self):
        revenue_1 = min(self.demand(self.vector_array[6], self.max_price_p1, self.max_demand_p1),self.vector_array[3])*self.vector_array[6]
        revenue_2 = min(self.demand(self.vector_array[7], self.max_price_p2, self.max_demand_p2),self.vector_array[4])*self.vector_array[7]
        revenue_3 = min(self.demand(self.vector_array[8], self.max_price_p3, self.max_demand_p3),self.vector_array[5])*self.vector_array[8]
        return revenue_1+revenue_2+revenue_3

    def profit(self):
        return self.revenue()-self.cost_total()