"""
    File Handling:

    There are 3 basic operations in any file.

    1) Write         w
    2) Read          r
    3) Append        a
    4)Read/Write     w+

    

    Notepad file is used in all the other O.S

s="Write Demo"
print(s)
print("*"*50)

file = open("tops.txt","w")
file.write("This is File Write Demo ")
#print("File written successfully")
file.close()

s="Read Demo"
print("*"*50)
file=open("tops.txt","r")
print(file.read())
file.close()
"""
s = "Append Demo"
print(s)
print("*"*50)
file = open("tops.txt","a")
file.write("\nNow this is Appended Data")
file = open("tops.txt","r")
print(file.read())
file.close()




















