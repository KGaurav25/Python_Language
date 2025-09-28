def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return sum(n-1)+n

n=int(input("Enter number: "))
print(sum(n))
