class Terminator:
    def __init__(self,limit=500):
        self.limit = limit
        self.count = 0
      
    def terminates(self):
        print('Iteration: ',self.count)
        self.count += 1
        if self.count > self.limit:
            return True
        else:
            return False
        
  
        
