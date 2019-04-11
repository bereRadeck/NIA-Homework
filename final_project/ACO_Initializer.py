import numpy as np

class ACO_Initializer():

    def initialize(self, customers_to_visit):
        print('customers_to_visit', customers_to_visit)
        print()
        size = len(customers_to_visit)
        return np.ones((size,size)) 
