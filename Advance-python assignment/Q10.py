#Write a Python program to read a file line by line and store it into a list.
def read_file_to_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        return ["File not found."]
    except Exception as e:
        return [f"An error occurred while reading the file: {e}"]

file_name = input("Enter the name of the text file: ")

lines_list = read_file_to_list(file_name)

print("File content stored in a list:")
for line in lines_list:
    print(line.strip())  
