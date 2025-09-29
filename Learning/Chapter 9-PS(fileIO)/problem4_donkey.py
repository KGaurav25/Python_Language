with open("problem4_donkey.txt", "r") as f:
    data=f.read()
    
rep=(data.lower()).replace("donkey", "####")

with open("problem4_donkey.txt", "w+") as f:
    f.write(rep)

with open("problem4_donkey.txt", "r") as f:
    data=f.read()
    print(data)