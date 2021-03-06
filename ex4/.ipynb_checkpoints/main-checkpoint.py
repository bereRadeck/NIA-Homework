# for debugging

from Initializer import Initializer
from DonorGenerator import DonorGenerator
from TrialGenerator import TrialGenerator
from Selector import Selector
from DE import DE

"""
Step 1: Read values of the control parameters of DE: scale
factor F, crossover rate Cr, and the population size NP from
user.
"""

# Parameter:
# np
# xmin =
# xmax =
# F =
# Cr =


initializer = Initializer(xmin, xmax, np)
donorgenerator = DonorGenerator(F)
trialgenerator = TrialGenerator(Cr)
selector = Selector
de = DE

DifferentialEvolution = de(initializer, donorgenerator, trialgenerator, selector)
