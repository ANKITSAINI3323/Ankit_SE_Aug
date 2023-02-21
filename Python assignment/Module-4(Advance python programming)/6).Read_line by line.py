# 6).Write a Python program to read a file line by line and store it into a list.

f = open("6).Readlinebyline.txt","r")

lines = f.readlines()
print(lines)


lines = [x.strip() for x in lines]
print(lines)