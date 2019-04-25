from GA_Taskinitializer import *

import os

PATH_HOME = os.sep.join(os.getcwd().split(os.sep)[:-1])

PATH_PROBLEM = os.sep.join(['Problem','VRP1'])

PATH = os.sep.join([PATH_HOME,PATH_PROBLEM])

task_initializer = Taskinitializer()

dist_matrix, capacities, trans_cost, demands = task_initializer.initialize_task(PATH)



assert len(trans_cost) ==  len(capacities)
assert len(demands) == dist_matrix.shape[0]-1



