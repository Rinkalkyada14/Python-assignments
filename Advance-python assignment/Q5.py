#Write a Python program to count the frequency of words in a file.
from collections import Counter
import string

def count_word_frequencies(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            words = content.split()
            words = [word.strip(string.punctuation) for word in words]
            word_count = Counter(words)
            return word_count
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

file_name = input("Enter the name of the text file: ")

word_frequencies = count_word_frequencies(file_name)

if isinstance(word_frequencies, Counter):
    print("Word frequencies in the file:")
    for word, count in word_frequencies.items():
        print(f"{word}: {count}")
else:
    print(word_frequencies)
