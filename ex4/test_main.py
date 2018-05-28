from Initializer import Initializer
from DonorGenerator import DonorGenerator
from TrialGenerator import TrialGenerator
from Selector import Selector
from DE import DE
from PPP import PPP
import matplotlib.pyplot as plt
"""
Step 1: Read values of the control parameters of DE: scale
factor F, crossover rate Cr, and the population size NP from
user.
"""

def visualize(DE,iterations,title='Differential Evolution'):
    results,time=DE.run(iterations)
    fig,ax = plt.subplots(figsize=(8,8))
    for x in range(10):
        plt.plot(results[:,x],label='Vector'+str(x))
    ax.ticklabel_format(style='plain')
    plt.ylabel("Profit/Fitness")
    plt.xlabel("Iteration")
    print('Time needed:',time)
    plt.legend()
    plt.show()


# Parameter:
np=10
problemnumber = 1
F = 0.5
Cr = 0.3


#initializer = Initializer(xmin, xmax, np)
ppp = PPP(problemnumber)
initializer = Initializer(ppp, np)
donorgenerator = DonorGenerator(F)
trialgenerator = TrialGenerator(Cr,problemnumber)
selector = Selector(ppp)
de = DE


DifferentialEvolution = de(ppp, initializer, donorgenerator, trialgenerator, selector)
results,time=DifferentialEvolution.run(500)
print(time)
visualize(DifferentialEvolution,500)
#visualize(DifferentialEvolution,500)
#visualize(DifferentialEvolution,500)


