# Approved by: Matan

def is_complex(password):
    """ Return true if given password is complex enough """
    counters = [0] * 4

    if len(password) < 8:
        return False
    
    for i in password:
        if i>="0" and i<="9":
           counters[0] += 1
        elif i >= "a" and i <= "z":
            counters[1] += 1
        elif i >= "A" and i <= "Z":
            counters[2] += 1
        elif i == "@" or i == "#" or i == "%" or i == "&":
            counters[3] += 1

    for j in counters:
        if j == 0:
            return False
    return True


if __name__ == "__main__":
    password = "Abcd2224#"
    print("5) Is password complex?", is_complex(password))