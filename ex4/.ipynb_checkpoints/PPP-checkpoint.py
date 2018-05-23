# Power Plant Problem
import numpy as np


class PPP:

    def __init__(self, xmin, xmax, problem_number):
        self.xmin = xmin
        self.xmax = xmax
        # initialize chromosome vector randomly  within the search space
        # constrained by the prescribed minimum and maximum bounds:

        d = len(xmin)
        self.x = xmin + (xmax-xmin) * np.random.uniform(0, 1, d)

        #alternative:
        self.x = np.zeros(d)
        for i in range(d):
            self.x[i] = np.random.uniform(xmin[i], xmax[i])
        
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
            self.max_price_m1 = 0.45
            self.max_price_m2 = 0.25
            self.max_price_m3 = 0.2
            #maximum demand for each market == d in slides
            self.max_demand_m1 = 2000000
            self.max_demand_m2 = 30000000
            self.max_demand_m3 = 20000000
            #price at which energy isn to buy if more sold then produced
            self.cost_price = 0.6
        
        if (problem_number == 2):
            #maximum number of Plants for each type of plant == m in slides
            self.max_number_p1 = 100
            self.max_number_p2 = 50
            self.max_number_p3 = 3
            #maximum price for each market == p in slides 
            self.max_price_m1 = 0.45
            self.max_price_m2 = 0.25
            self.max_price_m3 = 0.2
            #maximum demand for each market == d in slides
            self.max_demand_m1 = 2000000
            self.max_demand_m2 = 30000000
            self.max_demand_m3 = 20000000
            #price at which energy isn to buy if more sold then produced
            self.cost_price = 0.1
            
        if (problem_number == 3):
            #maximum number of Plants for each type of plant == m in slides
            self.max_number_p1 = 100
            self.max_number_p2 = 50
            self.max_number_p3 = 3
            #maximum price for each market == p in slides
            self.max_price_m1 = 0.5
            self.max_price_m2 = 0.3
            self.max_price_m3 = 0.1
            #maximum demand for each market == d in slides
            self.max_demand_m1 = 1000000
            self.max_demand_m2 = 5000000
            self.max_demand_m3 = 5000000
            #price at which energy isn to buy if more sold then produced
            self.cost_price = 0.6
            
    def purchasing_cost(energy):
        return energy*self.cost_price

    def production_cost(self):
        #if nothing is requested, return 0
        if(energy <= 0):
            return 0;
        
        #if more energy is requested then can be generated, return very large value
        if(energy > kwhPerPlant*maxPlants):
            large = 10000000000000
            return large
        
        #determine number of plants needed to generate requested energy
        plantsNeeded = math.ceil(x / kwhPerPlant)
        
        return plantsNeeded*costPerPlant        

    def cost(self):
        pass

    def demand(price, maxPrice, maxDemand):
        #if price is greater then max price, return 0
        if(price > maxPrice):
            return 0
        
        #if product is free return max demand(ignore negative prices)
        if(price <= 0):
            return maxDemand
        
        

    def revenue(self):
        pass

    def profit(self):
        pass
