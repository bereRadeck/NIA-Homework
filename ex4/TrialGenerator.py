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

            #once for every target vector
        for chromosome in generation:
            random_index_j = np.randint(0,len(chromosome))

            for index,x in enumerate(chromosome):
                if np.random() <= self.Cr or random_index_j == index: #we take the donor vector
                    chromosome[index]=donor_vector[chromosome][index]
                #else: # we just take the old vector
                #    chromosome[index]=generation[chromosome][index]
            list_of_trialvectors.append(chromosome)
        return list_of_trialvectors
