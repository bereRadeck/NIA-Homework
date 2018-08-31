
# coding: utf-8

# Genetic Algorithm for Nature-Inspired Algorithms for solving Makespan problem
#
# Create an Object of GenAlg and name one module for each required component in constructor
#  (Taskinitializer, Initializer, Selector, Recombiner, Mutator, Replacer)
# once initialized, run do() for GenAlg Object
# Taskinitializer initializes one of the 3 given tasks (defines jobtimes, amount of machines)

import random
import numpy as np
import matplotlib.pyplot as plt

class GenAlg:
    def __init__(self,taskinitializer,initializer,selector,recombiner,mutator,replacer):
        global times,Amount_jobs,Populationsize

        self.taskinitializer=taskinitializer
        self.initializer=initializer
        self.selector=selector
        self.recombiner=recombiner
        self.mutator=mutator
        self.replacer=replacer

    def do(self):
        global Max_Iterations

        generation_fitnesses=list()

        population = self.initializer.do()

        generation_fitnesses.append(max(calc_fitnesses(population)))

        for iteration in range(Max_Iterations):
            pool = self.selector.do(population,int(Populationsize/2))

            offspring = self.recombiner.do(pool)

            offspring = self.mutator.do(offspring)

            population = self.replacer.do(population,offspring)        
            generation_fitnesses.append(max(calc_fitnesses(population)))

        plt.plot(generation_fitnesses)
        plt.ylabel('Fitness')
        plt.xlabel('Generation')
        plt.show()

        return max(calc_fitnesses(population))


#Superclass for the three different tasks (variance of jobtimes and machine amount)
class Taskinitializer:
    pass

class Task1(Taskinitializer):
    global times,Amount_jobs,Amount_machines,Max_time

    Amount_jobs=300
    Amount_machines=20

    #List of the times, which are needed to complete job that has the number of list index
    times=list()

    for job in range(200):
        times.append(random.randint(10,1000))
    for job in range(100):
        times.append(random.randint(100,300))

    Max_time=sum(times)
    
class Task2(Taskinitializer):
    global times,Amount_jobs,Amount_machines,Max_time

    Amount_jobs=300
    Amount_machines=20

    #List of the times, which are needed to complete job that has the number of list index
    times=list()

    for job in range(150):
        times.append(random.randint(10,1000))
    for job in range(150):
        times.append(random.randint(400,700))

    Max_time=sum(times)

class Task3(Taskinitializer):
    global times,Amount_jobs,Amount_machines,Max_time

    Amount_jobs=101
    Amount_machines=50

    #List of the times, which are needed to complete job that has the number of list index
    times=list()

    times.append(50)
    times.append(50)
    times.append(50)
   
    for job in range(49):
        times.append(job+51)
        times.append(job+51)

    Max_time=sum(times)


class Initializer:
    pass

#Assigns jobs to random machines
class Initializer1(Initializer):
    def do(self):
        global Amount_jobs,Amount_machines,Populationsize

        population=list()

        for i in range(Populationsize):
            chromosome=list()
            for gene in range(Amount_jobs):
                chromosome.append(random.randint(0,Amount_machines-1))
            population.append(chromosome)

        return population

#Cyclic initializer, assigns machine1 to job1, machine2 to to job2,... and starts
#again with machine1 after every machine is assigned
class Initializer2(Initializer):
    def do(self):
        global Amount_jobs,Amount_machines,Populationsize

        population=list()

        for i in range(Populationsize):

            machine = i % Amount_machines
            chromosome=list()
            for gene in range(Amount_jobs):

                if machine == Amount_machines:
                    machine = 0

                chromosome.append(machine)
                machine +=1

            population.append(chromosome)

        return population


class Selector:
    pass

#Roulette-Wheel Selector
class Selector_Roulette(Selector):
    
    def compute_losses(self,population):
        #loss = time needed
        global Amount_machines,times
        
        losses=[]
        for chromosome in population:
            #compute the amount of time needed per machine
            loss_per_machine=np.zeros(Amount_machines)
            for gene in range(len(chromosome)):
                loss_per_machine[chromosome[gene]]+=times[gene]
                
            #the maximum time needed is the time needed for computing all tasks in general
            losses.append(max(loss_per_machine))
        
        return np.array(losses)
    
    def do(self,population,pool_size):
        global Amount_machines,times,max_loss
        
        losses=self.compute_losses(population)

        #fitness is larger the smaller the loss is
        fitnesses = (sum(times)-losses)

        #compute fitness so that the smallest ones are worth less
        fitnesses=fitnesses-(min(fitnesses)/2)
        #normalize them so that they are probabilities between 0 and 1
        summ=sum(fitnesses)
        if(summ):
            fitnesses/= summ
        else:
            fitnesses+=1
            fitnesses/= len(fitnesses)
         #   print('sideways',fitnesses)
        
        #roulette sections are cumulative sums
        roulette_sections=np.cumsum(fitnesses)

        #create random uniform number between 0 and 1 go through all the alleles
        #to get the biggest random number that is smaller than this random number
        selected=[]
        for x in range(pool_size):
            
            random=np.random.uniform() 
            y = 0
            while(y < len(roulette_sections)-1 and random > roulette_sections[y]):   
                    y+=1

            selected.append(population[y])

              
        return np.array(selected)

#Tournament selector
class Selector_Tournament(Selector):

    def do(self,population,pool_size):
        global Amount_machines,times
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

class Recombiner:
    pass

