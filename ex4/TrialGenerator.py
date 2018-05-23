import random

import numpy as np


class TrialGenerator:
    """
    for Crossover Step:
    Generate a trial vector for the ith target vector X
    through binomial crossover
    """

    def __init__(self, Cr):
        self.Cr = Cr

    def generate_trial(self, generation, donor_vector):
        list_of_trialvectors = []
        random_index_j = np.randint(0,len(generation))

            #once for every target vector
        for i in generation:
            if np.random() <= self.Cr or random_index_j == i: #we take the donor vector
                list_of_trialvectors.append(donor_vector[i])
            else: # we just take the old vector
                list_of_trialvectors.append(generation[i])

    return list_of_trialvectors
