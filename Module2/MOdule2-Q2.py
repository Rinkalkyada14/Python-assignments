### Write a Python program to get the Factorial number of given number. ###

n=int(input("Enter any number:"))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print("Factorial of given number is:", fact)
   
