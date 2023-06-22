###  Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. ###


a= int(input("Enter any number:"))
b= int(input("Enter any number:"))
c= int(input("Enter any number:"))
D = a+b+c
if a==b or a==c or b==c:
    print("D: 0")
else:
    print(D)
