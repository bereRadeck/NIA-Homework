import numpy.random as rnd
import copy

class Ordered_Recombiner:
    
    def __init__(self,chance=0.1):
        self.chance = chance
    
    
    def recombine(self,pool):
        
        for p in pool:
            capacities= p['vehicle_capacities']
         
        if rnd.uniform() < self.chance:
                
                p2=p
                while p2==p:
                     p2 = rnd.choice(pool)
                capacities1=p['capacities']
                capacities2=p2['capacities']
                new1 = copy.deepcopy(capacities1)
                new2 = copy.deepcopy(capacities2)
                
                cr_point1=rnd.choice(range(len(new1)-1))
                cr_point2=rnd.choice(range(len(new1)-cr_point1))+cr_point1+1
                
                
                slice1 =  new2[cr_point1:cr_point2]
               # print(slice1)
                for s in slice1:
                    #print(s)
                    del new1[new1.index(s)]
                for s in slice1:
                    new1.insert(cr_point1,s)
                

                new1_ = copy.deepcopy(capacities1)
                new2_ = copy.deepcopy(capacities2)

                slice2 =  new1_[cr_point1:cr_point2]
               # print(slice2)
                for s in slice2:
                    del(new2_[new2_.index(s)])
                for s in slice2:
                    new2_.insert(cr_point1,s)
                
                p['capacities']=new1
                p2['capacities']=new2_
