# 10). Write a Python program to count the frequency of words in a file.

count = 0

f = open("10).countFrequencyofwords.txt","r")

for line in f:
    word = line.split()
    count += len(word)

print("Total Number Of Words : ", count)