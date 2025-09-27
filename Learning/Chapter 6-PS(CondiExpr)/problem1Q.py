a1=int(input("Enter 1st number: "))
a2=int(input("Enter 2st number: "))
a3=int(input("Enter 3st number: "))
a4=int(input("Enter 4st number: "))

if a1==a2==a3==a4:
    print("All numbers are equal")
elif(a1>=a2 and a1>=a3 and a1>=a4):
    print(F"{a1} number is greatest")
elif(a2>=a1 and a2>=a3 and a2>=a4):
    print(F"{a2} number is greatest")
elif(a3>=a1 and a3>=a2 and a3>=a4):
    print(F"{a3} number is greatest")
else:
    print(F"{a4} number is greatest")

#Q make it for invalid marks or out of rang marks