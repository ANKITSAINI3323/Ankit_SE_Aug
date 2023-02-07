class Student:

    def getName(self,n):
        self.name = n

class ExtraMarks:

    def sportsMarks(self,sp):
        self.sm = sp

class Result(Student,ExtraMarks):

    total = 0
    per = 0
  

    def getMarks(self,s1,s2,s3):
        self.phy = s1
        self.chem = s2
        self.maths = s3
        self.total = (self.phy+self.chem+self.maths+self.sm)
        self.per = self.total/4

    def displayDetails(self):
        print("Student Name : ",self.name)
        print("Total Marks : ",self.total)
        print("Percentage : ",self.per)


res = Result()
name = input("Enter your Name : ")
res.getName(name)
sp = int(input("Enter Sports Marks : "))
res.sportsMarks(sp)
p = int(input("Enter Physics Marks : "))
c = int(input("Enter Chemistry Marks : "))
m = int(input("Enter Maths Marks : "))

res.getMarks(p,c,m)
print()
print("*"*50)
res.displayDetails()






































            
    
