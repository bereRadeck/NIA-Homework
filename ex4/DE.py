# Differential Evolution

class DE:

    def __init__(self, initializer, donorgenerator, trialgenerator, selector):
        self.initializer = initializer
        self.donorgenerator = donorgenerator
        self.trialgenerator = trialgenerator
        self.selector = selector

    def run(self):
        generation = self.initializer.initialize()
        
        for i in range(10):
            print(i)
            donors = self.donorgenerator.generate_donor_for_pop(generation)
            trials = self.trialgenerator.generate_trial(generation,donors)
            targets = self.selector.select(generation,trials)

