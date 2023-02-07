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

class C(A):
    def getC(self,c):
        self.c = c

    def putC(self):
        print("C : ",self.c)

class D(B,C):
    def getD(self,d):
        self.d = d

    def putD(self):
        print("D : ",self.d)


obj1 = D()

obj1.getA(20)
obj1.getB(30)
obj1.getC(40)
obj1.getD(50)

obj1.putA()
obj1.putB()
obj1.putC()
obj1.putD()


















        
    
