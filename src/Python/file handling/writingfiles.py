import json

txt_data = "hello nigga bro"
file_path = "write.txt"

employee = {
    "name":"nigga",
    "age" : 20,
    "job" : "Student"
}

file_path = "write.json"

# try:
#     with open(file=file_path, mode="w") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("file already exists")

try:
    with open(file=file_path, mode="w") as file:
        json.dump(employee, file)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("file already exists")