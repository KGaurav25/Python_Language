with open("problem7.txt", "r") as f:
    lines=f.readlines()
    print(len(lines))

with open("problem7.txt", "r") as f:
    for i in range(1, len(lines)+1):
        n=f.readline()
        if "python" in n:
            print(i)
