# Approved by: Matan

def convert_temper_cf (celsius):
    """ Convert tempeture from celsius to fahrenheit """
    return (celsius*9/5) + 32


if __name__ == "__main__":
    celsius = 37
    print("3)", celsius, "in celsius is", convert_temper_cf(celsius), "in fahrenheit")