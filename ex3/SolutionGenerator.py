import Taskinitializer
import numpy as np

class SolutionGenerator():

    def __init__(self, alpha, beta, num_of_ants):
        self.num_of_ants = num_of_ants
        self.alpha = alpha
        self.beta = beta

    def set_task(self, task):
        self.task = task
        self.task_matrix = task.get_task_matrix()

    def generate_solution(self, pheromone_matrix):
        num_citys = self.task_matrix.shape[0]
        cities = np.arange(1,num_citys,1)
        eta_matrix = 1 / self.task_matrix

        city = np.random.choice(cities,1,False)
        
        cities = cities.delete(city) #needs an index or something (you ment delete and not remove, right?)
        solution = np.array([city])

        for c in range(num_citys-1):

            #berechne die Wahrscheinlichkeiten von city zu allen möglichen city_next zu gelangen
            n = np.power(pheromone_matrix[city, cities], self.alpha)*np.power(eta_matrix[city,cities],self.beta)
            d = np.sum(np.power(pheromone_matrix[city, cities], self.alpha)*np.power(eta_matrix[city,cities],self.beta))

            ps = n/d


            #bestimme city_next anhand der wahrscheinlichkeiten
            city_next = np.random.choice(cities,1,False,ps)

            #appende city_next an solution
            solution.append(city_next)
            
            #entferne city aus der liste
            cities = cities.delete(city_next) #needs an index or something

            city = city_next

            #returne solution
        return solution

    def collecting_solutions(self,pheromone_matrix):

        solutions = np.array() #gives me an error, needs a parameter [list() should work, but well]
        evaluations = np.array()

        for ant in range(self.num_of_ants):
            solutions.append(self.generate_solution(pheromone_matrix))
            evaluations.append(self.task.solution_evaluation(solutions[ant]))


            indices = np.argsort(evaluations)
            #evaluations = np.array(evaluations)
            #evaluations = evaluations[indices]
            solutions = np.array(solutions)
            solutions = solutions[indices]
        return solutions, evaluations








