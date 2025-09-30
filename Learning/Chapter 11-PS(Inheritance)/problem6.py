class display:
    
    def __init__(self, x,y, z):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    

obj=display(2, 3, 4)
print(obj)