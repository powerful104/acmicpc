import math
num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    c = math.gcd(a,b)
    print(int(a*b/c))