# Approved by: Arin

def letter_occur(str):
    """ Return dict of letters in string and their occurances """
    dict = {}
    for x in str:
        dict[x] = dict.get(x, 0) + 1
    return dict


if __name__ == "__main__":
    str = "banana"
    print("Occurances in", str, "-->", letter_occur(str))