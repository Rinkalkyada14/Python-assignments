#Write python program that user to enter only odd numbers, else will raise an exception.

def is_odd(number):
    return number % 2 != 0

def get_odd_input():
    while True:
        try:
            user_input = int(input("Enter an odd number: "))
            if is_odd(user_input):
                return user_input
            else:
                raise ValueError("Entered number is not odd.")
        except ValueError as e:
            print(f"Error: {e}. Please enter an odd number.")

odd_number = get_odd_input()
print(f"You entered an odd number: {odd_number}")
