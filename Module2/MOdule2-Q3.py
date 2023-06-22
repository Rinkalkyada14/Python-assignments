### Write a Python program to get the Fibonacci series of given range. ###


a,b=0,1
print("Fibonacci series:")
for i in range(1,20):
    a,b=a+b,a
    print(a+b, end=" ")
    
