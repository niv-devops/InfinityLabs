#!/usr/bin/python3

import os.path

def reverse_file(file_name):
	""" Function takes a file and return new file with reversed lines order """
	if not os.path.isfile(file_name):
		print(f"File {file_name} does not exists 👍")
		exit(1)
	
	with open(file_name) as file,  open('rev_file.txt', 'w') as rev_file:
		rev_file.writelines(reversed(file.readlines()))
	print(f"File {file_name} reversed successfully.")
	
	
if __name__ == "__main__":
	reverse_file('niv_q29_testfile.txt')
	reverse_file('niv_q30_testfile.txt')
