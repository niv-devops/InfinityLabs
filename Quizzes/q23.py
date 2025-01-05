#!/usr/bin/python3

def is_empty(landing, takeoff):
	""" Function gets two lists of planes tail numbers
	    The function return string indicating if the field is empty
	    or it will return the tail num of the only plane left """
	    
	count_occur = {}

	for plane in landing:
		if plane in count_occur:
			count_occur[plane] += 1
		else:
			count_occur[plane] = 1
    
	for plane in takeoff:
		if plane in count_occur:
			count_occur[plane] -= 1
			if count_occur[plane] == 0:
				del count_occur[plane]
    
	if not count_occur:
		return "Field is empty."
	else:
		remaining_plane = list(count_occur.keys())[0]
		return f"One plane left at the field: {remaining_plane}."
		
		
def is_empty2(plane_lst):
	""" Function gets one list of planes tail numbers
		The function return string indicating if the field is empty
		or it will return the tail num of the only plane left """
		
	count_occur = {}
	
	for plane in plane_lst:
		if plane in count_occur:
			count_occur[plane] += 1
		else:
			count_occur[plane] = 1

	for plane in plane_lst:
		if count_occur[plane] % 2 == 1:
			return f"One plane left at the field: {plane}."
	return "Field is empty."


if __name__ == "__main__":
	landing = [1234, 5678, 1357, 5678]
	takeoff = [5678, 1234, 1357]
	planes = [1234, 5678, 1357, 1234, 5678]
	print(is_empty(landing, takeoff))
	print(is_empty2(planes))
