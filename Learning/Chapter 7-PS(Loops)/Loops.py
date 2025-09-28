#While loop
print("While loop")
# n=1

# while n<6:
#     print(n)
#     n +=1

l=[1, 2, 3, 4, "Gaurav", False, 3.14]

i=0
while i<7:
    print(l[i])
    i +=1

#For loop
print("\nFor loop")

for item in l:
    print(item)
else:
    print("Done") #for loop with else


# for a in range(2, 21, 2):
#     print(a)

s="Khuliii"
for i in s:
    print(i)

#Break and continue
print("\nBreak and Continue")
#break
for i in range(1,11):
    if (i==4):
        break #Exit the loop
    print(i)

print("\n")
#Continue
for i in range(1,11):
    if (i==4):
        continue #Skip this iteration
    print(i)

for i in range(20):
    pass #do nothing we can write this loop later

print("\n")
i=0
while i<11:
    print(i)
    i +=1
