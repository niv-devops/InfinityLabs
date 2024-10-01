# Approved by: Or

import sys # For argv

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for x in range(len(sys.argv)-1, 0, -1):
            print(sys.argv[x])