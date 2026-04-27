class Calculator:
    
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def s_root(self):
        print(f"The square root is {self.n**1/2}")

            
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

a = Calculator(9)
a.square()
a.s_root()
a.cube()