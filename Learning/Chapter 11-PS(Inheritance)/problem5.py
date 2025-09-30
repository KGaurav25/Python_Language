class vector:
    def FV(self, a1, a2):
        self.a1=a1
        self.a2=a2
        print(f"First Vector: \nA = {a1}i + {a2}j")
    
    def SV(self, b1 ,b2):
        self.b1=b1
        self.b2=b2
        print(f"Second Vector: \nB = {b1}i + {b2}j")

    def sum(self):
        print(f"\nA + B = {(self.a1)+(self.b1)} + {self.a2.__add__(self.b2)}i")
        
    def dot(self):
        
        x=(self.a1)*(self.b2)
        y=(self.a2)*(self.b2)


        print(f"A . B = {x} + {y}")
        
obj=vector()
obj.FV(2,3)
obj.SV(4,5)
obj.sum()
obj.dot()