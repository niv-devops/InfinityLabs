# Approved by: Arin

if __name__ == "__main__":
    """ Reads first n lines of file """
    file_name = input("From which file do you want to read? ")
    n = int(input("How many lines to read? "))

    with open(file_name, mode="r") as file:
        for line in (file.readlines() [:n]):
            print(line, end ='')