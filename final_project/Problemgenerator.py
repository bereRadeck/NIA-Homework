
import random, numpy as np
import math

n_customers = 5
n_cars = 10

demand_min = 1
demand_max = 10

capacitiy_min = 1
capacitiy_max = 10


demands = random.sample(range(demand_min,demand_max+1),n_customers)
capacities = random.sample(range(capacitiy_min,capacitiy_max+1),n_cars)

positions = []
for customer in range(n_customers+1):
    positions.append(np.array(random.sample(range(0,1000),2)))

distance_matrix = []
for customer_a in positions:
    distances = []
    for customer_b in positions:
        distances.append(int(np.linalg.norm(customer_a-customer_b)))
    distance_matrix.append(distances)

#distance_matrix = np.array(distance_matrix)

print(distance_matrix)
print(demands)
print(capacities)

path = "Problem/VRPsmall/"

with open(path+'distance.txt', 'w') as f:
    for line in distance_matrix:
        for element in line:
            f.write("%s " % element)
        f.write("\n")

with open(path+'demand.txt', 'w') as f:
        for element in demands:
            f.write("%s " % element)

with open(path+'capacity.txt', 'w') as f:
        for element in capacities:
            f.write("%s " % element)

with open(path+'transportation_cost.txt', 'w') as f:
        for element in capacities:
            f.write("%s " % math.ceil(int(element)/2))
