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

    def __init__(self,problemnumber, Np):
        self.Np = Np
        self.problemnumber = problemnumber

    def initialize(self):
        generation = np.zeros(self.Np)
        for index, x in enumerate(generation):
            generation[index] = PPP(self.problemnumber)
            #generation[index] = PPP(self.xmin, self.xmax)

        return generation
