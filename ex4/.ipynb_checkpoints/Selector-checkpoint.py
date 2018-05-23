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
            if PPP.profit(trials[i]) >= PPP.profit(targets[i]):
                targets[i] = trials[i]
        return targets
