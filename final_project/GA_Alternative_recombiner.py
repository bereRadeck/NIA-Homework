import numpy as np
from collections import Counter

class Recombiner:

    def recombine(self,parents):

        for parentpair in parents:

            parent1 = parentpair[0]['vehicle_capacities']
            parent2 = parentpair[1]['vehicle_capacities']

            vehicles = np.unique(parent1)

            vehicle_1,vehicle_2 = np.random.choice(vehicles,2,replace=False)

            print(vehicle_1)
            print(vehicle_2)

            parent1_copy = np.array(parent1)
            parent2_copy = np.array(parent2)
            # put vehicles at their new place
            print(len(parent1_copy[parent1_copy == vehicle_1]))
            print(len(parent1[parent2_copy == vehicle_1]))
            parent1[parent2_copy == vehicle_1] = parent1_copy[parent1_copy == vehicle_1]
            parent2[parent1_copy == vehicle_2] = parent2_copy[parent2_copy == vehicle_2]

            # replace the old vehicle indices with values that were at the place of the car before
            parent1[parent1_copy == vehicle_1] = parent1_copy[parent2_copy == vehicle_1]
            parent2[parent2_copy == vehicle_2] = parent2_copy[parent1_copy == vehicle_2]

            parentpair[0]['vehicle_capacities'] = parent1
            parentpair[1]['vehicle_capacities'] = parent2

        return parents