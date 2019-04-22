import numpy as np
class Replacer:

    def __init__(self):
        pass

    def replace(self, pop, offspring):

        fitnesses = [p['fitness'] for p in pop]
        pop = [x for x, _ in sorted(zip(pop,fitnesses), reverse=True,key=lambda pair: pair[1])]
        l = len(offspring)

        new_pop = np.append(offspring,pop[l:])
        assert len(new_pop) == len(pop)
        return new_pop

