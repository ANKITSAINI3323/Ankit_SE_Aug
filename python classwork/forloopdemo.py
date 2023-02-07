"""
for i in range(10):
    print(i)

1) Sum of N nos.

n = int(input("Enter N "))
sum=0
for k in range(1,n+1):
    sum=sum+k
    #print(k)

print("Sum : ",sum)
"""
n = int(input("Enter N "))
evensum=0
oddsum=0


for i in range(1,n+1):
    if i%2==0:
        evensum=evensum+i #6
    else:
        oddsum=oddsum+i     #9
    
    #print(i)
print("Even Sum = ",evensum)
print("Odd Sum = ",oddsum)




















    
