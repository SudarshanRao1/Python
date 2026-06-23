class Calculator:
    def __init__(self , n):
        self.n = n
    
    def square(self):
        print(f"The square is {self.n * self.n}")
    
    def cobe(self):
        print(f"The square is {self.n * self.n * self.n}")
    
    def squareroot(self):
        print(f"The square is {self.n **1/2}")

    @staticmethod
    def hello():
        print("Hello world")

a = Calculator(4)

a.square()
a.cobe()
a.squareroot()
a.hello()