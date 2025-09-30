print("Let's play 'Stone Paper Scissor' Madam ;)\n")

import random
r=1
while r==1:
    a=int(input("\nBola kas khelnar \n1:Computer brobar \t KA \t2:Mazya Brobar :)\nSanga kiii: "))

    if a==1:
        def computer():
            
            ch=["stone", "paper", "scissor"]
            
            computer_choice=random.choice(ch)

            user=input(":( Thik ahe Computer tar Computer  \nBola 'Stone' KA 'Paper' KA 'Scissor'???\nBola Bola Bola: ")

            if(user.lower()==computer_choice):
                print("\n___Draw Zali Kii___")
                print(f"Computer chi Nivad : {computer_choice}")
                return "draw"
            elif(user.lower()=="stone" and computer_choice=="scissor") or \
                (user.lower()=="paper" and computer_choice=="stone") or \
                (user.lower()=="scissor" and computer_choice=="paper"):
                print("\n____Jinklasa Nvh____:) :)")
                print(f"Computer chi Nivad : {computer_choice}")
                return "user"
            elif(user.lower()in ch):
                print("\n___Computer Jinkal Makdaa___:(")
                print(f"Computer chi Nivad :  {computer_choice}")
                return "lost"
            else:
                print("\n____As Khulya gat kai pan takaich nastai____=)")
                print(f"Computer chi Nivad : {computer_choice}")
                return "invalid"
            
           
            
            
        # computer()

        def calculate_score_computer():
            score=0
            lost=0
            n=int(input("\nKisat Dav Khelnar?? ;) "))
            for i in range(1,n+1):
                print(f"\nDav kramank {i}")
                win=computer()
                if win=="user":
                    score+=1
                    print(f"\nBgh Khulya atta parent kiti vela jinklas te {score} =)")
                elif win=="lost":
                    lost+=1
                    
            
            if (score>lost):
                print("\n!!!____Jinklas ki Makdaaa <3___!!! :)")
            elif (lost>score):
                print("\nEvdha kai vishai madam pudhchya veli iskatuya ;)")
            else:
                print("\n___Shevatch DRAW Kelasa nvh___")


        calculate_score_computer()

    elif a==2:
        def user():
            user1=input("Tumchii Paliii ;) \nBola 'Stone' KA 'Paper' KA 'Scissor'???\nBola Bola Bola: ")
            user2=input("Amchi Pa;iii \nTumhich sanga 'Stone' KA 'Paper' KA 'Scissor'???\nSanga sanga sanga: ")

            if (user1.lower()==user2.lower()):
                print("___Draw Zali Kii___")
            elif(user1.lower()=="stone" and user2.lower()=="scissor") or \
                (user1.lower()=="paper" and user2.lower()=="stone") or \
                (user1.lower()=="scissor" and user2.lower()=="paper"):
                print("____Tumhi Jinklasa Kiii___")
                return "user1"
            else:
                print("___Amhi jinklo Nvh___")
                return "user2"
            
        def calu_score_user():
            scr_user1=0
            scr_user2=0
            n=int(input("\nKisat Dav Khelaich?? ;) "))

            for i in range(1,n+1):
                print(f"\nDav kramank {i}")
                win_user=user()
                if win_user=="user1":
                    scr_user1+=1
                elif win_user=="user2":
                    scr_user2+=1
                print(f"\nSadhyach Tumch GUN bgha madam ;) {scr_user1} \nAni amcha pan GUN bagha ;) {scr_user2}")
            
            if scr_user1>=(n//2)+1 or (scr_user1>scr_user2):
                print("\n____Jinklas ki khulyaaaa <3___:)")
            elif scr_user2>=(n//2)+1 or (scr_user1<scr_user2):
                print("\n___Yanda amhi jinkalo___;)")
            else:
                print("\n___DRAW zala nvh___")

        calu_score_user()

    else:
        print("Kahi pan takaich nastis Khuliii")


    r=int(input("\n \nAni ekda khelaicha kai madam\n'Hoi' tar mg 1 Dab\nOR \n'Nahi' tar kahi pan dab ;) \nKahi tari dab pan "))
else:
    print("Bass zal Makda!!!\nEvdh khelaich nastai ;)")

