###### Write a Python script to check if a given key already exists in a dictionary  #########

a = {'A': 100, 'B': 200, 'C':300,'D': 20}
i = 'A'

if i in a:
    print("Key present,", end=" ")
    print("value is=",a[i])
else:
    print("not present")
