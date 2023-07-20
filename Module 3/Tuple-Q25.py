#####   Write a Python function to check whether a number is in a given range   ########

def test(n):
    if n in range(2,9):
        print(" %s is in the range"%str(n))
    else:
        print("The number is outside the given range.")
test(15)
