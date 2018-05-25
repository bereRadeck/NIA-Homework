import numpy as np
from PPP import PPP

class Selector:
    """
    for Selection Step:
    Evaluate the trial vector
    """

    def __init__(self,ppp):
        self.ppp = ppp

    #select either target or trial vector for each chromosome based on the fitness (PPP.profit)
    def select(self, targets, trials):
        for i in range(len(targets)):

            self.ppp.vector_array = trials[i]
            trial_profit = self.ppp.profit()

            self.ppp.vector_array = targets[i]
            target_profit = self.ppp.profit()

            if trial_profit >= target_profit:
                targets[i] = trials[i]
        return targets
