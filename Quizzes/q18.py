#!/usr/bin/python3

def insert_five(num):
	""" Replace one digit with 5 to achieve highest number """    
	num_str = str(num)
    
	is_negative = num_str[0] == '-'
    
	if is_negative:
		num_str = num_str[1:]
    
	for i in range(len(num_str)):
		digit = num_str[i]
		if is_negative:
			if digit > '5':
				num_str = num_str[:i] + '5' + num_str[i+1:]
				break
		else:
			if digit < '5':
				num_str = num_str[:i] + '5' + num_str[i+1:]
				break
    
	if is_negative:
		num_str = '-' + num_str
    
	return int(num_str)


if __name__ == "__main__":
	print(f"0 --> Highest number found after inserting '5': {insert_five(0)}")
	print(f"99999 --> Highest number found after inserting '5': {insert_five(99999)}")
	print(f"13579 --> Highest number found after inserting '5': {insert_five(13579)}")
	print(f"79531 --> Highest number found after inserting '5': {insert_five(79531)}")
	print(f"-3564 --> Highest number found after inserting '5': {insert_five(-3564)}")
	print(f"-9999 --> Highest number found after inserting '5': {insert_five(-9999)}")
	print(f"-407 --> Highest number found after inserting '5': {insert_five(-407)}")
	print(f"100000 --> Highest number found after inserting '5': {insert_five(200000)}")
