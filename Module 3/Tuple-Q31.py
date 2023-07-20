########### Write a Python program to calculate surface volume and area of a cylinder  #######


pi = 22/7
h = float(input("Enter the height of cylinder:"))
r = float(input('radius of cylinder:'))

volume = pi*r*h
area = ((2*pi*r) * h) + ((pi*r**2)*2)
print("volume is:",volume)
print("Surface area is:", area)
