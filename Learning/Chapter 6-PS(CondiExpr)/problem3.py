# make a loat of money, buy now, subscribe this, click this

m=input("Pest your message: ")

a="make a lot of money"
b="buy now"
c="subscribe this"
d="click this"

if a in m or b in m or c in m or d in m:
    print("This message is spam")
else:
    print("This message is not spam")
