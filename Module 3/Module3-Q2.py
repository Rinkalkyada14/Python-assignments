############  Write a Python function to get the largest number, smallest num and sum of all from a list.  ############


l = [12,13,14,15,22,23,24,25]
largest_number =0
Smallest_number = 100

for i in l:
    for j in l:
        if i<Smallest_number:
            if j>largest_number:
                Smallest_number = i
        largest_number = j
        
print(Smallest_number)
print(largest_number)
print(sum(l))
