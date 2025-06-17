import os

file_path = "test.txt"

if os.path.exists(file_path):
    if os.path.isfile(file_path):
        print(f"{file_path} is a file.")
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory.")
    else:
        print(f"{file_path} exists but is neither a file nor a directory.")
else:
    print(f"{file_path} does not exist.")