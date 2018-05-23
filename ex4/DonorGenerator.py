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
        # but not x
        choice_of_individuals = generation
        choice_of_individuals.remove(x)

        vectors = np.random.choice(choice_of_individuals, 3)
        x1 = vectors[0]
        x2 = vectors[1]
        x3 = vectors[2]

        diff = np.substract(x2, x3)

        donor = x1 + F*diff
        return donor



    def generate_donor_for_pop(self,generation):
        """

        :param generation: the current generation
        :return: a list of donors, one donor for each individual from the current generation
        """
        donors = []
        for x in generation:
            donors.append(self.mutate(x, generation))
        return donors
