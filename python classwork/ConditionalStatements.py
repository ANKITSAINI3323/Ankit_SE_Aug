"""
1) Simple if

    if condition:
        statement

2) if/else

    if condition:
        statement
    else:
        statement

3) Nested if/else

    if condition:
        if condition:
            statement
        else:
            statement
    else:
        if condition:
            statement
        else:
            statement

4) Ladder if/else:

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    elif condition:
        statement

    


a = -20

if a>0:
    print(a,"is +ve")

n  = int(input("Enter N : "))
#print(type(n))

if n%2==0:
    print(n," is Even")
else:
    print(n," is Odd")




n1 = int(input("Enter N1 "))
n2 = int(input("Enter N2 "))

if n1>n2:
    print(n1," is Greater")
else:
    print(n2," is Greater")




n1 = int(input("Enter A : "))
n2 = int(input("Enter B : "))
n3 = int(input("Enter C : "))

print("A = ",n1," B = ",n2," C = ",n3)

if n1>n2:
    if n1>n3:
        print(n1," is Greater")
    else:
        print(n3," is Greater")
else:
    if n2>n3:
        print(n2," is Greater")
    else:
        print(n3," is Greater")

"""

roll = int(input("Enter Roll No : "))
name = input("Enter your Name : ")
p = int(input("Enter Physics Marks : "))
c = int(input("Enter Chemistry Marks : "))
m = int(input("Enter Maths Marks : "))
tot = p+c+m
per = tot/3
#print("**************************")
print("*"*50)
print("Roll No : ",roll)
print("Name : ",name)
print("Total : ",tot)
print("Percentage : ",per)
print("Grade is ",end="")

if per>=75:
    print("Distinction")
elif per>=60:
    print("A")
elif per>=50:
    print("B")
elif per>=40:
    print("C")
else:
    print("Fail")











































