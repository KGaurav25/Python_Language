print("Stone Paper Scissor\n")
n=int(input("Do you want do play with \n1:Computer \nOR \n2:User: "))

def info():
    print("1: Stone")
    print("2: Paper")
    print("3: Scissor")


if n==1:
    ch1="Stone"     #Using list
    score=0

    for i in range(1,4):
        print(f"\nRound number {i}")
        info()

        ch2=int(input("Enter your choice: "))

        if ch2==2:
            score+=1
        elif ch2==3:
            print("You Lost")
        elif ch2==1:
            print("It's Draw!")
        else:
            print("Invalid Choice!")
        

elif n==2:
    for i in range(1,4):         #who many times do you want to play
        print(f"\nRound number {i}")
        info()
        ch1=int(input("Enter your choice for player 1: "))

        # info()
        ch2=int(input("Enter your choice for player 2: "))

        if ch1==ch2:
            print(" It's a draw!")
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
            print("Invalid Choice!")

