### Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. ###



s=input("Enter a string:")
if s.endswith("ing"):
    print(s.replace("ing","ly"))
elif len(s)==3:
    print(s,"ing")
else:
    print(s)
    
