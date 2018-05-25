from PPP import PPP
import numpy as np


class Initializer:
    """
    for Step 2: randomly initialize a population of NP
    individuals
    """

    #def __init__(self, xmin, xmax, Np):
     #   self.Np = Np
      #  self.xmin = xmin
       # self.xmax = xmax
        #pass

    def __init__(self,ppp, Np):
        self.Np = Np
        #self.problemnumber = problemnumber
        self.ppp = ppp

    def initialize(self):
        generation = list()#np.zeros(self.Np)
        for x in range(self.Np):
            generation.append(self.ppp.create_vector())
            #generation[index] = PPP(self.xmin, self.xmax)
        return generation
