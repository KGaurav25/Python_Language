class twoDV:
    def twoD(self, i, j):
        self.i=i
        self.j=j
        print(i,j)

class threeDV(twoDV):
    def threeD(self, k):
        # super().twoD(2,3)
        print(self.i, self.j, k)

obj=twoDV()
obj.twoD(2,3)
obj=threeDV()
obj.threeD(4)