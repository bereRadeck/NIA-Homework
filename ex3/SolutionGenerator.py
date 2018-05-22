import Taskinitializer
import numpy as np

class SolutionGenerator():

    def __init__(self, alpha, beta, num_of_ants,task):
        self.num_of_ants = num_of_ants
        self.alpha = alpha
        self.beta = beta
        self.task = task
        self.task_matrix = task.get_task_matrix()


    def generate_solution(self, pheromone_matrix):
        num_citys = self.task_matrix.shape[0]

        cities = np.arange(0,num_citys,1)



        #creating eta matrix
        eta_matrix = np.ones((num_citys,num_citys))
        for i in range(num_citys):
            for j in range(num_citys):

                if i == j:
                    eta_matrix[i,j] = 0
                else:
                    eta_matrix[i,j] = 1/self.task_matrix[i,j]



        #selecting first city randomly
        city = np.random.choice(cities,1,False)

        for i,c in enumerate(cities):
            if c == city:
                np.delete(cities,i)

        #appending first city to solutions
        solution = np.array([city])


        for c in range(num_citys-1):

            #berechne die Wahrscheinlichkeiten von city zu allen möglichen city_next zu gelangen


            n = np.power(pheromone_matrix[city, cities], self.alpha)*np.power(eta_matrix[city,cities],self.beta)

            d = np.sum(np.power(pheromone_matrix[city, cities], self.alpha)*np.power(eta_matrix[city,cities],self.beta))

            ps = n/d

            #bestimme city_next anhand der wahrscheinlichkeiten
            city_next = np.random.choice(cities,1,False,ps)


            #appende city_next an solution
            solution = np.append(solution,city_next)

            
            #entferne city aus der liste

            for i, c in enumerate(cities):
                if c == city:
                    np.delete(cities, i)

            #cities = cities.delete(city_next) #needs an index or something


            city = city_next

            #returne solution
        return solution

    def collecting_solutions(self,pheromone_matrix):


        solutions = list()
        #print(solutions)
        evaluations = list()

        for ant in range(self.num_of_ants):

            solution = self.generate_solution(pheromone_matrix)
            solutions.append(solution)

            evaluation = self.task.solution_evaluation(solutions[ant])

            evaluations.append(evaluation)


        for ant in range(self.num_of_ants):
            solutions.append(self.generate_solution(pheromone_matrix))
            evaluations.append(self.task.solution_evaluation(solutions[ant]))



        indices = np.argsort(evaluations)
        evaluations = np.array(evaluations)
        evaluations = evaluations[indices]
        solutions = np.array(solutions)
        solutions = solutions[indices]
        return solutions, evaluations








