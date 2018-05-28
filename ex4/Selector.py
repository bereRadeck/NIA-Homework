import numpy as np
from PPP import PPP

class Selector:
    """
    for Selection Step:
    Evaluate the trial vector
    """

    def __init__(self,ppp):
        self.ppp = ppp

    def select(self, targets, trials):
        """
        selects either target or trial vector for each chromosome based on the fitness (PPP.profit)
        :param targets: list of target vectors
        :param trials: list of trial vectors
        :return: new generation
        """
        for i in range(len(targets)):

            trial_profit = self.ppp.profit(trials[i])

            target_profit = self.ppp.profit(targets[i])

            if trial_profit >= target_profit:
                targets[i] = trials[i]
        #new generation is returned
        return targets
