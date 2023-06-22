### Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. ###


s="Royispoormanbutheisnotgreedysoallpoorpeopleisnotbadnotlikeraju"

s1= s[:5]+"good"+s[5+4:]
print(s1[:19]+"good"+s[19+3:])
