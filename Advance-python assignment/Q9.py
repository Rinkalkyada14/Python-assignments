#Write a Python program to read an entire text file.
def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

file_name = input("Enter the name of the text file: ")
file_content = read_text_file(file_name)
print("File Content:")
print(file_content)
