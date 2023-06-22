### Write a Python program to count the number of characters (character frequency) in a string ###


s=input("Enter a string:")
char =0

for i in s:
    if i.isalpha():
        char+=1
print("Total char: ",char)
