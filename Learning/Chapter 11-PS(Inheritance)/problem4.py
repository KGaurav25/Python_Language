class complex:
    def fc(self, a, b):
        self.a=a
        self.b=b
        print(f"First num: {a} + {b}i")
    
    def sc(self, c ,d):
        self.c=c
        self.d=d
        print(f"Second num: {c} + {d}i")

    def add(self):
        print(f"\nThe add is : {(self.a)+(self.c)} + {self.b.__add__(self.d)}i")
        
    def mul(self):
        #(ac-bd)+(ad+bc)
        
        w=self.a.__mul__(self.c)
        x=self.b.__mul__(self.d)
        y=(self.a)*(self.d)
        z=(self.b)*(self.c)


        print(f"The mul is : {w-x} + {y+z}i")
        


obj=complex()
obj.fc(2,3)
obj.sc(4,5)
obj.add()
obj.mul()