class Recombiner_One_Point(Recombiner):
    def do(self,population):
        
        counter=1
        children=[]
        for p in range(len(population)):
            counter+=1
             # mate every second time so the offspring population stays the same size
            if((counter)%2):
                parentA=population[p-1]
                parentB=population[p]
                #no crosspoint at the start or end
                crosspoint=random.randint(1,len(parentA)-2) #crosspoint at startorend allowed?
                childA=[]
                childB=[]
                #if x is higher than crosspoint, give parent's 1 
                #alleles to child 1 otherwise to child 2 and vice versa
                for x in range(len(parentA)):

                    if(x<=crosspoint):
                        childA.append(parentA[x])
                        childB.append(parentB[x])
                    else:
                        childB.append(parentA[x])
                        childA.append(parentB[x])
                
                children.append(childA)
                children.append(childB)

        return children
    

class Recombiner_Two_Point(Recombiner):
    def do(self,population):
         #lterally the same as one crosspoint point but with
        #two crosspoints look at that for reference
        #the only difference is, after second crosspoint parent 1's allelle
        #will be given to parent and vice versa
        counter=1
        children=[]
        for p in range(len(population)):
            counter+=1
            if((counter)%2):
                parentA=population[p-1]
                parentB=population[p]
                crosspoint1=0
                crosspoint2=0
                while crosspoint1==crosspoint2:
                    crosspoint1=random.randint(1,len(parentA)-2) 
                    crosspoint2=random.randint(1,len(parentA)-2)
                if crosspoint1>crosspoint2:
                    temp =crosspoint1
                    crosspoint1=crosspoint2
                    crosspoint2=temp
                childA=[]
                childB=[]
                for x in range(len(parentA)):

                    if(x<=crosspoint1 or x>crosspoint2):
                        childA.append(parentA[x])
                        childB.append(parentB[x])
                    else:
                        childB.append(parentA[x])
                        childA.append(parentB[x])
                
                children.append(childA)
                children.append(childB)

        return children
        

class Mutator:
    pass

#mutate randomly (one gene per chromosome)
class Mutator_Random(Mutator):
    def do(self,population):
        global Amount_machines
        for x in population:
            x[random.randint(0,len(x)-1)]=random.randint(0,Amount_machines-1)
        return population

#mutate swapping two genes of each chromosome
class Mutator_Swap(Mutator):
    def do(self,population):
        global Amount_machines
        for x in population:
            gene1=random.randint(0,len(x)-1)
            gene2=random.randint(0,len(x)-1)
            tmp = x[gene2]
            x[gene2]=x[gene1]
            x[gene1]=tmp
        return population
        
#mutate random alleles to be either machine 0 or machine 4 
#(doesn't make much sense)   
class Mutator_Boundary(Mutator):
    def do(self,population):
        global Amount_machines, Mutation_probability
        for x in population:
            for y in x:
                if np.random.uniform() < Mutation_probability:
                    y=random.randint(0,Amount_machines-1)
        return population
        

class Replacer():
    pass

#population = offspring
class Replacer_Delete_All(Replacer):
    def do(self,population,new_population):
        return new_population 

    
class Replacer_Steady_State(Replacer):
    def do(self,population_old,offspring):
        global Populationsize
        replace_amount=int(Populationsize/2)-1

        fitnesses_old=calc_fitnesses(population_old)
        fitnesses_offspring=calc_fitnesses(offspring)
        sorted_population_old=list(reversed([x for _,x in
sorted(zip(fitnesses_old,population_old))]))
        sorted_offspring=list(reversed([x for _,x in
sorted(zip(fitnesses_offspring,offspring))]))

        new_population=list()

        for i in range(replace_amount):
            new_population.append(sorted_offspring[i])
        for i in range(Populationsize-replace_amount):
            new_population.append(sorted_population_old[i])

        return new_population 


#calsulates fitness for one chomosome
def fitness(chromosome):
    global times,Max_time

    machines=[0]*Amount_machines

    for gene in range(len(chromosome)):
        allel=chromosome[gene]
        machines[allel]=machines[allel]+times[gene]

    return Max_time-max(machines)

#calculates fitnesses for whole population
def calc_fitnesses(population):
    fitnesses=list()
    for chromosome in population:
       fitnesses.append(fitness(chromosome))
    return fitnesses

#Automate tests of interplay of the different modules for the Genetic Algorithm
#(sorry for bad structure and output)
def multipletests():
    performances=list()
    for i1 in range(1): #nothing here
        for i2 in range(2):
            if i2==0: initializer=Initializer1()
            if i2==1: initializer=Initializer2()
            for i3 in range(2):
                if i3==0: selector=Selector_Tournament()
                if i3==1: selector=Selector_Roulette()
                for i4 in range(2):
                    if i4==0: recombiner=Recombiner_One_Point()
                    if i4==1: recombiner=Recombiner_Two_Point()
                    for i5 in range(2):
                        if i5==0: mutator=Mutator_Random()
                        if i5==1: mutator=Mutator_Swap()
                        for i6 in range(2):
                            if i6==0: replacer=Replacer_Steady_State()
                            if i6==1: replacer=Replacer_Delete_All()
                            performance=list()
                            for i7 in range(5):
                                for i8 in range(3):
                                    if i8==0: task=Task1()
                                    if i8==1: task=Task2()
                                    if i8==2: task=Task3() 

                                    g=GenAlg(task,initializer,selector,recombiner,mutator,replacer)
                                    performance.append(g.do())
                            #if len(performances)==18 or len(performances)==31:
                            #    print(str(initializer),str(selector),str(recombiner),str(mutator),str(replacer))
                            performances.append(sum(performance)/len(performance))
                            print(sum(performance)/len(performance))


    print(performances.index(max(performances)),max(performances))
    print(performances.index(min(performances)),min(performances))

Populationsize=20
Max_Iterations=1000

g=GenAlg(Task3(),Initializer2(),Selector_Tournament(),Recombiner_One_Point(),Mutator_Random(),Replacer_Delete_All())
g.do()

#multipletests()

