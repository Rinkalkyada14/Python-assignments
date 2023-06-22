
### Write a Python function that takes a list of words and returns the length of the longest one. ###


l = ['RInkal','Smit','RInkalKyada','SmitPatel','SmitKyada','JayrathPatel']
print(len(l))
length = 0
for j in l:
    if len(j)>length:
        length = len(j)
print("max length is", length)

