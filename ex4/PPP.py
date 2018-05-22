# Power Plant Problem
import numpy as np


class PPP:

    def __init__(self, xmin, xmax):
        self.xmin = xmin
        self.xmax = xmax
        # initialize chromosome vector randomly  within the search space
        # constrained by the prescribed minimum and maximum bounds:
        x = np.zeros(len(xmin))
        for i, v in enumerate(x):
            x[i] = np.random.random_integers(xmin[i], xmax[i])

    def purchasing_costs(self):
        pass

    def production_costs(self):
        pass

    def costs(self):
        pass

    def demand(self):
        pass

    def revenue(self):
        pass

    def profit(self):
        pass
