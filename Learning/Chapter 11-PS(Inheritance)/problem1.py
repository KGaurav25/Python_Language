class twoDV:
    def twoD(self, i, j):
        self.i=i
        self.j=j
        print(f"{i}i+{j}j")

class threeDV(twoDV):
    def threeD(self, k):
        super().twoD(2,3)
        print(f"{self.i}i+{self.j}j+{k}k")

# obj=twoDV()
# obj.twoD(2,3)
obj=threeDV()
obj.threeD(4)