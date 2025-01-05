#!/usr/bin/python3
def is_sum_found(lst, sum):
	""" Return 1 if two numbers in list adds up to given sum and print their indexes """
	for x in lst:
		if sum - x in lst:
			print(lst.index(x), "&", lst.index(sum-x))
			return 1
	return 0
	
	
numbers=[2,4,7,12,14]
print(is_sum_found(numbers, 21))
