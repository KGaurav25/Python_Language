import random

def computer():
    
    ch=["stone", "paper", "scissor"]               #using list
    
    computer_choice=random.choice(ch)
    print(computer_choice)
    user=input("Enter your choice:\nStone OR Paper OR Scissor\nInput: ")

    if(user.lower()==computer_choice):
        print("----Draw----")
        return "draw"
    elif(user.lower()=="stone" and computer_choice=="scissor") or \
        (user.lower()=="paper" and computer_choice=="stone") or \
        (user.lower()=="scissor" and computer_choice=="paper"):
        print("----Win----")
        return "user"
    else:
        print("----Lost----")
        return "lost"
        
    
# computer()

def calculate_score_computer():
    score=0
    n=int(input("How many times do you want to play: "))
    for i in range(1,n+1):
        print(f"\nRound No {i}")
        win=computer()
        if win=="user":
            score+=1
            print(f"\nYour current score is {score}")
    
    if (score>=((n//2)+1)):
        print("--------Finally user Win!!!--------")
    elif (win=="draw"):
        print("--------Completly Draw--------")
    else:
        print("--------Completly  lost!!--------")


calculate_score_computer()


