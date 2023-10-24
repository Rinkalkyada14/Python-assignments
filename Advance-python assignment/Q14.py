#Write a Python program to write a list to a file.
def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(item)
                file.write('\n')
        return "List written to file successfully."
    except Exception as e:
        return f"An error occurred while writing to the file: {e}"

data_list = ["apple", "banana", "orange", "grape", "kiwi"]
file_name = input("Enter the name of the text file: ")

result = write_list_to_file(file_name, data_list)

print(result)
