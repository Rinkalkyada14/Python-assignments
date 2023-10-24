#Write a Python program to count the number of lines in a text file.
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

file_name = input("Enter the name of the text file: ")

num_lines = count_lines(file_name)

if isinstance(num_lines, int):
    print(f"Number of lines in the file: {num_lines}")
else:
    print(num_lines)
