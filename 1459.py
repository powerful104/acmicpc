a,b,c,d = map(int, input().split())
if 2*c < d:
    e = (a + b) * c
elif 2*c > 2*d:
    if (a+b)%2==0:
        e=max(a,b)*d
    else:
        e=(max(a,b)-1)*d+c
else:
    if a==b:
        e=a*d
    else:
        e=min(a*d,b*d)+abs(a-b)*c
print(e)