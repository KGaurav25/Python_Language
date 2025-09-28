n=int(input("Enter the number: "))

if n==1:
    print("1 is not a prime neither composite")
else:
    for i in range(2,n):
        if (n%i)==0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
    







# 11/(2,3,4,5,6,7,8,9,10,11)
# 14/(2,3,4,5,6,7,8,9,10,11,12,13,14)