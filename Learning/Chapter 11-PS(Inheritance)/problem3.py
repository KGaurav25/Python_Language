class Emp:
    def name(self, name):
        self.name=name
        print(f"Your name is: {self.name}")
        

class salary(Emp):
    
    def sal(self, sal):
        self.salary=sal
        print(f"Current salary: {sal}")
    
    def increment(self):
        i=100
        new=self.salary+i
        print(f"After increament your salary is: {new}")

obj=salary()
n=input("Enter your name: ")
sal=int(input("Enter your salary: "))
obj.name(n)
obj.sal(sal)
obj.increment()