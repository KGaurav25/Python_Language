with open("problem11_original.txt", "r")as f:
    st=f.read()
    # print(st)
    
with open("problem11_rename.txt", "w")as f:
    f.write(st)
    st2="This is remane file"
    f.write("\n"+st2)