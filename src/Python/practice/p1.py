k = int(input())

if(k < 0):
    print("Invalid input")
    exit()
for i in range(0, k+1):
    square = i*i
    if square > k:
        print(i-1)
        break
    elif square == k:
        print(i)
        break