# Approved by: Arin

def convert_dict(dict):
    """ Convert dictionary into list of tuples """
    return list(dict.items())


if __name__ == "__main__":
    dict = {
        "brand":"Ford",
        "model":"Mustang",
        "year":1964,
        "miles":1964
    }

    print("Converted dict to list of tuples:", convert_dict(dict))