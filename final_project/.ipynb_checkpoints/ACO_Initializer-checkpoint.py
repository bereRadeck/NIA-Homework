import numpy as np

class Initializer():

    def initialize(self,task):
        task_matrix = task.get_task_matrix()
        size = len(task_matrix[0])
        return np.ones((size,size)) 
    
    #greetings, stranger
