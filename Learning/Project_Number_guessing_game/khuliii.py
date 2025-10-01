import random

class game:
    @staticmethod
    def greet():
        print("-------W E L C O M E-----")
        print("""
            📘Rule Book
                    1.Guess the number between 1 and 100.

                    2.I’ll tell you if your guess is too high or too low.

                    3.Keep guessing until you get it right.

                    4.I’ll show you how many tries you took.

            Good luck! 🎯""")

    def number(self):
        list1=[ ]
        for i in range(0,101):
            list1.append(i)

        num=random.choice(list1)
        return num
    
    def choose(self,num,ch):
        self.num=num
        self.ch=ch
        if(ch==num):
            print("Congratulationssss !!")
        elif(ch>num):
            print("enter Small number ")
        elif(ch<num):
            print("Enter greater number")
        else:
            print("Invalid number")

obj=game()
obj.greet()
num=obj.number()
for i in range(0,3):
    ch=int(input("Enter your number : "))
    obj.choose(num,ch)

print(num)