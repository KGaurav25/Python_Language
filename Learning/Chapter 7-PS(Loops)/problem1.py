n=int(input("Enter the number: "))

print("\nUsing For loop")
for i in range(1,11):
    print(f"{n}x{i}: ", n*i)

print("\nUsing While loop")
i=0
while (i<11):
    print(f"{n}x{i}: {n*i}")
    i +=1