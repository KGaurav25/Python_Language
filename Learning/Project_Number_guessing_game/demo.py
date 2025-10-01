import random

print("\t--------WELCOME--------")    
print("______Its Number Guessing Game______")
print("""\n📖 The Rules and Regulations ^-^:
        
        1.You have guess the number between 1 to 100
        2.The Enter number shuld be NUMBER and it shuld be between 1 to 100. \n\t   Otherwise it will give you invalid choice!!!
        3.After guessing it tells you the number is higher or lower 
        4.Keep guessing until it is correct!
        5.It also shows the number of guessing
        6.follow above rules!!
        
Good Luck!!! 🏆🏅🎯🌟""")


list=[]
for i in range(0, 101):
    list.append(i)
num=random.choice(list)

ch=0
guess=0
while ch!=num:

    ch=int(input("\nPlease Enter the num between 0 to 100 \nEnter your num: "))
    
    if ch<101:
        guess=guess+1
        if ch>num:
            print("Enter the lower number!")
        elif ch<num:
            print("Enter the higher number!")
        else:
            print(f"\nCongratulations!\t Your number is matches with computer numeber\nYou Guess the number in {guess}")
        
        print(f"Guess Times: {guess}")
    else:
        print("Invalid number!!!")

