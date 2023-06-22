### Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. ###


s = "Write a python program to find"
s1 = s[:2:1] + s[28:]
#print(s1)

if len(s1) < 2:
    s1 = s[:2:1] + s[28:]
    print(s1)

