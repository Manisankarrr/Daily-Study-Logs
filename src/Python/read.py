#read .txt,.json.csv

#------------------txt file------------------
# file_path = "test/testt1.txt"

# try:
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         print(lines)
# except FileNotFoundError:
#     print(f"File not found: {file_path}")
# except PermissionError:
#     print(f"Permission denied: {file_path}")

#------------------json file------------------
# import json

# file_path = "test/test.json"
# try:
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#         print(data["employee1"])
# except FileNotFoundError:
#     print(f"File not found: {file_path}")

# #------------------csv file------------------
# import csv
# import pandas as pd

# file_path = "test/test.csv"
# try:
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row[0], row[1], row[2])
# except FileNotFoundError:
#     print(f"File not found: {file_path}")