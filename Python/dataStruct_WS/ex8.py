# Approved by: Arin

def find_min_max(dict):
    """ Print the keys of the first found max and min values in given dictionary """
    print("Key of max value:", list(dict.keys())[list(dict.values()).index(max(dict.values()))], end="   |   ")
    print("Key of min value:", list(dict.keys())[list(dict.values()).index(min(dict.values()))])


if __name__ == "__main__":
    dict = {
        "first":1,
        "second":2,
        "third":3,
        "fourth":4,
        "fifth":5,
        "sixth":6,
        "a":1
    }
    find_min_max(dict)