###########  Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30  ###########


l1 = []
for i in range(1,51):
    l1.append(i*i)
print(l1)
print((l1[0:5])+(l1[-5:]))
