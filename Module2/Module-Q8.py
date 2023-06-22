###  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. ###


a = int(input("Enter a interger:"))
b= int(input("Enter b interger:"))
c = a+b
d = a-b
if a==b or c==5 or d==5:
    print("True")
else:
    print("False")
