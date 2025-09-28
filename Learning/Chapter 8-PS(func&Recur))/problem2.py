#  F = (C * 9/5) + 32

c=int(input("Enter the temp in C: "))

def ConvTemp(c):
     f = (c*(9/5))+32
     return f

print(ConvTemp(c))