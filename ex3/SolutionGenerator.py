import Taskinitializer
import numpy as np

class SolutionGenerator():

    def __init__(self, alpha, beta, num_of_ants, task=Taskinitializer):
        self.task = task
        self.num_of_ants = num_of_ants
        self.alpha = alpha
        self.beta = beta
        self.task_matrix = task.get_task_matrix


    def generate_solution(self, pheromone_marix):
        num_citys = self.task_matrix.shape[0]
        citys = np.arrange(1,num_citys,1)
        eta_matrix = 1 / task.get_task_matrix()

        city = #random choice of citys to start with
        solution = np.array([0])

        for c in range(num_citys-1):

            #berechne die Wahrscheinlichkeiten von city zu allen möglichen city_next zu gelangen

            #bestimme city_next anhand der wahrscheinlichkeiten

            #appende city_next an solution

            #returne solution






