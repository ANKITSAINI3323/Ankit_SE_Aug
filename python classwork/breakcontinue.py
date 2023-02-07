
n = int(input("Enter Number :"))

for i in range(1,n+1):
    if i==5:
        break    
    print(i)


for i in range(1,n+1):
    if i==2 or i==8:
        continue
    print(i)
