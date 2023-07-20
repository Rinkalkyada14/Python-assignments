########   Write a Python program to find the repeated items of a tuple.   #######


t1 = (12,23,45,1.1,True,'Rinkal','s','a',12,23,'python',1.1)
l = []
for i in t1:
    #print(i)
   # print(t1.count(i))
    if t1.count(i) > 1:
        l.append(i)
print(tuple(l))
