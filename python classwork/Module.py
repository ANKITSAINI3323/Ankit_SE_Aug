import UDF

while True:
    print("*"*50)
    print("Press 1. for Finding Maximum of Two Numbers")
    print("Press 2. for Finding Maximum of Three Numbers")
    print("Press 3. for Finding Even Odd. Number")    
    print("Press 4. for Exiting the Application")
    print("*"*50)

    choice = int(input("Enter your choice ? "))

    if choice==1:
        a = int(input("Enter A : "))
        b = int(input("Enter B : "))
        UDF.MaxofTwo(a,b)
    elif choice==2:
        a = int(input("Enter A : "))
        b = int(input("Enter B : "))
        c = int(input("Enter C : "))
        UDF.MaxofThree(a,b,c)
    elif choice==3:
        a = int(input("Enter Value : "))
        UDF.EvenOdd(a)
    else:
        break













        
        
