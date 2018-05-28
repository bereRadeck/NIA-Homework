import random

import numpy as np


class TrialGenerator:
    """
    for Crossover Step:
    Generate a trial vector for the ith target vector X
    through binomial crossover
    """

    def __init__(self, Cr, p):
        self.Cr = Cr
        self.p = p-1
        self.upper_bounds = [[5000000, 30000000, 12000000, 2000000, 30000000, 20000000, 0.45, 0.25, 0.2],
                             [5000000, 30000000, 12000000, 2000000, 30000000, 20000000, 0.45, 0.25, 0.2],
                             [5000000, 30000000, 12000000, 1000000, 5000000, 5000000, 0.5, 0.3, 0.1]]

    def generate_trial(self, generation, donor_vectors):
        """
        generates list of trial generators, one for each targetvector
        :param generation: list of the current population (targetvectors)
        :param donor_vectors: list of donorvectors
        :return: list of trialvectors for selector
        """
        list_of_trialvectors = []

        #once for every target vector (every chromosome in the current generation)
        for cindex,chromosome in enumerate(generation):
            new_chromosome=np.zeros(len(chromosome))
            random_index_j = np.random.randint(0,len(chromosome))

            for xindex,x in enumerate(chromosome):
                if np.random.uniform() <= self.Cr or random_index_j == xindex:
                    #check whether new vector is between the boundarys and correct if needed
                    if donor_vectors[cindex][xindex] > self.upper_bounds[self.p][xindex]:
                        new_chromosome[xindex] = self.upper_bounds[self.p][xindex]
                    elif donor_vectors[cindex][xindex] < 0:
                        new_chromosome[xindex] = 0
                    else:
                        #take the value from the donor vector
                        new_chromosome[xindex]=donor_vectors[cindex][xindex]
                else:
                    #take the value from the target vector
                    new_chromosome[xindex]=chromosome[xindex]
            list_of_trialvectors.append(new_chromosome)
            
        return list_of_trialvectors
