# 1). Write a Python program to unzip a list of tuples into individual lists. 

# Create a tuple :

l1 = [(1,2), (3,4), (9,8)]

print(list(zip(*l1)))


def unzip_list(lst_of_tuples):
    transposed = zip(*lst_of_tuples)
    return [list(i) for i in transposed]

lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
unzipped_lst = unzip_list(lst)

print(unzipped_lst)
