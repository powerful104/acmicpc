import math as ma
num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    print(ma.factorial(m)//(ma.factorial(n)*ma.factorial(m-n)))