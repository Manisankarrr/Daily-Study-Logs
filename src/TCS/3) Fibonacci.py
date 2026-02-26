n = int(input())
if n <= 0:
    print()
else:
    a , b = 0,1
    res = []
    for _ in range(n):
        res.append(str(a))
        a,b = b,a+b
    print(" ".join(res))