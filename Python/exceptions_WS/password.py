# Approved by: Eitan

import exceptions

def is_complex(password):
    """ Return true if given password is complex enough """
    try:
        if len(password) < 8:
            raise exceptions.TooShortExeception
    except TypeError:
        print("Password must be a string!")

    counters = [0] * 4
    for char in password:
        if char.isdigit():
            counters[0] += 1
        elif char.islower():
            counters[1] += 1
        elif char.isupper():
            counters[2] += 1
        elif char in "@#%&":
            counters[3] += 1
        
    if not counters[0]:
        raise exceptions.NoNumberExeception
    elif not counters[1]:
        raise exceptions.NoLowerCaseExeception
    elif not counters[2]:
        raise exceptions.NoUpperCaseExeception
    elif not counters[3]:
        raise exceptions.NoSymbloExeception
    else:
        print("Password is complex.")


if __name__ == "__main__":
    password = "Abcd2224#" # Complex password
    #password = 12345 # Invalid data type exception
    #password = "abc123" # Password too short exception
    #password = "2כע26grDgr664#" # Invalid letter exception 
    #password = "aBcdefgh#" # No digits exception
    #password = "A1234567@" # No lowercase exception
    #password = "abcd1234@" # No uppercase exception
    #password = "Abcd1234" # No special character exception
    is_complex(password)