'''Stone paper scissor'''

def info():
    print("1: Stone")
    print("2: Paper")
    print("3: Scissor")

info()
ch1=int(input("Enter your choice for player 1: "))

info()
ch2=int(input("\nEnter your choice for player 2: "))

if ch1==ch2:
    print(" It's a draw")
elif ch1==1 and ch2==2:
    print("Player 2 win")
elif ch1==1 and ch2==3:
    print("Player 1 win")
elif ch1==2 and ch2==1:
    print("Player 1 win")
elif ch1==2 and ch2==3:
    print("Player 2 win")
elif ch1==3 and ch2==1:
    print("Player 2 win")
elif ch1==3 and ch2==2:
    print("Player 1 win")
else:
    print("Invalid Choce!")

