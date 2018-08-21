#Tournament selector
class Selector_Tournament():

    def do(self,population,pool_size): #car array as population

        opponent_amount=2 #more than two "opponents" for the tournament possible

        fitnesses=calc_fitnesses(population) #not ideal, because maybe not every
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

    def summarize(population,demandarray):
        sumpop=list()

        for chromosome in population: #can demandarray be bigger than cararray?? #<> #similar numbers of demandarray always next to each other, right?
            for index in range(len(chromosome)):
                if (index<len(demandarray)):
                    customer=demandarray[index]
                    car=chromosome[index]
                    sumchrom=list()
                    

#calculates fitnesses for whole population
def calc_fitnesses(population):
    fitnesses=list()
    for chromosome in population:
       fitnesses.append(fitness(chromosome))
    return fitnesses
