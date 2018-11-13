import numpy as np
import random as rnd
import copy 

class Recombiner:
    def __init__(self, recomb_chance=0.1):
        self.recomb_chance=recomb_chance
       
    

    def do(self,pool):
        '''go through all the pairs and recombine them with a certain chance'''
        
        #first go through all the items
        for p1 in range(len(pool)):
            #then with a certain chance...
            if(np.random.uniform()<self.recomb_chance):
                #create crossover point...
                cr_point1=np.random.choice(range(len(pool[p1])-2))
                cr_point2=np.random.choice(range(len(pool[p1])-cr_point1-2))+cr_point1+2
                #search for a fitting partner in the rest of the pool (in random order)...
                rnge = list(range(len(pool)))
                rnd.shuffle(rnge)
                for p2 in rnge:
                    if not(p2==p1):  
                        #look whether a potential swapping partner has the same set of
                        #numbers between those two points (they don't have to have the same order)
                        
                        compareto = np.zeros(pool[p1].shape)
                        compareto[cr_point1:cr_point2]=np.ones(cr_point2-cr_point1)
                        segment1= pool[p1][cr_point1:cr_point2]
                        mask=np.isin(pool[p2],segment1)
                        
                        #If yes, swap them
                        if np.array_equal(mask,compareto):
                            print(pool[p1][cr_point1:cr_point2])
                            print(pool[p2][cr_point1:cr_point2])
                            replace_with= copy.deepcopy(pool[p1][cr_point1:cr_point2])
                            pool[p1][cr_point1:cr_point2]=pool[p2][cr_point1:cr_point2]
                            pool[p2][cr_point1:cr_point2]=replace_with
                            break
        return pool
 '''   
    def make_child(self,parent1,parent2,cr_point1,cr_point2):
        #take section from parent
        child = np.zeros(parent1.shape)
        segment1= parent1[cr_point1:cr_point2]
        child[cr_point1:cr_point2] = segment1
        #define a mask to find out which numbers the child already has
        mask1=np.isin(parent2,segment1,invert=True)
        #mark them out in parent 2
        p2remains = parent2[mask1]
        count = 0
        for c in range(cr_point1):
            child[c]= p2remains[c]
        for c in range(len(parent2)-cr_point2):
            child[c+cr_point2]= p2remains[c+cr_point1]
        return child
    
    #This function makes two children from two parents and creates two crossover points
    def crossover(self,parent1,parent2):
        allele1=np.random.choice(range(len(parent1)-1))
        allele2 = np.random.choice(range(len(parent2)-allele1))+allele1

        child1=self.make_child(parent1,parent2,allele1,allele2)
        child2=self.make_child(parent2,parent1,allele1,allele2)
        return child1,child2
        '''
