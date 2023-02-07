class Sample:

    def common(self):
        n = int(input("Enter No."))
        print("Number : ",n)

    def common(self,a,b):
        self.a = a
        self.b = b
        
        if self.a>self.b:
            print(self.a," is Greater")
        else:
            print(self.b," is Greater")
    

s = Sample()

s.common()
