###### Write a Python program to unzip a list of tuples into individual lists.  ####


l = [(12,23,4),(32,45,5),(5,76,45)]
print(list(zip(*l)))
