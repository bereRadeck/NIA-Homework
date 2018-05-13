import numpy as np

class Initializer():

    def initialize(self,taskinitializer):
        task_matrix = taskinitializer.get_task_matrix()
        len = task_matrix.shape[0]
        return np.ones((len,len))