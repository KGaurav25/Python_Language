n=int(input("Enter the number: "))

mul=1
for i in range(1,n+1):
    mul*=i
    # i+= 1
print(f"The factorial of {n} is {mul}.")

