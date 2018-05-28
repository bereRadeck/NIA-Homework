# Differential Evolution
import time
import numpy as np
class DE:

    def __init__(self, ppp, initializer, donorgenerator, trialgenerator, selector):
        self.initializer = initializer
        self.donorgenerator = donorgenerator
        self.trialgenerator = trialgenerator
        self.selector = selector
        self.ppp = ppp

    def run(self,iterations):
        now=time.time()
        generation = self.initializer.initialize()
        solutions = np.zeros([iterations,len(generation)])
        for i in range(iterations):
            donors = self.donorgenerator.generate_donor_for_pop(generation)
            trials = self.trialgenerator.generate_trial(generation,donors)
            newgen = self.selector.select(generation,trials)
            generation=newgen
 
            for t in range(len(newgen)):
                solutions[i][t]=np.array(self.ppp.profit(newgen[t]))
           # print(solutions[0])
           # print('fuck')
        return solutions,time.time()-now

