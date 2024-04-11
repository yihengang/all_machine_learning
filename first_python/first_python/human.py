class Human:
    # definining properties
    # self is always passed, we don't need to pass this argument
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    
    # defining methods
    def do_work(self):
        if self.occupation == "data scientist":
            print(self.name, "builds and trains machine learning models")
        elif self.occupation == "MMA fighter":
            print(self.name, "fights for a living")

    def speaks(self):
        print(self.name, "says how are you?")        

Cason = Human("Cason", "data scientist")
Cason.do_work()

Abdul = Human("Abdul", "MMA fighter")
Abdul.speaks()