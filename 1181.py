import sys
num = int(sys.stdin.readline())
b=[]
c=[]
for _ in range(num):
    a = str(sys.stdin.readline())
    if not (a in c):
        b.append((a,len(a)))
        c.append(a)
f = sorted(b, key=lambda  x : (x[1], x[0]))
for i in f:
    print(i[0].strip())