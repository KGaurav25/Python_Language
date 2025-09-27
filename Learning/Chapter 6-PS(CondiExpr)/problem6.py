marks=int(input("Enter your maeks out of 100:"))

if marks>100 or marks<0:
    print("Invalid marks")
elif marks>=90:
    print("You got Ex")
elif marks>=80:
    print("You got A")
elif marks>=70:
    print("You got B")
elif marks>=60: 
    print("You got C")  
elif marks>=50: 
    print("You got D")
else:
    print("You got F")    