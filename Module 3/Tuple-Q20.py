#########     Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.   ##########


from itertools import product
a = {'1': ['a','b'], '2': ['c','d']}
for x ,y in product(*a.values()):
    print(x+y)
    
