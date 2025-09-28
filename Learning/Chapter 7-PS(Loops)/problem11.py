n=int(input("Enter the number: "))

for i in range(1,n+1):
    if((i%2)!=0):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2), end="")
        print("*")