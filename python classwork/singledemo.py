
class A:
    fname=""
    lname=""
    n=0

    def getA(self,a):
        self.a =a

    def putA(self):
        print("A : ",self.a)

    def acceptDetails(self,f,l):
        self.fname = f
        self.lname = l

    def evenOdd(self,val):
        self.n = val
        if self.n%2==0:
            print("Is Even ")
        else:
            print("Is Odd")
        

class B(A):

    def getB(self,b):
        self.b = b

    def putB(self):
        print("B : ",self.b)

    def showDetails(self):
        print("First Name : ",self.fname)
        print("Last Name : ",self.lname)

n1 = int(input("Enter A : "))
n2 = int(input("Enter B : "))

fname = input("Enter First Name : ")
lname = input("Enter Last Name : ")
monika = int(input("Enter No."))

obj2 = B()
obj2.getA(n1)
obj2.getB(n2)
obj2.acceptDetails(fname,lname)

obj2.putA()
obj2.putB()
obj2.showDetails()
obj2.evenOdd(monika)















