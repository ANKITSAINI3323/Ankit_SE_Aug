"""
    Exception : An Abnormal situation  that raises during the
                Runtime of your program is called Exception.

                It will stop the program, when the exception is generated.

                Exception is the predefined class.


    To handle Exception ,there are 4 keywords.

    1) try
    2) except
    3) else
    4) finally.


    try : it is a block.

        e.g  try
                statement

          -it will never be alone,it will have either except/finally.
          -it can have more than 1 except block

    finally : it is a block.

             - it will be executed anyhow, even if the exception is
               generated or not


Demo1)

a = int(input("Enter A : "))
b = int(input("Enter B : "))
div = a/b
print("Division : ",div)


Demo2)
try:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    div = a/b
    print("Division : ",div)

except Exception:
    print("Exception Caught")

    
    
except ZeroDivisionError:
    print("Exception Caught")
except ValueError:
    print("Exception Caught")
"""

while True:
    try:
        n= input("Enter Integer Value Only : ")
        n = int(n)
        break
    except Exception:
        print("Invalid Input")
    finally:
        print("Finally Called")

print("Bye")
        
















