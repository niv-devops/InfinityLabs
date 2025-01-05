#!/usr/bin/python3

""" Module to check if given int number is palindrome """

def is_palindrome(num):
    """ Function return True if given int number is palindrome """
    str_num = str(num)
    start = 0
    end = len(str_num) - 1

    while start < end:
        if str_num[start] != str_num[end]:
            return False
        start += 1
        end -= 1
    return True


if __name__ == "__main__":
    print("is 123321 a palindrome number?:", is_palindrome(123321))
    print("is 1234321 a palindrome number?:", is_palindrome(1234321))
    print("is 123456 a palindrome number?:", is_palindrome(123456))
