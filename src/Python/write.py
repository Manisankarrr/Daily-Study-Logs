# .txt, .json, .csv
#---------------------w-write on existing file|| overwrite-------------------------------------------
# txt_data = "I like to have a cup of coffee in the morning."

# file_path = "test/test.txt"
# # with opens and close the file automatically.
# with open(file=file_path, mode="w") as file: #open()-returns file obj,(filepath,mode[write-w|x,append-a,read-r]), as - giving name as file
#     file.write(txt_data)
#     print(f"text file '{file_path}' written successfully.")


# employee = ["employee1", "employee2", "employee3", "employee4", "employee5"]

# txt_data = "I like to have a cup of coffee in the morning."

# file_path = "test/test.txt"
# # with opens and close the file automatically.
# try:
#     with open(file=file_path, mode="w") as file: #open()-returns file obj,(filepath,mode[write-w|x,append-a,read-r]), as - giving name as file
#         for emp in employee:
#             file.write(emp + "\n")
#         print(f"text file '{file_path}' written successfully.")
# except FileExistsError:
#     print(f"File '{file_path}' already exists. Choose a different name or delete the existing file.")


#----------------------X-create & read------------------------------------------
# txt_data = "I like to have a cup of coffee in the morning."

# file_path = "test/test1.txt"
# # with opens and close the file automatically.
# try:#x - to create and write if exist it throws error so to avoid using exception handling
#     with open(file=file_path, mode="x") as file: #open()-returns file obj,(filepath,mode[write-w|x,append-a,read-r]), as - giving name as file
#         file.write(txt_data)
#         print(f"text file '{file_path}' written successfully.")
# except FileExistsError:
#     print(f"File '{file_path}' already exists. Choose a different name or delete the existing file.")

#---------------------.json file-------------------------------------------
# import json 

# employee = {
#     "employee1": "John Doe",
#     "employee2": "Jane Doe",
#     "employee3": "Alice Doe",
#     "employee4": "Bob Doe",
#     "employee5": "Emily Doe"
# }

# txt_data = "I like to have a cup of coffee in the morning."
# file_path = "test/test.json"
# # with opens and close the file automatically.
# try:
#     with open(file=file_path, mode="w") as file: #open()-returns file obj,(filepath,mode[write-w|x,append-a,read-r]), as - giving name as file
#         json.dump(employee, file, indent=4) #converts dict -> json string
#         print(f"json file '{file_path}' written successfully.")
# except FileExistsError:
#     print(f"File '{file_path}' already exists. Choose a different name or delete the existing file.")

#---------------------.csv file-------------------------------------------
# import csv

# employee = [["Name","Age","Job"],
#             ["John Doe", 30, "Software Engineer"],
#             ["Jane Doe", 25, "Data Scientist"],
#             ["Alice Doe", 28, "Web Developer"],
#             ["Bob Doe", 35, "Project Manager"],
#             ["Emily Doe", 29, "UX Designer"]]

# file_path = "test/test.csv"
# # with opens and close the file automatically.
# try:
#     with open(file=file_path, mode="w", newline="") as file: #open()-returns file obj,(filepath,mode[write-w|x,append-a,read-r]), as - giving name as file
#         writer = csv.writer(file)
#         for row in employee:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' written successfully.")
# except FileExistsError:
#     print(f"File '{file_path}' already exists. Choose a different name or delete the existing file.")

