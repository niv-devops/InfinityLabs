# Approved by: Or

x = 3

def is_defined_global(name):
    """ Return true if given name is defined in the global namespace """
    y = 5
    if name in globals():
        return True
    return False

if __name__ == "__main__":
    print(is_defined_global("x"), is_defined_global("y"))