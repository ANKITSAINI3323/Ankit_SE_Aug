
class Sample:

    x = 0       
    def __init__(self,f):
        self.x = f
        print()

    def demo(self):
        print("X : ",self.x)

    def evenOdd(self):
        if self.x%2==0:
            print("It is Even ")
        else:
            print("It is Odd")

n = int(input("Enter No. "))
obj = Sample(n)
obj.demo()
obj.evenOdd()














