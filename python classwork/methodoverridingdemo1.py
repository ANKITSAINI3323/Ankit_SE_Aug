class A:

    def show(self,a):
        self.a = a
        super().show(41)
        print("Show from A, Value is : ",self.a)

class B:
    def show(self,b):
        self.b = b        
        print("Show from B, Value is : ",self.b)

class C(B,A):
    def show(self,c):
        self.c = c
        super().show(54)
        print("Show from C, Value is : ",self.c)


obj = C()
obj.show(34)

