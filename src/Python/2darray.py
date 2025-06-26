rows = int(input("Enter number of rows: "))
matrix = []

for i in range(rows):
    row = list(map(int,input().split()))
    matrix.append(row)

print("Matrix:")
for i in matrix:
    print(i)