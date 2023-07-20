##########   Write a Python program to remove duplicates from a list.   ########




l1 = [12, 23, 45, 67, 7, 67, 32, 45, 78, 78, 87]
l2 = str(l1)
l3 = []
#print(l2)
for i in l1:
    if i not in l3:
        l3.append(i)

print(str(l3))
