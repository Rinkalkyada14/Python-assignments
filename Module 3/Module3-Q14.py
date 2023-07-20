#####   Write a Python function that takes a list and returns a new list with unique elements of the first list   ######

l2 = []
l3 = []
n = int(input("Enter the number of element: "))

for i in range (0,n):
    ele = int(input())
    l2.append(ele)
print("l2 = ",str(l2))

for i in l2:
    if i not in l3:
        l3.append(i)

print("l3 = ",str(l3))
