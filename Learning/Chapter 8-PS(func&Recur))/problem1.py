def greatestNum (a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    return "Done"

print(greatestNum(12,32,21))