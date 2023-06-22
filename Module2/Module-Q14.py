### Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. ###


s1=("Rinkal Kyada-Embedded engineer")
s2=("Smit patel-Senior software engineer")

s=s1.replace(s1[:2],s2[:2])+ " " +s2.replace(s2[:2],s1[:2])
print(s)
