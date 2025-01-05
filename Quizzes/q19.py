#!/usr/bin/python3

def sort_colors(colors):
	""" Sort list with "green" at the beginning, "red" at the end """
	order = {'green': 0, 'yellow': 1, 'red': 2}
	return sorted(colors, key=lambda x: order.get(x, 3))
	

if __name__ == "__main__":
	colors = ['yellow', 'green', 'red', 'yellow', 'red', 'green']
	print(sort_colors(colors))
