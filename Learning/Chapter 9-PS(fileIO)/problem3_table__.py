#genrate tables from 2 to 5

def table():
    for i in range(2,6):
        with open(f"problem3_table_{i}.txt", "w") as f:
            for j in range(1,11):
                mul=i*j
                f.write(f"{i} x {j} = "+str(mul)+"\n")

table()