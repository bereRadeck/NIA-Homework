import numpy as np

class Taskinitializer():

    def initialize_task(self,folder = "VRP1"):
        task = read_task(folder)
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

def read_task(folder):
    distance_matrix = parsefile("Problem/"+ folder + "/distance.txt")
    capacities = parsefile("Problem/"+ folder + "/capacity.txt")
    transportation_costs = parsefile("Problem/"+ folder + "/transportation_cost.txt")
    demands = parsefile("Problem/"+ folder + "/demand.txt")

    """
    print(len(distance_matrix))
    print(len(distance_matrix[0]))
    print(len(capacities))
    print(len(transportation_costs))
    print(len(demands))
    """
    return distance_matrix, capacities, transportation_costs, demands


t = Taskinitializer().initialize_task()

