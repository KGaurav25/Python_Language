letter='''Dear <|NAME|>,
your are selected!
<|DATE|>'''

name=str(input("Enter your name: "))
date=str(input("Enter the date: "))

print(letter.replace("<|NAME|>", name).replace("<|DATE|>", date))