with open("problem2_high_score.txt", "r") as f:
    data=f.read()
    print(f"Data in file: {data}")

n=int(input("Enter num: "))
if n>int(data):
    with open("problem2_high_score.txt", "w") as f:
        f.write(str(n))
