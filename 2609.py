n= input()
split_n= n.split()
a=int(split_n[0])
b=int(split_n[1])
c=[]
d=[]
e=[]
f=[]
um=0
am=0
cm=0
for i in range(1,a+1):
    if a%i == 0 :
        c.append(i)
        um=um+1
for j in range(1,b+1):
    if b%j == 0 :
        d.append(j)
        am=am+1
for i in range(0,um):
    for j in range(0,am):
        if c[i]==d[j]:
            e.append(d[j])
            cm=cm+1
print(e[cm-1])
print(int((a*b)/e[cm-1]))