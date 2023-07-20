########  Write a Python function that takes two lists and returns true if they have at least one common member.  #####



def common(l1,l2):
    result = False
    for i in l1:
        for j in l2:
            if i == j:
                result = True
                return result
print(common([1,2,3,4,5], [5,6,7,8,9]))
print(common([12,34,56,23],[67,78,90,32]))
print(common([87,96,90,54],[96,8,62,5]))
