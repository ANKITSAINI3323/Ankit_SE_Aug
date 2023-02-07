"""
    Function : It is a piece of code/set of code which
               performs some specific task is called
               a Function.

               Two Types of Functions.

               1) Predefined Functions.(Library functions)
               
               2) Userdefined Functions.

                   - A function which is created according to the
                     requirement of the user.

    UDF :

    Categories of Functions.

    1) A Function with No Arguments and no return value.
    2) A Function with Arguments and with no return value.
    3) A Function with Arguments and with return value.


    A Function can be defined with the def keyword.

    syntax:  def function_name():
                statement


    Important facts about function.

    Function Creation
    Function Calling



def Mohit():
    print("*"*50)

Mohit()
print("Welcome to Python Programming using UDF.")
Mohit()



def printstar():
    print("*"*80)

def add():
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    print("Before Swapping A = ",a," B = ",b)
    a,b = b,a
    print("After Swapping A = ",a," B = ",b)
    print("Addition : ",(a+b))

printstar()
add()
printstar()


def printstar():
    print("*"*80)

def add(a,b):
    printstar()
    print("A : ",a)
    print("B : ",b)
    print("Addition : ",(a+b))
    printstar()

n1 = int(input("Enter A : "))
n2 = int(input("Enter B : "))

add(n1,n2)
"""

def printstar():
    print("*"*80)

def add(a,b):
    printstar()
    print("A : ",a)
    print("B : ",b)
    printstar()
    return a+b

def evenOdd(n):
    print("Value is ",n)
    if n%2 ==0:
        print("Addition is Even No.")
    else:
        print("Addition is Odd No.")
    

n1 = int(input("Enter A : "))
n2 = int(input("Enter B : "))

no=add(n1,n2)
print("Addition : ",no)
evenOdd(no)





















