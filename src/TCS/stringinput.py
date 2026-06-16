str  = input().strip()
nums = str.split(" ")
listt = []

for i in nums:
    listt.append(int(i))
    
for i in listt:
    print(i, end="\n")