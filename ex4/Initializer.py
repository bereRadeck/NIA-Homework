from PPP import PPP
import Numpy as np


class Initializer:
    """
    for Step 2: randomly initialize a population of NP
    individuals
    """

    def __init__(self, xmin, xmax, np):
        self.np = np
        self.xmin = xmin
        self.xmax = xmax
        pass

    def initialize(self):
        generation = np.zeros(self.np)
        for index, x in enumerate(generation):
            generation[index] = PPP(self.xmin, self.xmax)
        return generation
