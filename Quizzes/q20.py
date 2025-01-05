#!/usr/bin/python3

def roman_to_decimal(roman_num):
	""" Function converts roman number to decimal system """
	rom_dec = {
		"I":1,
		"V":5,
		"X":10,
		"L":50,
		"C":100,
		"D":500,
		"M":1000
	}

	dec_num = 0
	i = 0

	while i < len(roman_num):
		char1 = rom_dec.get((roman_num[i]))

		if (i+1 < len(roman_num)):
			char2 = rom_dec.get((roman_num[i+1]))

			if (char1 >= char2):
				dec_num += char1
				i += 1
			else:
				dec_num += char2 - char1
				i += 2
		else:
			dec_num += char2
			i += 1

	return dec_num


if __name__ == "__main__":
	print("IX in decimal system is:", roman_to_decimal("MCMXLVIII"))
