###########  Write a Python program to check whether a list contains a sub list   ########

l1 = [12,23,43,121,54,67]

#l1.insert(3,[3,42,78])
#print(l1)

      
l2 = [87,90,12]

if (all(i in str(l1) for i in str(l2))):
    print("Sublist is present")
else:
    print("Sublist is not present")
