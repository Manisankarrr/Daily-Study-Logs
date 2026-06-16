s = input("num: ")
# arr = list(map(int,input("Elements: ").split()))
# arr = []
# for i in range(n):
#     arr.append(int(input()))
a = 1
for i in range(len(s)):
    a *= int(s[i])
print(a)