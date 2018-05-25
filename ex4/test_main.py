# for debugging

from Initializer import Initializer
from DonorGenerator import DonorGenerator
from TrialGenerator import TrialGenerator
from Selector import Selector
from DE import DE
from PPP import PPP

"""
Step 1: Read values of the control parameters of DE: scale
factor F, crossover rate Cr, and the population size NP from
user.
"""

# Parameter:
np = 10
#xmin = 0
#xmax = 100
problemnumber = 1
F = 0.5
Cr = 0.3


#initializer = Initializer(xmin, xmax, np)
ppp = PPP(problemnumber)
initializer = Initializer(ppp, np)
donorgenerator = DonorGenerator(F)
trialgenerator = TrialGenerator(Cr)
selector = Selector(ppp)
de = DE


DifferentialEvolution = de(ppp, initializer, donorgenerator, trialgenerator, selector)
DifferentialEvolution.run()

