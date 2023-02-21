# 12). Write a Python program to copy the contents of a file to another file.

f1 = open("12).file.txt","r")
f2 = open("12).file1.txt","w")

for line in f1:
    f2.write(line)  