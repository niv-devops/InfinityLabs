# Approved by: Matan

def count_char(string, char):
    """ Return number of times specified character appears in given string """
    counter = 0
    for x in string:
        if char == x:
            counter+=1
    return counter


if __name__ == "__main__":
    print("1) Character appears in string", count_char("amazing", "a"), "times")