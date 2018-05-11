import numpy as np

class Initializer():

    def initialize(self,task):
        task_matrix = task.get_task_matrix()
        len = task_matrix.shape[0]
        return np.ones((len,len))