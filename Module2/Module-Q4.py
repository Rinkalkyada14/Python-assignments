###  Write python program that swap two number with temp variable and without temp variable. ###


'''(With temp)
a = 23
b = 34
temp = 0
temp = b
a,b=temp,a
print("A:",a,"B:",b)'''


#(Without temp)
a = 23
b = 34
a,b = b,a
print("A:",a,"B:",b)
