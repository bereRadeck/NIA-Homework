import numpy as np
from PPP import PPP

class DonorGenerator:
    """
    for Mutation Step:
    Generate a donor vector corresponding to the ith target vector
    via the differential mutation scheme of DE

    """

    def __init__(self, F):
        self.F = F

    def generate_donor(self, x, generation):
        """

        :param x: an individual from the current generation
        :param generation: the curent generation
        :return: a single donor vector for the individual
        """

        # pic randomly 3 individuals from the current generation:
        # but not x itself
        
        choice_of_individuals = list(generation)
        choice_of_individuals.pop(x)

        #vectors = np.random.choice(choice_of_individuals, 3, replace=False)
        vectors = np.random.choice(range(len(choice_of_individuals)), 3, replace=False)
        x1 = choice_of_individuals[vectors[0]]
        x2 = choice_of_individuals[vectors[1]]
        x3 = choice_of_individuals[vectors[2]]

        diff = np.subtract(x2, x3)

        donor = x1 + self.F*diff
      #  print(donor)
        return donor



    def generate_donor_for_pop(self,generation):
        """

        :param generation: the current generation
        :return: a list of donors, one donor for each individual from the current generation
        """
        
        donors = []
        for x in range(len(generation)):
            donors.append(self.generate_donor(x, generation))
        return donors
