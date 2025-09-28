n=int(input("Enter the number: "))

print("*"*n)
if n>2:
    for i in range(2,n):
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")
if n>=2:
    print("*"*n)

# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n)
#     else:
#         print("*", end="")
#         print(" "*(n-2),end="")
#         print("*")
        