import random
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy



class Simple_Mutator:
    
    def __init__(self,mutate_probability=0.1):
        self.mutate_probability = mutate_probability
        
    def mutate(self,offspring):
        
        for o in offspring:
            capacities= o['vehicle_capacities']
            
            if np.random.uniform(0,1) < self.mutate_probability:
                
                cr_point1 = np.random.choice(range(len(capacities)-1))
                cr_point2 = np.random.choice(range(len(capacities)-cr_point1-1))+cr_point1+1
                temp=capacities[cr_point1]
                capacities[cr_point1]=capacities[cr_point2]
                capacities[cr_point2]=temp
        return offspring


class Mutator:
    
    def __init__(self,capacities_list, mutate_probability=1, select_as_swap_start_prob=0.8, select_as_swap_end_prob=0.9):
        self.mutate_probability = mutate_probability
        self.select_as_swap_start_prob = select_as_swap_start_prob
        self.select_as_swap_end_prob = select_as_swap_end_prob
        self.capacities_list = capacities_list
        
    
    #im not sure if i can explain the generell idea well enough in comments. It might be the most informative thing if i make a handwritten / drawen explanation (Mutator/Recombiner Rules Nr2 in clean)
    def mutate(self,offspring):
                
        #mutated_offspring = []
        for individual in offspring:
            if np.random.uniform() < self.mutate_probability:
                swapping = 0
                swapped = 0
                swap_start = 0
                swap_end = 0
                vehicles_toswap = []
                vehicle_capacities = individual['vehicle_capacities']
                for i in range(int(len(vehicle_capacities)/2)):
                    if swapping == 1:
                        vehicles_toswap.append(vehicle_capacities[i])
                        if not vehicle_capacities[i] == vehicle_capacities[i+1]:
                            if np.random.uniform() < self.select_as_swap_end_prob:
                                swap_end = i+1
                                swapped = 1
                                break
                    
                    if swapping == 0:
                        if not vehicle_capacities[i] == vehicle_capacities[i+1]:
                            if np.random.uniform() < self.select_as_swap_start_prob:
                                swapping = 1
                                swap_start = i+1
                if swapped == 1:
                    #print("swap_start: ", swap_start, "swap_end: ", swap_end, "vehicles_toswap: ",vehicles_toswap)
                    swapping = 0
                    swapped_2 = 0
                    swap_end_2 = 0
                    swap_start_2 = 0
                    vehicles_toswap_2 = []
                    for i in range(int(len(vehicle_capacities)/2)):
                        if i == 0:
                            i += 1
                        if swapping == 1:
                            vehicles_toswap_2.append(vehicle_capacities[len(vehicle_capacities)-i])
                            if not vehicle_capacities[len(vehicle_capacities)-i] == vehicle_capacities[len(vehicle_capacities)-i-1]:
                                if len(vehicles_toswap) == len(vehicles_toswap_2) :
                                    if not vehicle_capacities[len(vehicle_capacities)-i] == vehicle_capacities[len(vehicle_capacities)-i-1]:
                                        swap_end_2 = len(vehicle_capacities)-i
                                        swapped_2 = 1
                                        break
                                if len(vehicles_toswap) < len(vehicles_toswap_2) :
                                    break
                        if swapping == 0:
                            if not vehicle_capacities[len(vehicle_capacities)-i] == vehicle_capacities[len(vehicle_capacities)-i-1]:
                                if np.random.uniform() < self.select_as_swap_start_prob:
                                    swapping = 1
                                    swap_start_2 = len(vehicle_capacities)-i
                    if swapped_2 == 1:
                        #print("swap_start_2: ", swap_start_2, "swap_end_2: ", swap_end_2, "vehicles_toswap_2: ",vehicles_toswap_2)
                        vehicle_capacities[swap_start:swap_end] = vehicles_toswap_2
                        vehicle_capacities[swap_end_2:swap_start_2] = vehicles_toswap
                        #new_individual = individual.copy()
                        #new_individual['vehicle_capacities'] = vehicle_capacities
                        #mutated_offspring.append(new_individual)
                        #print("vehicle_capacities:", vehicle_capacities)
                        individual['vehicle_capacities'] = vehicle_capacities

        return offspring