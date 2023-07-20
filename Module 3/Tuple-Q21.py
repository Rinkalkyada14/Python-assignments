######### Write a Python program to find the highest 3 values in a dictionary #######


d = {"A":12,"B":13,"C":9,"D":89,"E":34,"F":17,"G":65,"H":36,"I":25,"J":11}

l = []

for i in d.values():
    l.append(i)
    l.sort()

print("Highest value:",l[-1])
print("Second Highest value:",l[-2])
print("Third Highest value:",l[-3])
