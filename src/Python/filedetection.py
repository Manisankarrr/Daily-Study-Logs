import os #mandatory for file handling

file_path = "test/test.txt" #paste exact location of anyfile

if os.path.exists(file_path):#relative file path checking mean only both are in same folder or not
    print(f"{file_path} exists.")

    if os.path.isfile(file_path):#checking file is present or not
        print(f"{file_path} is a file.")
        file_size = os.path.getsize(file_path)
        print(f"Size of file: {file_size} bytes")
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory.")
else:
    print(f"{file_path} does not exist.")

