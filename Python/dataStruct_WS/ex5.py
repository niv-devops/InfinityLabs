# Approved by: Arin

def left_rotate(lst):
    """ Perform rotation to the left in a given list """
    return  lst[1:] + lst[:1]


if __name__ == "__main__":
    lst = [1,2,3,4,5,6]
    print("Original list:", lst, "--> List after left rotation:", left_rotate(lst))