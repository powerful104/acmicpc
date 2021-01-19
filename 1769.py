nu = str(input())
n=0
while len(nu)!=1:
    tmp=0
    a=str(nu)
    for i in range(len(a)):
        tmp+=int(a[i])
    nu=str(tmp)
    n+=1
print(n)
if int(nu)%3==0:
    print("YES")
else:
    print("NO")