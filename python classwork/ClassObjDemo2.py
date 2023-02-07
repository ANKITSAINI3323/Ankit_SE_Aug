
class Person:
    fname=""
    lname=""
    email=""
    

    def __init__(self,fname,lname,email,age):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.age = age

    def showDetails(self):
        print("First Name : ",self.fname)
        print("Last Name : ",self.lname)
        print("Email : ",self.email)
        print("Age : ",self.age)

f = input("Enter First Name : ")
l = input("Enter Last Name : ")
e = input("Enter Email : ")
a = int(input("Enter Age : "))
    
p = Person(f,l,e,a)
p.showDetails()













