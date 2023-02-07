class A:

    def getA(self,a):
        self.a = a

    def putA(self):
        print("A : ",self.a)

class B(A):

    def getB(self,b):
        self.b = b

    def putB(self):
        print("B : ",self.b)

class C(B):
    def getC(self,c):
        self.c = c

    def putC(self):
        print("C : ",self.c)
    

n1 = int(input("Enter A : "))
n2 = int(input("Enter B : "))
n3 = int(input("Enter C : "))

obj2 = C()
obj2.getA(n1)
obj2.getB(n2)
obj2.getC(n3)
obj2.putA()
obj2.putB()
obj2.putC()















