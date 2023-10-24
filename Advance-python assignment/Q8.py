#Write a python program to find the longest words.
def find_longest_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            longest_length = max(len(word) for word in words)
            longest_words = [word for word in words if len(word) == longest_length]
            return longest_words
    except FileNotFoundError:
        return ["File not found."]
    except Exception as e:
        return [f"An error occurred while reading the file: {e}"]

file_name = input("Enter the name of the text file: ")

longest_words_list = find_longest_words(file_name)

if longest_words_list:
    print("Longest words in the file:")
    for word in longest_words_list:
        print(word)
else:
    print("No words found in the file.")
