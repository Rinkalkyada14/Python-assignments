########   Write a Python program to returns sum of all divisors of a number #########


def div(number):
    divi = [1]
    for i in range(2, number):
        if (number % i)==0:
            divi.append(i)
    return sum(divi)
print(div(8))
print(div(12))
