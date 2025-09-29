with open("problem9_m1.txt")as f:
    r1=f.read()

# n=str(input("Enter your file name(Without .txt): "))
with open("problem9_m2.txt")as f:
    r2=f.read()

if (r1.lower()==r2.lower()):
    print("Both files have same content!")
else:
    print("Both files are diffrent!")