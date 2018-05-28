from PPP import PPP
import numpy as np


class Initializer:
    """
    for Step 2: randomly initialize a population of NP
    individuals
    """


    def __init__(self,ppp, Np):
        self.Np = Np
        self.ppp = ppp

    def initialize(self):
        generation = list()
        for x in range(self.Np):
            #create ppp intances for the range of the given population size
            #which is the first generation
            generation.append(self.ppp.create_vector())
        return generation
