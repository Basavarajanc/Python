class Car:
    
    def __init__(self):
        self.cluth = True
        self.acc = True
        self.brea = False
       
    
    def start(self):
        print("car started", self)
        
se = Car().start()
