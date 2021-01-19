import math as m
num=int(input())
for _ in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    length = m.sqrt((x1-x2)**2+(y1-y2)**2)
    ans = 0
    if length==0 and r1==r2:
        ans=-1
    elif r1+r2==length or abs(r1-r2)==length:
        ans = 1
    elif abs(r1-r2)<length<r1+r2:
        ans = 2
    print(ans)