# 4). Write a Python program to read first n lines of a file.

f = open("4).Readfirstline.txt","r")

lines = f.read().splitlines()

print(lines)
print(lines[0])