with open("problem1_poem.txt","w") as f:
    
    st='''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.'''

    f.write(st)

with open("problem1_poem.txt") as f:
    
    c=f.read()
    if "twinkle" in c.lower():
        print("Yes")
    else:
        print("No")

