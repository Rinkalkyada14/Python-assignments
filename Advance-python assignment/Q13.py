#Write a Python program to read last n lines of a file.
def read_last_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if n >= len(lines):
                return "".join(lines)
            else:
                return "".join(lines[-n:])
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

file_name = input("Enter the name of the text file: ")
num_lines = int(input("Enter the number of lines to read: "))

last_n_lines = read_last_n_lines(file_name, num_lines)

print(f"Last {num_lines} lines of the file:")
print(last_n_lines)
