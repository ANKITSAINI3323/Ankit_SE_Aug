import random

data = open("data.txt","w")
for i in range(10):
    num = random.randint(1,999)
    data.write(str(num)+" ")
data.close()

data = open("data.txt","r")
even = open("even.txt","w")
odd = open("odd.txt","w")
s = data.read().split(" ")[:-1]
print(s)
#print(type(s))

for i in s:
    #print(type(int(i)))
    if int(i)%2==0:
        even.write(i+" ")
    else:
        odd.write(i+" ")

even.close()
odd.close()
data.close()

data = open("data.txt","r")
print("Data File Content")
print("*"*50)
print(data.read())
data.close()
print("*"*50)

even = open("even.txt","r")
print("Even Content")
print("*"*50)
print(even.read())
even.close()
print("*"*50)

odd = open("odd.txt","r")
print("Odd Content")
print("*"*50)
print(odd.read())
odd.close()
print("*"*50)













