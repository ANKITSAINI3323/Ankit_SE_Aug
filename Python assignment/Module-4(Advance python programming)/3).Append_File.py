# 3). Write a Python program to append text to a file and display the text.

f = open("3).Myfile1.txt","a")

name = input("Enter Anything Here : ")
f.write("\n"+name)

f.close()