import os
import re

def find_word(start_path, word):
	""" Find given word in all files in filesystem and print matched file names """
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    
    for root, dirs, files in os.walk(start_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', errors='ignore') as file:
                    if any(pattern.search(line) for line in file):
                        print(file_path)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")


if __name__ == "__main__":
    word = input("Enter the word to search for: ")
    path = '/' 
    find_word(path, word)
