"""

In Python we have magic methods, which are automatically Called,
when we create or print the object.

"""

class Point:

    def __init__(self,x,y):
        print("Init Called")
        self.x = x
        self.y = y
        print(" X : ",x, ",Y = ",y)

    def __str__(self):
       print("str Called")
       return "[{0},{1}]".format(self.x,self.y)
    
    def __add__(self,obj):
        print("add called")
        x = self.x + obj.x
        y = self.y + obj.y
        return Point(x,y)

p1 = Point(10,20)
print(p1)           # object print
print("*"*50)
p2 = Point(30,40)
print(p2)
print("*"*50)
print(p1+p2)











    
