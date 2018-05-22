# Power Plant Problem
import numpy as np


class PPP:

    def __init__(self, xmin, xmax):
        self.xmin = xmin
        self.xmax = xmax
        # initialize chromosome vector randomly  within the search space
        # constrained by the prescribed minimum and maximum bounds:

        d = len(xmin)
        self.x = xmin + (xmax-xmin) * np.random.uniform(0, 1, d)

        #alternative:
        x = np.zeros(d)
        for i in range(d):
            x[i] = np.random.uniform(xmin[i], xmax[i])

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
