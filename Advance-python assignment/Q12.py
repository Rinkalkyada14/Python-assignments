#Write a Python program to read first n lines of a file.
def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = []
            for _ in range(n):
                line = file.readline().strip()
                if not line:
                    break
                lines.append(line)
            return "\n".join(lines)
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

file_name = input("Enter the name of the text file: ")
num_lines = int(input("Enter the number of lines to read: "))

first_n_lines = read_first_n_lines(file_name, num_lines)

print(f"First {num_lines} lines of the file:")
print(first_n_lines)
