class Programmer:
    name="NULL"
    id=0

    def __init__(self, name, id):
        print("The class is define.")
        self.name= name 
        self.id= id 

        print(f"name:{self.name}\t id:{self.id}")
        
        

name=input("Enter your name: ")
id=input("Enter your id: ")

obj=Programmer(name, id)



