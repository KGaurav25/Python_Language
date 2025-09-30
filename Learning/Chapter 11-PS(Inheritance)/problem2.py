class Animal:
    print("There are wild animals and pet animals")

class Pets(Animal):
    print("Cat and Dogs are pets")

class Dog(Pets):
    def bark(self):
        print("Dongs can bark!")


obj=Dog()
obj.bark()