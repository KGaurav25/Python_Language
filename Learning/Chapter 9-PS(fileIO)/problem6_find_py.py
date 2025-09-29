with open("problem6_find_pythone.txt", "w")as f:
    st='''Python is a high-level, versatile, and easy-to-learn programming language that is widely used for web development, data analysis, artificial intelligence, scientific computing, and automation. 
It was created by Guido van Rossum and first released in 1991. 
Python emphasizes readability and simplicity, using clear and concise syntax that makes it ideal for beginners as well as experienced developers. 
Its vast standard library and active community support make it a powerful tool for building a wide range of applications, from small scripts to complex machine learning systems. 
Python’s flexibility and compatibility with other languages and tools have made it one of the most popular programming languages in the world today.
'''
    f.write(st)

with open("problem6_find_pythone.txt", "r")as f:
    r=f.read()
    if "python" in r.lower():
        print("Pythone in give file")
    else:
        print("Not")