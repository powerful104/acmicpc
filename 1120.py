n=50
a,b= map(str, input().split())
if len(a)>len(b):
    a,b = b,a
for i in range(len(b)-len(a)+1):
    ina=0
    for j in range(len(a)):
        if(a[j]!=b[i+j]):
            ina+=1
    if n>ina:
        n=ina
print(n)