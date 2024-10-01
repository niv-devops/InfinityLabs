# Approved by: Arin

def keep_str(lst):
    """ Remove all non-string vars from list """
    for x in list(lst):
        if type(x) != str:
            lst.remove(x)
    return lst


if __name__ == "__main__":
    lst = ["cartman", 20, True, 40, 30, "kyle", "kenny", False, 50, "stan", True]
    print("Modified list:", keep_str(lst))