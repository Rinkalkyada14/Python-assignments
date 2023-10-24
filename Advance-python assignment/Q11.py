#Write a Python program to read a file line by line store it into a variable.
def read_file_to_variable(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

file_name = input("Enter the name of the text file: ")

file_content = read_file_to_variable(file_name)

print("File content stored in a variable:")
print(file_content)
