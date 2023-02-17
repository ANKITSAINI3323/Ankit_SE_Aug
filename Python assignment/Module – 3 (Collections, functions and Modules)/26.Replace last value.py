# 1). Write a Python program to replace last value of tuples in a list.

l1 = [("vishvam","Saini","krish"), ("monika","kaushal","mohit"), ("gorav","rakesh","rahul")]
print(l1)

print([t[:-1] + ("Ankit",) for t in l1])