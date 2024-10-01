# Approved by: Or

import os # For os functions

if __name__ == "__main__":
    print("OS name:", os.name, "-", os.uname()[0])
    print("Logged user:", os.getlogin())
    print("Current working dir:", os.getcwd())