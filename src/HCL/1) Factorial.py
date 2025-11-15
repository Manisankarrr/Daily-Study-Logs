n = int(input())
def fact(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res
print(fact(n))