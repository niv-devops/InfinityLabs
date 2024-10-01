# Approved by: Arin

def rmv_second_until_empty(lst):
    """ Remove and print every second element in list until it's empty """
    num=0
    while (len(lst) > 0):
        num = (num+1) % len(lst)
        print(lst.pop(num), end =" ")


if __name__ == "__main__":
    lst = [1,2,3,4,5,6]
    print("Original list:", lst, end =" --> Removing elements: ")
    print("--> List after function:", rmv_second_until_empty(lst))