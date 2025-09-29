with open("problem8_original.txt", "r")as f:
    st=f.read()
    print(st)
    
with open("problem8_copy.txt", "w")as f:
    f.write(st)
    st2="This is copy file"
    f.write("\n"+st2)