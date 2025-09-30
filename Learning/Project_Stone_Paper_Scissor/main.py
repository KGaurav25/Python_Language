'''Stone paper scissor'''

def info():
    print("1: Stone")
    print("2: Paper")
    print("3: Scissor")

info()

ch1="Stone"
ch2=int(input("Enter your choice: "))

if ch2==2:
    print("You win")
elif ch2==3:
    print("You Lost")