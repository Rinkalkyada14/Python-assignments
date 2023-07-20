##############   Write a Python function that takes two lists and returns true if they have at least one common member. ###########


l2 = []
l1 =[]
l3 = []
result = False
n = int(input("Enter the  number of elemenbt: "))

for i in range (0,n):
    ele = int(input())
    l1.append(ele)
print("l1 = ",str(l1))

for j in range(0,n):
    sec = int(input())
    l2.append(sec)
print("l2 = ",str(l2))

for i in l1:
    for j in l2:
        if i == j:
            result = True
print(result)
