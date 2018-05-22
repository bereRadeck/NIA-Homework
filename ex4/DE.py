#Differential Evolution

from PPP import PPP
class DE:

    def __init__(self,initializer,donorgenerator,trialgenerator,selector):
        self.initializer = initializer
        self.donorgenerator = donorgenerator
        self.trialgenerator = trialgenerator
        self.selector = selector
        pass

    def run(self):
        pass