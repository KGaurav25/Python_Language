import random
class game:

    def greet(self):
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

    def level(self):
        print("""\nSelect the level:
                    Press:
                    1:For Easy
                    2:For Modrate  
                    3:For Hard""")
        lev=int(input("Enter your Choice: "))

        if lev==1:
            list=[]
            for i in range(0, 51):
                list.append(i)
            num=random.choice(list)
            self.l=50

            return num 
        elif lev==2:
            list=[]
            for i in range(0, 101):
                list.append(i)
            num=random.choice(list)
            self.l=100

            return num 
        elif lev==3:
            list=[]
            for i in range(0, 1001):
                list.append(i)
            num=random.choice(list)
            self.l=1000

            return num 
        else:
            print("-----Invalid Choice-----")

    def choice(self):
        self.num=num

        ch=0
        guess=0
        while ch!=num:
            
            # print(" "*(guess), end="")
            ch=int(input(f"\nPlease Enter the num between 0 to {self.l} \nEnter your num: "))
            if ch<(self.l):
                guess=guess+1
                if ch>num:
                    print("Enter the lower number!")
                elif ch<num:
                    print("Enter the higher number!")
                else:
                    print(f"\nCongratulations!!!\nYour number is matches with computer numeber\nYou Guess the number in {guess}")
                
                print(f"Guess Times: {guess}")
            else:
                print("Invalid number!!!")
    
obj=game()
obj.greet()
num=obj.level()
obj.choice()
