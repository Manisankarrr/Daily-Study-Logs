n = int(input("Size: "))
# arr = list(map(int,input("Elements: ").split()))
arr = []
for i in range(n):
    arr.append(int(input()))
j = 0
count = 0
maxi = -1
for i in arr:
    if maxi < i:
        count += 1
        maxi = i
print(count)



arr = []
print("Enter elements one by one (press Enter without input to stop):")
while True:
    val = input()
    if val == "":
        break
    arr.append(int(val))

# Now process the array
j = 0
maxi = -1
count = 0
for i in arr:
    if i > maxi:
        count += 1
        maxi = i
print(count)   