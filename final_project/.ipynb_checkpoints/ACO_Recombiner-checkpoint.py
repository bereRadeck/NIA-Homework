
# coding: utf-8

# In[26]:


import numpy as np

class Recombiner:
    def __init__(self, recomb_chance=0.1):
        self.recomb_chance=recomb_chance
    def do(self,pool):
        for p in range(len(pool)):
            for p2 in range(len(pool)):
                if(np.random.uniform()<self.recomb_chance):
                    pool[p],pool[p2]=crossover(pool[p],pool[p2])
        
    def make_child(self,parent1,parent2,cr_point1,cr_point2):
        child = np.zeros(parent1.shape)
        segment1= parent1[cr_point1:cr_point2]
        child[cr_point1:cr_point2] = segment1

        mask1=np.isin(parent2,segment1,invert=True)
        p2remains = parent2[mask1]
        count = 0
        for c in range(cr_point1):
            child[c]= p2remains[c]
        for c in range(len(parent2)-cr_point2):
            child[c+cr_point2]= p2remains[c+cr_point1]
        return child

    def crossover(self,parent1,parent2):
        allele1=np.random.choice(range(len(parent1)-1))
        allele2 = np.random.choice(range(len(parent2)-allele1))+allele1

        child1=self.make_child(parent1,parent2,allele1,allele2)
        child2=self.make_child(parent2,parent1,allele1,allele2)
        return child1,child2


# In[29]:


recomb = Recombiner()
print(recomb.do(np.array([1,2,4,6,7,3,5]),np.array([2,1,4,5,3,7,6])))

