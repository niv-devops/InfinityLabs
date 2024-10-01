# Approved by: Or

import os # For path, walk, stat, chmod
import sys # For argv, exit
import stat # For chnaging permissions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Expected syntax: python3 ex5.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    search_dir = os.path.expanduser("~")
    print(search_dir)
    found_files = []

    for root, _, files in os.walk(search_dir):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                found_files.append(file_path)

    if not found_files:
        print(f"No files '{file_name}' were found.")
    else:
        print(f"{len(found_files)} files found:")
        for file_path in found_files:
            print(f"File: {file_path}")
            enable_execute = input("Enable execution permission for owner and group? (yes/no): ").lower()
            permission = os.stat(file_path).st_mode | stat.S_IXUSR | stat.S_IXGRP

            if enable_execute == 'yes':
                if stat.S_IXUSR & os.stat(file_path).st_mode and stat.S_IXGRP & os.stat(file_path).st_mode:
                    print("File '{file_name}' already has execution permissions for user and group.")
                else:
                    os.chmod(file_path, permission)
                    print(f"Enabled {file_path} execution permission for owner and group.")
            elif enable_execute == 'no':
                print("Permissions untouched.")
            else:
                print("Invalid input.")