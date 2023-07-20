
######### Write a Python program to find the second smallest number in a list  ########


def find_second_smallest(l1):
    smallest = min(l1)
    l1.remove(smallest)
    second_smallest = min(l1)
    return second_smallest

l1 = [12,34,56,32,21,4,15]
print(find_second_smallest(l1))
