class Calculator:
    n=0

    @staticmethod
    def greet():
        print("Hello!")


    def info(khulii, n):
        khulii.n=n

        s=n**2
        c=n**3
        r=n**0.5

        print(f"Square:{s}\t Cube:{c}\t SquareRoot:{r}")

n=int(input("Enter Number: "))

obj=Calculator()
obj.greet()
obj.info(n)