# coding: utf-8

from ACO_Initializer import Initializer
from ACO_Taskinitializer import Taskinitializer
from ACO_SolutionGenerator import SolutionGenerator
from ACO_Evaporator import Evaporator
from ACO_Intensificator import Intensificator

#Tournament selector
class Selector_Tournament():

    def do(self,population,pool_size): #car array as population

        opponent_amount=2 #more than two "opponents" for the tournament possible

        fitnesses=calc_fitnesses(car_assignments) #not ideal, because maybe not every
                                            #fitness is interesting, but probably better than calcuting one fitness
                                            #multiple times
        
        selected=list()
        for i in range(pool_size):
            opponents=list()
            opponent_fitnesses=list()
            
            for i2 in range(opponent_amount):

                rnd=random.randint(0,len(population)-1)
                while (rnd in opponents): #in: probably poor performance #where did the do while loop go...
                    rnd=random.randint(0,len(population)-1)

                opponents.append(rnd)
                opponent_fitnesses.append(fitnesses[rnd])

            selected.append(population[opponents[opponent_fitnesses.index(max(opponent_fitnesses))]])

        return selected

def summarize(cararray,demandarray): #or are demandarrays included in population?
    sumpop=list()

    #can demandarray be bigger than cararray?? #<> #similar numbers of demandarray just as cars are always next to each other, right?
    customer=0
    car=cararray[0]
    sumchrom=list()

    for index in range(len(cararray)):
        if (index<len(demandarray)):


            if (cararray[index]!=car):
                sumpop.append(sumchrom)
                sumchrom=list()
                customer=0
                car=cararray[index]

            if (demandarray[index]!=customer and demandarray[index]!=0):
                sumchrom.append(demandarray[index])
                customer=demandarray[index]

        else:
            if len(sumchrom)>0:
                sumpop.append(sumchrom)
            break

    return sumpop   #Reihenfolge/damit Kosten der cars?
                    
#calculates fitnesses for whole population
def calc_fitnesses(population):

    taskinitializer = Taskinitializer(1) #replace
    initializer = Initializer()
    solutiongenerator = SolutionGenerator(alpha=1, beta=1, num_of_ants=20)
    evaporator = Evaporator(rho=0.1)
    intensificator = Intensificator(delta=0.5)

    fitnesses=list()
    for chromosome in population:
        #summarize()
        antco = ACO(taskinitializer, initializer, solutiongenerator, evaporator, intensificator, 30, printing=False)
        best_solutions,solutions,scores = antco.run()
        fitnesses.append(best_solutions[len(best_solutions)-1])

    return fitnesses

print(len(list()))
print(summarize([1,1,1,5,5,3,3,3,3,3,2],[2,0,0,3,3,3,1,1]))
