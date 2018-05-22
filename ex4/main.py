#for debugging

from Initializer import Initializer
from DonorGenerator import DonorGenerator
from TrialGenerator import TrialGenerator
from Selector import Selector
from DE import DE

#Parameter:
#xmin =
#xmax =
#F =
#Cr =



initializer = Initializer(xmin,xmax,NP)
donorgenerator = DonorGenerator(F)
trialgenerator = TrialGenerator(Cr)
selector = Selector
DE = DE

DifferentialEvolution = DE(initializer,donorgenerator,trialgenerator,selector)