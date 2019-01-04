class Dummy_Terminator:
    def __init__(self,limit=500):
        self.limit = limit
        self.count = 0
      
    def terminates(self):
        if self.count > self.limit:
            return True
        else:
            return False
        
    def call(self):
        self.count += 1