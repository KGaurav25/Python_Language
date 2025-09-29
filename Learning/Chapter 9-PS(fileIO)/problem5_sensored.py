l=["computer", "python", "c++", "java" , "javascript"]

with open("problem5_sensored.txt", "r") as f:
    data=f.read()

for i in l:
    data=(data.lower()).replace(i, "***")

with open("problem5_sensored.txt", "w") as f:
    f.write(data)

print(data)
