class train:
    
    def __init__(self):
        print("Welcome")

    
    def booking(self):
        a=10
        print(f"Availabe tickets are {a}")
        n=int(input("How many tickes wants to book? :"))
        print(f"{n} tickets are booked.\nThe remaining tickes are {a-n}")

print("\n")

obj=train()
obj.booking()