'''s=input("Enter a string:")

upper = 0
lower =0
char =0
space=0
digit =0

for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    if i.isalpha():
        char+=1
    elif i.isnumeric():
        digit+=1
    elif i.isspace():
        space+=1

print("Total upper: ",upper)
print("Total lower: ",lower)
print("Total char: ",char)
print("Total digit: ",digit)
print("Total space: ",space)
print(len(s))
'''



'''s = ("Rinkal Kyada@123")
if len(s)%4 == 0:
    print(s[::-1])
else:
    print(s)'''


#*************************************************************************************************************************

'''s = "Write a python program to find"

s1 = s[:2:1] + s[28:]
if len(s1)<2:
    print(s1)'''
'''
l=[2,33,222,14,25]
print(l[-1])
'''



'''l1 = [12, 23, 45, 67, 7, 67, 32, 45, 78, 98, 87]
l2 = str(l1)
l3 = []
print(l2)
for i in l1:
    if i not in l3:
        l3.append(i)

print(str(l3))'''




'''l1 = []
l2 = []
n = int(input("Enter the  number of elemenbt: "))

for i in range (0,n):
    ele = int(input())
    l1.append(ele)
x = str(l1)

for i in l1:
    if i not in l2:
        l2.append(i)
print(str(l2))'''




#*******************************Tuple************************************************

'''t = ('a',12,22,'smit',True,1.23)
print(t)'''

'''t = (12,23,43,45,67,89)
print(t)'''


'''t = ('a','smit','r','as')
print("".join(t))'''


'''t = ('a',12,23,'python',True,1.1)
print(len(t))'''


'''t = ('a',12,23,'python',1.1)
print(t.count(12))'''


'''l = [12,23,45,'1.1',True,'Rinkal','s']
t = tuple(l)
print(t)'''


'''t = (12,23,45,'1.1',True,'Rinkal','s')

print(t[::-1])'''



'''t = (2,23,45,'1.1',True,'Rinkal','s')
print(len(t))
l = []
for i in t[6]:
    l.append(i)
    print(l)'''


'''t1 = (12,23,45,1.1,True,'Rinkal','s','a',12,23,'python',1.1)
l = []
for i in t1:
    #print(i)
    print(t1.count(i))
    if t1.count(i) > 1:
        l.append(i)
print(tuple(l))

oooooRRRRRR'''

'''t1 = (12,23,45,1.1,True,'Rinkal',12,'a',12,23,'python',12)
print(t1.count(12))'''


'''l = [(12,23,'a','rinkal',4),(),(23,45,'s'),(5,76)]
for i in l:
    if len(i)== 0:
        print("empty tuple from list:",i)'''



'''l = [(12,23,4),(32,45,5),(5,76,45)]
print(list(zip(*l)))'''



'''l = [(12,34),(11,5),(78,43)]
print(dict(l))'''



'''t = (('a',12),('b',23),('c',14),('d',56))
#x = list(t)
#print(x)
print(dict(t))'''


'''from collections import Counter

d1 = Counter({'a': 100, 'b': 200, 'c':300})
d2 = Counter({'a': 300, 'b': 200, 'd':400})

d = d1 + d2
print(d)'''


'''d1 = {'a': 100, 'b': 200, 'c':300}

for i in d1:
    print(i,"=",d1.get(i))'''


'''d1 = {'a': 100, 'b': 200, 'c':300,'x': 20}
i = 'g' and 'a'

if i in d1:
    print("Key present,", end=" ")
    print("value is=",d1[i])
else:
    print("not present")'''



'''d1 = {1:'Rinkal',2:'janvi',3:'mansi'}
d2 = {4:'khushi',5:'pinal',6:'pari'}
d3 = d1.copy()
d3.update(d2)
print(d3)'''


'''a = {'A': 100, 'B': 200, 'C':300,'D': 20}
i = 'A'

if i in a:
    print("Key present,", end=" ")
    print("value is=",a[i])
else:
    print("not present")'''



'''d = {}

for i in range(1,16):
   d[i] = i**2
print(d)'''



'''k = ['Rinkal','smit','krina']
v = [4703,2306,2345]
d = dict(zip(k,v))
print(d)'''

    

    
student = {
  'name': 'Ram',
  'age': 23,
  'city': 'Salem'
}
print(type(student.keys()))
print(student.keys())
print(student.keys() >= {'age', 'name'})
print(student.keys() >= {'name', 'city', 'age'})
print(student.keys() >= {'city', 'Salem'})




    


    

















