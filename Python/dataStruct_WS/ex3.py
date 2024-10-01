# Approved by: Arin

def combine_list(lst1, lst2):
    """ Return list containing shared elements from two given lists """
    lst = []
    for x in lst1:
        if x in lst2:
            lst.append(x)
    return lst


if __name__ == "__main__":
    lst1 = ["cartman", 20, True, 40, 30, "kyle", "kenny", 40, False, 50, "stan", True]
    lst2 = [15, True, "cartman", 35, 40, "Bob", "kenny"]
    print("Combined list:", combine_list(lst1, lst2))