print("Let's play 'Stone Paper Scissor'!!!\n")

import random
r=1
while r==1:
    a=int(input("\nDo you want to play with \n1:Computer\t OR \t2:User\n___Input: "))

    if a==1:
        def computer():
            
            ch=["stone", "paper", "scissor"]
            
            computer_choice=random.choice(ch)

            user=input("What is your choice \nIs it 'Stone' OR 'Paper' OR 'Scissor'???\n___Input: ")

            if(user.lower()==computer_choice):
                print("\n----Draw----")
                print(f"computer choice: {computer_choice}")
                return "draw"
            elif(user.lower()=="stone" and computer_choice=="scissor") or \
                (user.lower()=="paper" and computer_choice=="stone") or \
                (user.lower()=="scissor" and computer_choice=="paper"):
                print("\n!!!----Win----!!!")
                print(f"computer choice: {computer_choice}")
                return "user"
            elif(user.lower()in ch):
                print("\n!!!----Lost----!!!")
                print(f"computer choice: {computer_choice}")
                return "lost"
            else:
                print("\n!!!----Invalid----!!!")
                print(f"computer choice: {computer_choice}")
                return "invalid"
            
           
            
            
        # computer()

        def calculate_score_computer():
            score=0
            lost=0
            n=int(input("\nHow many times do you want to play: "))
            for i in range(1,n+1):
                print(f"\nRound No {i}")
                win=computer()
                if win=="user":
                    score+=1
                    print(f"\nYour current score is {score}")
                elif win=="lost":
                    lost+=1
                    
            
            if (score>lost):
                print("\n-----___!!!Finally user Win!!!___-----")
            elif (lost>score):
                print("\n-----___!!!Completly Lost!!!___-----")
            else:
                print("\n-----___!!!Completly  Draw!!!___-----")


        calculate_score_computer()

    elif a==2:
        def user():
            user1=input("USER 1 \nIs it 'Stone' OR 'Paper' OR 'Scissor'???\n___Input: ")
            user2=input("USER 2 \nIs it 'Stone' OR 'Paper' OR 'Scissor'???\n___Input: ")

            if (user1.lower()==user2.lower()):
                print("!!!---Its Draw---!!!")
            elif(user1.lower()=="stone" and user2.lower()=="scissor") or \
                (user1.lower()=="paper" and user2.lower()=="stone") or \
                (user1.lower()=="scissor" and user2.lower()=="paper"):
                print("!!!----User 1 Win----!!!")
                return "user1"
            else:
                print("!!!----User 2 Win----!!!")
                return "user2"
            
        def calu_score_user():
            scr_user1=0
            scr_user2=0
            n=int(input("\nHow many times do you want to play: "))

            for i in range(1,n+1):
                print(f"\nRound No {i}")
                win_user=user()
                if win_user=="user1":
                    scr_user1+=1
                elif win_user=="user2":
                    scr_user2+=1
                print(f"\nCurrent score of User_1 is {scr_user1} \nCurrent score of User_2 is {scr_user2}")
            
            if scr_user1>=(n//2)+1 or (scr_user1>scr_user2):
                print("\n-----___!!!User 1 Finally wins!!!___-----")
            elif scr_user2>=(n//2)+1 or (scr_user1<scr_user2):
                print("\n-----___!!!User 2 Finally wins!!!___-----")
            else:
                print("\n-----___!!!Completly  Draw!!!___-----")

        calu_score_user()

    else:
        print("Invalid choice!!")


    r=int(input("\n \nDo you want to play again\nIf 'Yes' press: 1\nOR \nIf 'No' prass anything\n___Input: "))
else:
    print("!!!---___Thank You___---!!!")

