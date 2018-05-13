#from typing import List, Any
import numpy as np


class Taskinitializer():

    def __init__(self, task):

        if task == 1:
            self.file = '01.tsp'
        if task == 2:
            self.file = '02.tsp'
        if task == 3:
            self.file = '03.tsp'

        self.task_matrix = self.get_task_matrix()

    def get_task_matrix(self):
        with open('TSPs/'+self.file) as filereader:
                task_matrix = []
                for line in filereader:
                    row = line.split(' ')
                    for i in range(len(row) - 1):
                        row[i] = int(row[i])
                    row = row[0:-1]
                    task_matrix.append(row)
        return np.asarray(task_matrix)

    def solution_evaluator(self, solution):

        task_matrix = self.get_task_matrix()


        return np.sum(task_matrix[solution[0:-1], solution[1:]])

