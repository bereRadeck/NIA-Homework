import random
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

"""
class Simple_Mutator:
    
    def __init__(self,mutate_probability=0.1):
        self.mutate_probability = mutate_probability
        
    def mutate(self,offspring):
        
        for o in offspring:
            capacities= o['vehicle_capacities']
            
            if rnd.uniform(0,1) < self.mutate_probability:
                
                cr_point1 = rnd.choice(range(len(capacities)-1))
                cr_point2 = rnd.choice(range(len(capacities)-cr_point1-1))+cr_point1+1
                temp=capacities[cr_point1]
                capacities[cr_point1]=capacities[cr_point2]
                capacities[cr_point2]=temp
        return offspring

"""
class Mutator:
    
    def __init__(self,mutate_probability=0.1,capacities_list):
        self.mutate_probability = mutate_probability
        self.capacities_list = capacities_list
    
    #im not sure if i can explain the generell idea well enough in comments. It might be the most informative thing if i make a handwritten / drawen explanation (Mutator/Recombiner Rules Nr2 in clean)
    def mutate(self,offspring):
        
        mutate_probability = self.mutate_probability
        
        for individual in offspring:
            
            vehicle_capacities = individual['vehicle_capacities']
            customer_demands = individual['customer_demands']
            capacities_list = self.capacities_list
        
        
            big_small = np.zeros((len(capacities_list)), dtype=int)   #safes information if a car was the small or big member of a swap
            zeros_array = np.zeros((len(capacities_list)), dtype=int) #used to keep track how many zeros have to be added/substracted from customer_demands when swapping a car

            vehicle_capacities_unique_cars = []                               #contains every car exactly once, retaining their order
            vehicle_capacities_unique_cars.append(vehicle_capacities[0])
            vehicle_capacities_unique_cars_pointer = 0
            for i in range(len(vehicle_capacities)):
                if vehicle_capacities[i] != vehicle_capacities_unique_cars[vehicle_capacities_unique_cars_pointer]:
                    vehicle_capacities_unique_cars.append(vehicle_capacities[i])
                    vehicle_capacities_unique_cars_pointer += 1

            for first_car_pointer in range(len(vehicle_capacities_unique_cars)): #swaps every car with a mutation probability with another car in the vehicle_capacities_unique_cars array and keeps important information
                    if np.random.uniform() < mutate_probability:
                        zeros_counter = 0
                        first_car = deepcopy(vehicle_capacities_unique_cars[first_car_pointer])
                        second_car_pointer = random.randint(0,len(vehicle_capacities_unique_cars)-1)  #randomly selects a car to swap the current car with
                        second_car = deepcopy(vehicle_capacities_unique_cars[second_car_pointer])

                        if not first_car == second_car:

                            car_length_difference = np.absolute(capacities_list[first_car]-capacities_list[second_car]) #safes which of the two selected cars is bigger

                            big = second_car
                            small = first_car

                            if capacities_list[first_car] > capacities_list[second_car]:
                                big = first_car
                                small = second_car

                            if car_length_difference != 0:          #checks if cars are allowed to be swapped according to size and zeros
                                for j in range(len(vehicle_capacities)):
                                    if (customer_demands[j] == 0) & (vehicle_capacities[j] == big):
                                        zeros_counter +=1

                            if zeros_counter >= car_length_difference & car_length_difference > 0: 
                                if big_small[small]+big_small[big] == 0: #checks if one of the selected cars has been swapped already

                                    vehicle_capacities_unique_cars[first_car_pointer] = deepcopy(second_car)  #swaps selected cars positions
                                    vehicle_capacities_unique_cars[second_car_pointer] = deepcopy(first_car)

                                    big_small[small] = 1                                # if a car has: a 0 = not swapped / a 1 = was small member of a swap / a 2 = was big
                                    big_small[big] = 2

                                    zeros_array[small] = car_length_difference          
                                    zeros_array[big] = car_length_difference

                                    #print("big: ",big," small: ",small)

            vehicle_capacities_new = []
            customer_demands_new = []
            customer_demands_pointer = 0
            block = 0

            #print("big_small  ",big_small)
            vehicle_capacities_pointer = 0

            for vehicle_capacities_pointer in range(len(vehicle_capacities)): #create new customer_demands array from old vehicle_capacities while cutting out / inserting zeros

                if big_small[vehicle_capacities[vehicle_capacities_pointer]] == 1 & zeros_array[vehicle_capacities[vehicle_capacities_pointer]] > 0: #if it was the smaller car in a trade and zeros_array didnt reach 0 yet => insert 0 
                    customer_demands_new.append(0)
                    zeros_array[vehicle_capacities[vehicle_capacities_pointer]] -= 1

                elif big_small[vehicle_capacities[vehicle_capacities_pointer]] == 2: #if it was the big partner => reduce zeros by not copying them into new demand
                    if customer_demands[vehicle_capacities_pointer] == 0:
                        zeros_array[vehicle_capacities[vehicle_capacities_pointer]] -= 1
                        vehicle_capacities_pointer += 1
                        block = 1

                if block == 0:                                #if 0 was skipped, skip customer_demands copy
                    customer_demands_new.append(customer_demands[vehicle_capacities_pointer])

                block = 0


            vehicle_capacities_unique_cars_pointer = 0

            for vehicle_capacities_unique_cars_pointer in range(len(vehicle_capacities_unique_cars)): #create new vehicle_capacities from swapped c_single

                for j in range(capacities_list[vehicle_capacities_unique_cars[vehicle_capacities_unique_cars_pointer]]):
                    vehicle_capacities_new.append(vehicle_capacities_unique_cars[vehicle_capacities_unique_cars_pointer])              

            #if cars with only zeros as customer_demands get involved in a swap we can lose 0`s at the end of the customer_demands array. seems to be no harm if we just fill the array up again
            delta_customer_demands = len(customer_demands)-len(customer_demands_new)

            for j in range(delta_customer_demands):
                customer_demands_new.append(0)        

            individual['vehicle_capacities'] = vehicle_capacities_new
            individual['customer_demands'] = customer_demands_new

        return offspring
