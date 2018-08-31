# coding: utf-8

from ACO_Initializer import Initializer
from ACO_Taskinitializer import Taskinitializer
from ACO_SolutionGenerator import SolutionGenerator
from ACO_Evaporator import Evaporator
from ACO_Intensificator import Intensificator

#still need to implement the 0-adding/removing

#Tournament selector
class Selector_Tournament():

    def do(self, population, pool_size): #population = [[car_slots],[demand_slots]] # imagineable as 3D-Array

        opponent_amount=2 #more than two "opponents" for the tournament possible

        fitnesses=calc_fitnesses(population) #not ideal, because maybe not every fitness is interesting, but probably better than calcuting one fitness multiple times
        
        winners=list() #new population
        winners.append(list()) #car_slots
        winners.append(list()) #demand_slots

        #Do as many tournaments as the new population's amount of individuals should be
        for tournament in range(pool_size):
            opponents=list()
            opponent_fitnesses=list()
            
            #Select opponents for tournament randomly
            for opponent_number in range(opponent_amount):

                #where did the do while loop go...
                rnd=random.randint(0,len(population[0])-1)
                while (rnd in opponents): #in: probably poor performance 
                    rnd=random.randint(0,len(population[0])-1)

                opponents.append(rnd)
                opponent_fitnesses.append(fitnesses[rnd])

            winners[0].append(population[0][opponents[opponent_fitnesses.index(max(opponent_fitnesses))]])
            winners[1].append(population[1][opponents[opponent_fitnesses.index(max(opponent_fitnesses))]])

        return winners


#takes one chromosome
#returns a list of customers for each car, so cuts out demands, indices of said list are number of car (what about car 0, we start with 1, right??) / i think car 0 would be more intuitive since we will have the cars in an array

#similar numbers of demandarray just as cars are always next to each other, right??
    #otherwise, this method won't work, but has more performance this way

#can demandarray be bigger than cararray?? / no that has to be avoided

def summarize(chromosome, car_amount):
   
    assignments=[None] * (car_amount+1) #one entry for each car that has to drive + we don't use the 0

    #<> sorry, just need these because of my keyboard

    customer=0
    car=chromosome[0][0]
    customers=list() #temporary list of customers for a car to visit

    #loop through every car-slot
    for index in range(len(chromosome[0])):
        if (index<len(chromosome[1])):

            if (chromosome[0][index]!=car):
                assignments[car]=(customers)
                customers=list()
                customer=0
                car=chromosome[0][index]

            if (chromosome[1][index]!=customer and chromosome[1][index]!=0):
                customers.append(chromosome[1][index])
                customer=chromosome[1][index]

        else:
            if len(customers)>0:
                assignments[car]=(customers)
            break

    return assignments
                    
#calculates fitnesses for whole population
#fitness values come from ACO
def calc_fitnesses(population):

    #Modules for ACO
    taskinitializer = Taskinitializer(1) #replace
    initializer = Initializer()
    solutiongenerator = SolutionGenerator(alpha=1, beta=1, num_of_ants=20)
    evaporator = Evaporator(rho=0.1)
    intensificator = Intensificator(delta=0.5)

    fitnesses=list()
    for chromosome in population:
        car_assignments=summarize(chromosome) #ACO doesn't need exact demand, just which car visits which customer
        antco = ACO(taskinitializer, initializer, solutiongenerator, evaporator, intensificator, 30, printing=False)
        best_solutions,solutions,scores = antco.run()
        fitnesses.append(best_solutions[len(best_solutions)-1])

    return fitnesses

print(len(list()))
print(summarize([[1,1,1,5,5,3,3,3,3,3,2],[2,0,0,3,3,3,1,1]],5))
