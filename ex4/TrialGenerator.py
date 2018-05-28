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
            new_chromosome=np.zeros(len(chromosome))
            random_index_j = np.random.randint(0,len(chromosome))

            for xindex,x in enumerate(chromosome):
                if np.random.uniform() <= self.Cr or random_index_j == xindex: #we take the donor vector
                    new_chromosome[xindex]=donor_vectors[cindex][xindex]
              #  print(donor_vectors[chromosome][index])
                #print(generation[chromosome][xindex])
                else: 
                    new_chromosome[xindex]=chromosome[xindex]
            list_of_trialvectors.append(new_chromosome)
            
        return list_of_trialvectors
