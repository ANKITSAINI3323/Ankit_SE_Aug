class Length:

    def getVal(self,l):
        self.l = l

class Square(Length):

    def sqr(self):
        return self.l*self.l

class Cube(Length):

    def cub(self):
        return self.l*self.l*self.l



sq = Square()
n1 = int(input("Enter No. for Square : "))
sq.getVal(n1)
val1 = sq.sqr()
print("Square is : ",val1)

c = Cube()
n2 = int(input("Enter No. for Cube : "))
c.getVal(n2)
val2 = c.cub()
print("Cube is : ",val2)















        
