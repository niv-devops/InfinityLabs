# Approved by: Arin

import string # For A...Z

if __name__ == "__main__":
    """ Generate 26 text files anmes A.txt, B.txt .. Z.txt
        Write the name of the letter for each file """

    for x in string.ascii_uppercase:
        with open(f"{x}.txt", mode="w") as file:
            file.write(f"{x}")