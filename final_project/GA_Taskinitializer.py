import numpy as np
from os.path import join

class Taskinitializer():

    def initialize_task(self,PATH = "VRP1"):
        task = read_task(PATH)
        return task

def parsefile(filename):
    with open(filename) as filereader:
        file_array = []
        for line in filereader:
            line = line.split(' ')
            line = [int(value) for value in line if value != '' and value != "\n"]

            file_array.append(line)
    if len(file_array) == 1:
        file_array = file_array[0]
    file_array = np.asarray(file_array)

    return file_array

def read_task(PATH):
    capacities = parsefile(join(PATH, "capacity.txt"))
    distance_matrix = parsefile(join(PATH,"distance.txt"))
    transportation_costs = parsefile(join(PATH,"transportation_cost.txt"))
    demands = parsefile(join(PATH,"demand.txt"))

    """
    print(len(distance_matrix))
    print(len(distance_matrix[0]))
    print(len(capacities))
    print(len(transportation_costs))
    print(len(demands))
    """
    return distance_matrix, capacities, transportation_costs, demands


#t = Taskinitializer().initialize_task()

