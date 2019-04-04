import numpy.random as rnd

class Simple_Mutator:
    
    def __init__(self,mutation_probability=0.1):
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
                
