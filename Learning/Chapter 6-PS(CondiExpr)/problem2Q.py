s1=int(input("Enter marks of subject 1: "))
s2=int(input("Enter marks of subject 2: "))
s3=int(input("Enter marks of subject 3: "))

if s1>=33 and s2>=33 and s3>=33:
    if (s1+s2+s3)/3 >= 40:
        print("You are pass")
    else:
        print("You are fail")
