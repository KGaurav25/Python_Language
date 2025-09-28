print("Functions\n")

def avg():    #creating a function
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))

    avg=((a+b)/2)
    print(avg)

avg() #function call
print("Thank You")


#Default argument

def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Mehuni") 
# goodDay("Mehuni", "Thanks")


print("\nRecursion")

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("Enter the number: "))
print(f"The factorial of {n}: {factorial(n)}")