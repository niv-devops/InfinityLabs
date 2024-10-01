# Approved by: Arin

def unique_value(dict):
    """ Return list of all unique values in given dictionary """
    lst = []
    unique_lst = list(dict.values())
    for x in unique_lst:
        if unique_lst.count(x) == 1:
            lst.append(x)
    return lst


if __name__ == "__main__":
    dict = {
        "brand":"Ford",
        "model":"Mustang",
        "year":1964,
        "miles":1964,
        "Wannabe":"Mustang"
    }

    print("Unique values in dictionary:", unique_value(dict))