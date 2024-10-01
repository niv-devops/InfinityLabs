# Approved by: Matan

def flip(num):
    """ Flip order of digit in given number """
    return str(num)[::-1]


if __name__ == "__main__":
    num = 12345
    print("2) Original number:", num, "--> Flipped number:", flip(num))