class A:

    def show(self,a):
        self.a = a
        print("Show from A, Value is : ",self.a)

class B(A):
    def show(self,b):
        self.b = b
        super().show(23)
        print("Show from B, Value is : ",self.b)

class C(B):
    def show(self,c):
        self.c = c
        super().show(78)
        print("Show from C, Value is : ",self.c)


obj = C()
obj.show(54)



