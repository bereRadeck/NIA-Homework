import numpy as np
import random as rnd
import copy 

class Recombiner:
    def __init__(self, recomb_chance=0.1):
        self.recomb_chance=recomb_chance
       
    

class Ordered_Recombiner:
    def __init__(self, combine_probability, swap_prob):

        self.combine_probability = combine_probability
        self.swap_prob = swap_prob

    def recombine(Population, combine_probability, swap_prob):


        for i in Population:
        
            if np.random.uniform() < combine_probability:
                k = "false"
                while not i == k: 
                    k = random.randint(0,len(Population)-1)
                j = Population[k]
                
                car_a = i['vehicle_capacities']
                car_b = j['vehicle_capacities']
                demand_a = i['customer_demands']
                demand_b = j['customer_demands']
                car_a_amount = i['capacities_list']                
                car_a_swap = [] #array that keeps the cars of array car_a which are possible members of a swap
                car_b_swap = []
                zeros_counter = 0 
                swapping = 0 #used to tell the array loop it should start shifting cars into the swap arrays until stop is hit
                swap_end_prob = 0.7
                broke = 0 #if the selected part of the array hits the end of the car array we dont need to add cars from the garage

                for i in range(len(car_a)-1):

                    #if swapping mode is enabled =>
                    if swapping == 1:
                        #if demand_a[i] == 0:
                         #   zeros_counter += 1
                        if i < len(car_b):

                            if not car_b[i] == car_b[i+1]: #copy each individual car inside the swapping-part of car_a into the swap array
                                car_b_swap.append(car_b[i])
                                car_a[i].delete
                            elif i == len(car_b)-2:        #if i=end of array => append last car
                                car_b_swap.append(car_b[i])
                                car_a[i].delete

                            if not car_a[i] == car_a[i+1]: #copy each individual car inside the swapping-part of car_a into the swap array
                                car_a_swap.append(car_a[i])
                                                                
                                if np.random.uniform() < swap_end_prob: #if end-probability is hit and the car in car_b ends within a reasonable
                                    if not car_b[i] == car_b[i+1]:      #range of car a`s end (in this case 3 units) we stop swapping                                                                #if b is longer then a we might need to correct for that by adding zeros
                                        print("end swapping")
                                        broke = 1
                                        swap_end = i
                                        car_a[i].delete
                                        break
                                    elif i < len(car_b)-2:
                                        if not car_b[i+1] == car_b[i+2]:
                                            print("end swapping")
                                            #zeros_counter = 1
                                            broke = 1
                                            swap_end = i
                                            car_a[i].delete
                                            break
                                    #elif not car_b[i] == car_b[i-zeros_counter]:
                                     #   i = len(car_a)
                                    elif i < len(car_b)-3:
                                        if not car_b[i+2] == car_b[i+3]:
                                            print("end swapping")
                                            #zeros_counter = 2
                                            broke = 1
                                            swap_end = i
                                            car_a[i].delete
                                            break
                                    car_a[i].delete
                                    #if we didnt select a start of our swapping-part yet =>
                    if swapping == 0:    
                        if not car_a[i] == car_a[i+1]: #and if we are at a point where a new car starts for a and b =>
                            if not car_b[i] == car_b[i+1]:
                                if np.random.uniform() < swap_prob: #and if set probability is hit => start swapping mode
                                    swapping = 1
                                    print("start swapping")
                                    swap_start = i

                if broke == 1: #if we did end the swapping-part before the end of the array => add cars from garage to car_a_swap array
                    for j in range(len(car_a)-1): #start at the end of the car_a array
                        if not demand_a[len(car_a)-1-j] == 0: #if our demand is not 0 => end of garage => stop copying cars to car_a_swap
                            car_a[len(car_a)-j].delete
                            break                    
                        elif not car_a[len(car_a)-1-j] == car_a[len(car_a)-1-(j+1)]: #copy each individual car from garage to the car_a_swap array
                            car_a_swap.append(car_a[len(car_a)-1-j])
                        car_a[len(car_a)-j].delete
                #next step would be: check if car_b_swap in car_a_swap
                # if true => append car_a_swap - car_b_swap to car_b_swap
                # perform resulting swaps in c_single_array
                print("car_a_swap: ", car_a_swap)
                print("car_b_swap: ", car_b_swap)
                
                if car_b_swap in car_a_swap:
                    
                    car_b_swap_multi = []
                    for i, car in enumerate(car_b_swap):
                        for c in range(car_a_amount[i]):
                            car_b_swap_multi.append(car)              
                    
                    while len(car_b_swap_multi) < (swap_end-swap_start):
                        car_b_swap_multi.append(0)
                            
                    np.insert(car_a, swap_start, car_b_swap_multi)
                    
                    car_a_swap_multi = []
                    for i, car in enumerate(car_a_swap-car_b_swap):
                        for c in range(car_a_amount[i]):
                            car_a_swap_multi.append(car)
                            
                    car_a.append(car_a_swap_multi)
                                            
                    

            i['vehicle_capacities'] = car_a
        
        return Population