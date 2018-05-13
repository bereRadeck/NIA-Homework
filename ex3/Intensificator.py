
class Intensificator:

    def __init__(self,delta):
        self.delta = delta

    def intensify(self,pheromone_matrix,solutions):
        best_solution = solutions[0]

        for i in best_solution:
            for j in range(len(best_solution)):
            #j = best_solution[i+1]
                pheromone_matrix[i, j] = pheromone_matrix[i,j] + self.delta

        return pheromone_matrix


