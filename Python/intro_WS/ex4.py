# Approved by: Matan

def is_leap (year):
    """ Return true if given year is a leap year """
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    year = 1600
    print("4) Is", year, "a leap year?", is_leap(year))