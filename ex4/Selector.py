import Numpy as np
from PPP import PPP

class Selector:
    """
    for Selection Step:
    Evaluate the trial vector
    """

    def __init__(self):
        pass

    #select either target or trial vector for each chromosome based on the fitness (PPP.profit)
    def select(self, targets, trials):
        for i in range(len(targets)):

            PPP.vector_array = trials[i]
            trial_profit = PPP.profit()

            PPP.vector_array = targets[i]
            target_profit = PPP.profit()

            if trial_profit >= target_profit:
                targets[i] = trials[i]
        return targets
