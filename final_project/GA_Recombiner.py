import numpy as np
import random as rnd
import copy

class Simple_Recombiner:

    def __init__(self):
       # self.combine_probability = combine_probability

    def recombine(self, parents):

        for p in parents:

            
            new1 = copy.deepcopy(p[0])
            new2 = copy.deepcopy(p[1])
            
            capacities1 = new1['vehicle_capacities']
            capacities2 = new2['vehicle_capacities']

            
            cr_point1 = rnd.choice(range(len(capacities1) - 1))
            cr_point2 = rnd.choice(range(len(capacities1) - cr_point1)) + cr_point1 + 1
            print(cr_point1,cr_point2)
            slice1 = capacities2[cr_point1:cr_point2]
            print(len(slice1))    
            for s in slice1:
                    
                del capacities1[capacities1.index(s)]
            for s in slice1:
                capacities1.insert(cr_point1, s)

            return new1


class Ordered_Recombiner:
    def __init__(self, select_as_swap_start_prob=0.3, select_as_swap_end_prob=0.5):

        self.select_as_swap_start_prob = select_as_swap_start_prob
        self.select_as_swap_end_prob = select_as_swap_end_prob

    def recombine(parents):

        offspring = []
        
        for parent_pair in parents:

            vehicle_capacities_a = parent_pair[0]['vehicle_capacities']
            vehicle_capacities_b = parent_pair[1]['vehicle_capacities']
            customer_demands_a = parent_pair[0]['customer_demands']
            vehicle_capacities_b_amount = parent_pair[1]['capacities_list']                
            vehicle_capacities_a_swap = [] #array that keeps the cars of array car_a which are possible members of a swap
            vehicle_capacities_b_swap = []
            swapping = 0 #used to tell the array loop it should start shifting cars into the swap arrays until stop is hit
            broke = 0 #if the selected part of the array hits the end of the car array we dont need to add cars from the garage

            for i in range(len(vehicle_capacities_a)-1):

                #if we didnt select a start of our swapping-part yet =>
                if swapping == 0:    
                    if not vehicle_capacities_a[i] == vehicle_capacities_a[i+1]: #and if we are at a point where a new car starts for a and b =>
                        if not vehicle_capacities_b[i] == vehicle_capacities_b[i+1]:
                            if np.random.uniform() < self.select_as_swap_start_prob: #and if set probability is hit => start swapping mode
                                swapping = 1
                                i += 1
                                #print("start swapping at ", i)
                                swap_start = i
                
                #if swapping mode is enabled =>
                if swapping == 1:
                    if i < len(vehicle_capacities_b):

                        if not vehicle_capacities_b[i] ==vehicle_capacities_b[i+1]: #copy each individual car inside the swapping-part of car_a into the swap array
                            vehicle_capacities_b_swap.append(vehicle_capacities_b[i])
                        elif i == len(vehicle_capacities_b)-2:        #if i=end of array => append last car
                            vehicle_capacities_b_swap.append(vehicle_capacities_b[i])

                        if not vehicle_capacities_a[i] == vehicle_capacities_a[i+1]: #copy each individual car inside the swapping-part of car_a into the swap array
                            vehicle_capacities_a_swap.append(vehicle_capacities_a[i])
                            if np.random.uniform() < self.select_as_swap_end_prob: #if end-probability is hit and the car in car_b ends within a reasonable
                                if not vehicle_capacities_b[i] == vehicle_capacities_b[i+1]:      #range of car a`s end (in this case 3 units) we stop swapping                                                                #if b is longer then a we might need to correct for that by adding zeros
                                    #print("end swapping at ",i)
                                    broke = 1
                                    swap_end = i
                                    break

            if broke == 1: #if we did end the swapping-part before the end of the array => add cars from garage to car_a_swap array
                #print("vehicle_capacities_a: ",vehicle_capacities_a)
                for j in range(len(vehicle_capacities_a)): #start at the end of the vehicle_capacities_a array
                    if not customer_demands_a[len(vehicle_capacities_a)-1-j] == 0: #if our demand is not 0 => end of garage => stop copying cars to vehicle_capacities_a_swap
                        break                    
                    elif not vehicle_capacities_a[len(vehicle_capacities_a)-1-j] == vehicle_capacities_a[len(vehicle_capacities_a)-1-(j+1)]: #copy each individual car from garage to the vehicle_capacities_a_swap array
                        vehicle_capacities_a_swap.append(vehicle_capacities_a[len(vehicle_capacities_a)-1-j])

            #print("vehicle_capacities_a_swap: ", vehicle_capacities_a_swap)
            #print("vehicle_capacities_b_swap: ", vehicle_capacities_b_swap)
            
            #remove every car that is in vehicle_capacities_a_swap from vehicle_capacities_a
            for car in vehicle_capacities_a_swap:
                vehicle_capacities_a = [x for x in vehicle_capacities_a if x != car]
            
            #print("vehicle_capacities_a: ", vehicle_capacities_a)
            
            vehicle_capacities_a_list = []
            vehicle_capacities_b_swap_np = np.array(vehicle_capacities_b_swap)
            vehicle_capacities_a_swap_np = np.array(vehicle_capacities_a_swap)
            if np.in1d(vehicle_capacities_b_swap_np,vehicle_capacities_a_swap_np).all(): #if every member of the parent vehicle_capacities_b is either in the part of vehicle_capacities_a which we exchange or the garage of vehicle_capacities_a we can use the ordered part from vehicle_capacities_b

                vehicle_capacities_b_swap_multi = []
                vehicle_capacities_a_sub_b_swap = []
                for car in vehicle_capacities_b_swap: #unfold flat swap array before adding it to vehicle_capacities_a
                    
                    #################### self.vehicle_capacities_amount
                    
                    for c in range(vehicle_capacities_b_amount[car]):
                        vehicle_capacities_b_swap_multi.append(car)              

                for i, car in  enumerate(vehicle_capacities_b_swap_multi):
                    vehicle_capacities_a.insert(swap_start+i,car)
                #exchange the old part of vehicle_capacities_a with the part from vehicle_capacities_b
                #print("vehicle_capacities_a after insert: ", vehicle_capacities_a)
                
                
                vehicle_capacities_a_sub_b_swap = []
                for car in vehicle_capacities_a_swap:
                    if not car in vehicle_capacities_b_swap:
                        vehicle_capacities_a_sub_b_swap.append(car) #create a list which contains all elements that vehicle_capacities_a is still missing to be complete again

                vehicle_capacities_a_swap_multi = []
                for car in vehicle_capacities_a_sub_b_swap: #unfold them
                    
                    #################### self.vehicle_capacities_amount
                    
                    for c in range(vehicle_capacities_b_amount[car]): 
                        vehicle_capacities_a_swap_multi.append(car)

                vehicle_capacities_a_list = list(vehicle_capacities_a)
                for car in vehicle_capacities_a_swap_multi:
                    vehicle_capacities_a_list.append(car) #add them to vehicle_capacities_a



            parent_pair[0]['vehicle_capacities'] = vehicle_capacities_a_list
            offspring.append(parent_pair[0])
        
        return offspring
