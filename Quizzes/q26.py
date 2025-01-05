#!/usr/bin/python3

def is_pangram(string):
	""" Function return true if given string is pangram """
	string = string.lower()
	
	alphabet = {
		'a' : 0, 
		'b' : 0, 
		'c' : 0, 
		'd' : 0, 
		'e' : 0, 
		'f' : 0, 
		'g' : 0, 
		'h' : 0, 
		'i' : 0, 
		'j' : 0, 
		'k' : 0, 
		'l' : 0, 
		'm' : 0, 
		'n' : 0, 
		'o' : 0, 
		'p' : 0, 
		'q' : 0, 
		'r' : 0, 
		's' : 0, 
		't' : 0, 
		'u' : 0, 
		'v' : 0, 
		'w' : 0, 
		'x' : 0, 
		'y' : 0, 
		'z' : 0
	}
	
	for letter in string:
		if letter in alphabet:
			alphabet.update({letter: alphabet.get(letter)+1})
			
	if 0 in alphabet.values():
		return False
	return True
	
def is_pangram2(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in string.lower():
            return False
    return True


if __name__ == "__main__":
	string1 = "the quick brown fox jumps over the lazy dog"
	string2 = "abcdefghijklmnopqrstuvwxyz"
	string3 = "abcdefghijklmnopqrstuvwxy"
	print(is_pangram(string1))
	print(is_pangram(string2))
	print(is_pangram(string3))
	
	print(is_pangram2(string1))
	print(is_pangram2(string2))
	print(is_pangram2(string3))
