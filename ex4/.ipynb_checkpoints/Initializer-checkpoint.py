from PPP import PPP
import Numpy as np


class Initializer:
    """
    for Step 2: randomly initialize a population of NP
    individuals
    """

    def __init__(self, xmin, xmax, Np):
        self.Np = Np
        self.xmin = xmin
        self.xmax = xmax
        pass

    def initialize(self):
        generation = np.zeros(self.Np)
        for index, x in enumerate(generation):
            generation[index] = PPP(self.xmin, self.xmax)
        return generation
