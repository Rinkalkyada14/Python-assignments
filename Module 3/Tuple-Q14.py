##########   Write a Python program to combine two dictionary adding values for common keys   ###########


from collections import Counter

d1 = Counter({'a': 100, 'b': 200, 'c':300})
d2 = Counter({'a': 300, 'b': 200, 'd':400})

d = d1 + d2
print(d)
