#Write a Python program to append text to a file and display the text.
def append_to_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text)
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

file_name = input("Enter the name of the text file: ")
append_text = input("Enter the text to append: ")

append_to_file(file_name, append_text)
file_content = read_text_file(file_name)

print("Updated File Content:")
print(file_content)

