
# coding: utf-8

# In[26]:


import numpy as np

class Recombiner:
    def __init__(self, recomb_chance=0.1):
        self.recomb_chance=recomb_chance
        
    #go through all the pairs and recombine them with a certain chance

    def do(self,pool):
        for p in range(len(pool)):
            for p2 in range(len(pool)):
                if(np.random.uniform()<self.recomb_chance):
                    pool[p],pool[p2]=crossover(pool[p],pool[p2])
        
    #Here is how you make 1 child from 2 parents:
    #Step 1: Define two crossover points
    #Step 2: The section between the two crossover points 
    #of the first parent is transferred to the first child
    #    parent 1       4|5 6 7|8
    #    parent 2       8 6 5 4 7
    #    child  1       - 5 6 7 -
    #Step 3: the remaining numbers are inserted in the order in
    #which they appear in parent 2. 
    #    parent 2       8 / / 4 /
    #    child  1       8 5 6 7 4
    #For the other child you just reverse parent 1 with parent 2
    
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


# In[29]:


recomb = Recombiner()
print(recomb.do(np.array([1,2,4,6,7,3,5]),np.array([2,1,4,5,3,7,6])))

