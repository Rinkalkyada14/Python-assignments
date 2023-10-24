#Write a Python program to copy the contents of a file to another file.
def copy_file(source_filename, destination_filename):
    try:
        with open(source_filename, 'r') as source_file:
            content = source_file.read()
            with open(destination_filename, 'w') as destination_file:
                destination_file.write(content)
        return "File copied successfully."
    except FileNotFoundError:
        return "Source file not found."
    except Exception as e:
        return f"An error occurred while copying the file: {e}"

source_file_name = input("Enter the name of the source file: ")
destination_file_name = input("Enter the name of the destination file: ")

result = copy_file(source_file_name, destination_file_name)

print(result)
