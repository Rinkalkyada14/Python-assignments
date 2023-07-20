#########   Write a Python program to remove an empty tuple(s) from a list of tuples.  #############


l = [(12,23,'a','rinkal',4),(),(23,45,'s'),(5,76)]
for i in l:
    if len(i)== 0:
        l.remove(i)
        print(l)
       # print("empty tuple from list:",i)
