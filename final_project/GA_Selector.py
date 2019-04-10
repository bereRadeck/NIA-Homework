# coding: utf-8

import ACO_Main as aco
import random
import numpy as np

#Tournament selector
# big fitness value is worse, because it means high transportation cost

class Roulette_Selector:

    def __init__(self,offspring_size):
        self.offspring_size = offspring_size

    def select(self,pop):

        parents = []

        for _ in range(self.offspring_size):
            fitnesses = np.array([individual['fitness'] for individual in pop])

            probabilities = [((x/ fitnesses.sum())) for x in fitnesses]
            parent1, parent2 = np.random.choice(pop,size=2,replace=False, p=probabilities)
            parents.append((parent1,parent2))

        return parents

class Tournament_Selector:

    def __init__(self,offspring_size,opponent_number=2):
        self.offspring_size = offspring_size
        self.opponent_number = opponent_number

    def select(self,pop):
        parents = []
        for _ in range(self.offspring_size):

            opponents1 =  np.random.choice(a=range(len(pop)),size=self.opponent_number,replace=False)
            parent1 = min(opponents1, key= lambda x: x['fitness'])

            opponents2 =  np.random.choice(a=range(len(pop)),size=self.opponent_number,replace=False)
            parent2 = min(opponents2, key= lambda x: x['fitness'])

            parents.append((parent1,parent2))

        return parents




"""

class Selector_Tournament():

    def __init__(self, trans_cost, dist_matrix, pool_size, ACO):
        self.trans_cost = trans_cost
        self.dist_matrix = dist_matrix
        self.pool_size= pool_size
        self.ACO = ACO

    def do(self, population): #population = [[car_slots],[demand_slots]] # imagineable as 3D-Array

        population = mutate(population)

        opponent_amount=2 #more than two "opponents" for the tournament possible

        fitnesses=calc_fitnesses(population) #not ideal, because maybe not every fitness is interesting, but probably better than calcuting one fitness multiple times
        
        winners=list() #new population
        winners.append(list()) #car_slots
        winners.append(list()) #demand_slots

        #Do as many tournaments as the new population's amount of individuals should be
        for tournament in range(self.pool_size):
            opponents=list()
            opponent_fitnesses=list()
            
            #Select opponents for tournament randomly
            for opponent_number in range(opponent_amount):

                #where did the do while loop go...
                rnd=random.randint(0,len(population)-1)
                while (rnd in opponents): #in: probably poor performance 
                    rnd=random.randint(0,len(population)-1)

                opponents.append(rnd)
                opponent_fitnesses.append(fitnesses[rnd])

            winners.append(population[opponents[opponent_fitnesses.index(min(opponent_fitnesses))]])

        return winners

# todo: maybe make following functions as part of class
# todo :this was meant to enable solutions with even and uneven numbers of 0, but we initialize even and uneven arrays anyway so i think we can skip this part completly ~Till 
# todo: add or take 0's from demandarray, we should maybe move it to mutator module, since it's a mutation
def mutate(population, add_probability=0.1,take_probability=0.1):
    #chromosome index
    for chromosomeindex in range(len(population)):

        #for each 0 in demandarray: remove it with take_probability
        slotindex=0
        while (slotindex in range(len(population[chromosomeindex]['customer_demands']))):
            if (population[chromosomeindex]['customer_demands'][slotindex]==0):
                if (random.random()<take_probability):
                    del(population[chromosomeindex]['customer_demands'][slotindex])
                    slotindex=slotindex-1
            slotindex=slotindex+1

        #go through demandarray starting with 2. element
        #add a 0 with add_probability after each demandblock (so when number changes between two demandslots)
        # todo: we need to make sure somewhere that demandarray doesn't get bigger than cararray
        slotindex=1
        while (slotindex in range(1,len(population[chromosomeindex]['customer_demands']))):
            if (population[chromosomeindex]['customer_demands'][slotindex]!=population[chromosomeindex]['customer_demands'][slotindex-1]):
                if (random.random()<add_probability):
                    population[chromosomeindex]['customer_demands'].insert(slotindex,0)
                    slotindex=slotindex+1
            slotindex=slotindex+1
                   
    return population 


#takes one chromosome
#returns a list of customers for each car, so cuts out demands, indices of said list are number of car

#similar numbers of demandarray just as cars are always next to each other
    #otherwise, this method won't work, but has more performance this way

def summarize(chromosome, car_amount):
   
    assignments=[ [] for i in range(car_amount)] #one entry for each car that has to drive

    #<> sorry, just need these because of my keyboard

    #loop through every car-slot
    for index in range(len(chromosome['vehicle_capacities'])):
        if (len(chromosome['customer_demands'])<=index):
            break
        if (chromosome['customer_demands'][index] not in assignments[chromosome['vehicle_capacities'][index]]):
            assignments[chromosome['vehicle_capacities'][index]].append(chromosome['customer_demands'][index])

    return assignments
                    
#calculates fitnesses for whole population
#fitness values come from ACO
def calc_fitnesses(population):

    fitnesses=list()
    for chromosome in population:
        cars_assignments=summarize(chromosome) #ACO doesn't need exact demand, just which car visits which customer
        fitness = 0
        for car_index, car_assignment in enumerate(cars_assignments):
            #todo: simplify, if only one customer
            if len(car_assignment)>0:
                #todo: double check if index starts with 0 or 1
                score, solution = self.ACO.run_default(self.dist_matrix, car_assignment)
                fitness = fitness + self.trans_cost[car_index] * score
            #include
        fitnesses.append(fitness)

    return fitnesses

# todo: first customer 1 or 0

#print(mutate([[[1,1,1,5,5,3,3,3,3,3,2]],[[2,0,0,3,3,3,1,1]]],1,1))
#dic = {"vehicle_capacities": [1,1,1,5,5,3,3,3,3,3,2], 'customer_demands': [2,0,0,3,3,3,1,1] }
#print(summarize(dic,6))

dis_mat=[[0,3,4,7],[3,0,1,4],[4,1,0,2],[7,4,2,0]]

print("Testing ACO, wtf are customers visited multiple times?")
score, solution = self.ACO.run_default(dis_mat, [0,1,2,3])
print(score, solution)"""


