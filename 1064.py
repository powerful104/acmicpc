import math as m
x1, y1, x2, y2, x3, y3 = map(int, input().split())
ans=0
a1=0
a2=0
if (x1-x2)!=0:
    a1 = abs(y1 - y2) / abs(x1 - x2)
if (x2-x3)!=0:
    a2 = abs(y2 - y3) / abs(x2 - x3)
length = []
if(a1==a2):
    ans=-1
else:
    length.append(m.sqrt((x1-x2)**2+(y1-y2)**2))
    length.append(m.sqrt((x2-x3)**2+(y2-y3)**2))
    length.append(m.sqrt((x3-x1)**2+(y3-y1)**2))
    length.sort()
    ans = 2*(length[2]-length[0])
print(ans)