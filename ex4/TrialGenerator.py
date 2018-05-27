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

    def generate_trial(self, generation, donor_vectors):
        list_of_trialvectors = []

            #once for every target vector
        for cindex,chromosome in enumerate(generation):
            random_index_j = np.random.randint(0,len(chromosome))

            for xindex,x in enumerate(chromosome):
                if np.random.uniform() <= self.Cr or random_index_j == xindex: #we take the donor vector
                    chromosome[xindex]=donor_vectors[cindex][xindex]
                #else: # we just take the old vector
                #    chromosome[index]=generation[chromosome][index]
            list_of_trialvectors.append(chromosome)
        return list_of_trialvectors
