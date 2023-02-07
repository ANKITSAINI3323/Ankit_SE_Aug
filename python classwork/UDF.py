def MaxofTwo(a,b):
    if a>b:
        print(a," is Max")
    else:
        print(b," is Max")

def MaxofThree(a,b,c):
    if a>b:
        if a>c:
            print(a," is Greater")
        else:
            print(c," is Greater")
    else:
        if b>c:
            print(b," is Greater")
        else:
            print(c," is Greater")

def EvenOdd(a):
    if a%2==0:
        print(a," is Even")
    else:
        print(a," is Odd")
