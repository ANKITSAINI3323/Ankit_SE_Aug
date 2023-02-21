# 5). Write a Python program to read last n lines of a file. 

f = open("5).Readlastline.txt","r")

lines = f.read().splitlines()

print(lines)
print(lines[-1])