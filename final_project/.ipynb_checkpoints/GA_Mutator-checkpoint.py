import random
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

c_amount = [5,3,4,2,4,1]
demand =  [2,2,2,2,0,1,1,3,3,3,3,4,4,4,0,5,5,5,6]
c_multi = [0,0,0,0,0,1,1,1,2,2,2,2,3,3,4,4,4,4,5]

class Mutator:

    def do(demand,c_amount,c_multi,Mutation_probability):
        
        big_small = np.zeros((len(c)), dtype=int)   #safes information if a car was the small or big member of a swap
        zeros_array = np.zeros((len(c)), dtype=int) #used to keep track how many zeros have to be added/substracted from demand when swapping a car
        
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

                car_length_difference = np.absolute(c_amount[first_car]-c_amount[second_car]) 
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
                    if big_small[small]+big_small[big] == 0: #checks if one of the intended cars has been swapped already
                        
                        c_single[first_car_pointer] = deepcopy(second_car)
                        c_single[second_car_pointer] = deepcopy(first_car)
                        
                        big_small[small] = 1
                        big_small[big] = 2
                       
                        zeros_array[small] = car_length_difference
                        zeros_array[big] = car_length_difference

        c_multi_new = []
        demand_new = []
        demand_pointer = 0
        
        print("big_small  ",big_small)
        
        for c_single_pointer in range(len(c_single)):     #creates new car and demand array
            
            for c_multi_new_pointer in range(c_amount[c_single[c_single_pointer]]):
                
                if (demand_pointer < len(demand)-1): #skips zeros in the demand array so they wont get copied to the new demand of the smaller car
                    if (demand[demand_pointer] == 0) & (zeros_array[c_single[c_single_pointer-1]] > 0):
                        if (big_small[c_single[c_single_pointer-1]] == 1):
                            demand_pointer += 1
                            zeros_array[c_single[c_single_pointer-1]]-=1
                        
                    if (demand[demand_pointer] == 0) & (zeros_array[c_single[c_single_pointer+1]] > 0):
                        if (big_small[c_single[c_single_pointer+1]] == 1):
                            demand_pointer += 1
                            zeros_array[c_single[c_single_pointer+1]]-=1
                    
                    if (demand[demand_pointer] == 0) & (zeros_array[c_single[c_single_pointer]] > 0):
                        if (big_small[c_single[c_single_pointer]] == 1):
                            demand_pointer += 1
                            zeros_array[c_single[c_single_pointer]]-=1
                
                if demand_pointer < len(demand):
                    demand_new.append(demand[demand_pointer])
                demand_pointer += 1
                
                if (big_small[c_single[c_single_pointer]] == 2): #adds zeros to new demand of bigger car
                    if (c_multi_new_pointer == c_amount[c_single[c_single_pointer]]-zeros_array[c_single[c_single_pointer]]-1):
                        for h in range(zeros_array[c_single[c_single_pointer]]):
                            demand_new.append(0)
                            c_multi_new_pointer += 1
                                               
                c_multi_new.append(c_single[c_single_pointer])
        print(demand_new)
        print(c_multi_new)
        return demand_new, c_multi_new
print(Mutator.do(demand,c_amount,c_multi,1))