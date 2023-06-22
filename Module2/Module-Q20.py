
### Write a Python function to insert a string in the middle of a string. ###

s = "python is a easy everyone can learn it easily"

insert_str = " language to learn "
print(len(s))
s = s[:22]+ insert_str +s[22:]
print(s)
