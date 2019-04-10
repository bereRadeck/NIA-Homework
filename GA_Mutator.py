import random
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

class Mutator:
    
    def __init__(self,chance=0.1):
        self.chance = chance
        print("Warning! Mutation probability still needs to be implemented for old Mutator")
    #im not sure if i can explain the generell idea well enough in comments. It might be the most informative thing if i make a handwritten / drawen explanation (Mutator/Recombiner Rules Nr2 in clean)
    def do(Population,Mutation_probability):
        
        for i in Population:
            
            c_multi = i['vehicle_capacities']
            demand = i['customer_demands']
            c_amount = i['capacities_list']
        
        
            big_small = np.zeros((len(c_amount)), dtype=int)   #safes information if a car was the small or big member of a swap
            zeros_array = np.zeros((len(c_amount)), dtype=int) #used to keep track how many zeros have to be added/substracted from demand when swapping a car

            c_single = []                               #contains every car exactly once, retaining their order
            c_single.append(c_multi[0])
            c_single_pointer = 0
            for i in range(len(c_multi)):
                if c_multi[i] != c_single[c_single_pointer]:
                    c_single.append(c_multi[i])
                    c_single_pointer += 1

            for first_car_pointer in range(len(c_single)): #swaps every car with a mutation probability with another car in the c_single array and keeps important information
                    if np.random.uniform() < Mutation_probability:
                        zeros_counter = 0
                        first_car = deepcopy(c_single[first_car_pointer])
                        second_car_pointer = random.randint(0,len(c_single)-1)  #randomly selects a car to swap the current car with
                        second_car = deepcopy(c_single[second_car_pointer])

                        if not first_car == second_car:

                            car_length_difference = np.absolute(c_amount[first_car]-c_amount[second_car]) #safes which of the two selected cars is bigger

                            #no need to swap same sized cars, right?
                            #if car_length_difference == 0:
                             #   c_single[first_car_pointer] = deepcopy(second_car)  #swaps selected cars positions
                              #  c_single[second_car_pointer] = deepcopy(first_car)
    #
     #                           print("1 / first car: ",c_single[first_car_pointer]," second car: ",c_single[second_car_pointer])
    #
    #
     #                       else:

                            big = second_car
                            small = first_car

                            if c_amount[first_car] > c_amount[second_car]:
                                big = first_car
                                small = second_car

                            if car_length_difference != 0:          #checks if cars are allowed to be swapped according to size and zeros
                                for j in range(len(c_multi)):
                                    if (demand[j] == 0) & (c_multi[j] == big):
                                        zeros_counter +=1

                            if zeros_counter >= car_length_difference & car_length_difference > 0: 
                                if big_small[small]+big_small[big] == 0: #checks if one of the selected cars has been swapped already

                                    c_single[first_car_pointer] = deepcopy(second_car)  #swaps selected cars positions
                                    c_single[second_car_pointer] = deepcopy(first_car)

                                    big_small[small] = 1                                # if a car has: a 0 = not swapped / a 1 = was small member of a swap / a 2 = was big
                                    big_small[big] = 2

                                    zeros_array[small] = car_length_difference          
                                    zeros_array[big] = car_length_difference

                                    #print("big: ",big," small: ",small)

            c_multi_new = []
            demand_new = []
            demand_pointer = 0
            block = 0

            #print("big_small  ",big_small)
            c_multi_pointer = 0

            for c_multi_pointer in range(len(c_multi)): #create new demand array from old c_multi while cutting out / inserting zeros

                if big_small[c_multi[c_multi_pointer]] == 1 & zeros_array[c_multi[c_multi_pointer]] > 0: #if it was the smaller car in a trade and zeros_array didnt reach 0 yet => insert 0 
                    demand_new.append(0)
                    zeros_array[c_multi[c_multi_pointer]] -= 1

                elif big_small[c_multi[c_multi_pointer]] == 2: #if it was the big partner => reduce zeros by not copying them into new demand
                    if demand[c_multi_pointer] == 0:
                        zeros_array[c_multi[c_multi_pointer]] -= 1
                        c_multi_pointer += 1
                        block = 1

                if block == 0:                                #if 0 was skipped, skip demand copy
                    demand_new.append(demand[c_multi_pointer])

                block = 0


            c_single_pointer = 0

            for c_single_pointer in range(len(c_single)): #create new c_multi from swapped c_single

                for j in range(c_amount[c_single[c_single_pointer]]):
                    c_multi_new.append(c_single[c_single_pointer])              

            #if cars with only zeros as demand get involved in a swap we can lose 0`s at the end of the demand array. seems to be no harm if we just fill the array up again
            delta_demand = len(demand)-len(demand_new)

            for j in range(delta_demand):
                demand_new.append(0)        

            #print("demand:      ",demand)
            #print("c_multi:     ",c_multi)
            #print("demand_new:  ",demand_new)
            #print("c_multi_new: ",c_multi_new)
            
            i['vehicle_capacities'] = c_multi_new
            i['customer_demands'] = demand_new
        return population


class Simple_Mutator:
    
    def __init__(self,chance=0.1):
        self.chance = chance
        
    def mutate(self,pool):
        
        for p in pool:
            capacities= p['vehicle_capacities']
            
            if rnd.uniform() < self.chance:
                
                cr_point1=rnd.choice(range(len(capacities)-1))
                cr_point2=rnd.choice(range(len(capacities)-cr_point1-1))+cr_point1+1
                temp=capacities[cr_point1]
                capacities[cr_point1]=capacities[cr_point2]
                capacities[cr_point2]=temp
                