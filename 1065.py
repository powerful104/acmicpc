num = int(input())
ans=0
for i in range(1,num+1):
    a = list(map(int,list(str(i))))
    d = 0
    tmpd = 0
    check = 0
    if len(a)>2:
        for j in range(len(a)-1):
            d = a[j]-a[j+1]
            if(j!=0 and d != tmpd):
                check=1
            tmpd=d
        if check == 0:
            ans+=1
    else:
        ans+=1
print(ans)