name = str(input())
name = list(name)
setname=set(name)
setname=list(setname)
odd=0
tmp=[]
tmpr=[]
for i in setname:
    if name.count(i)%2==1:
        odd+=1
        charodd=i
if odd>1:
    print("I'm Sorry Hansoo")
else:
    if odd==1:
        name.remove(charodd)
    name.sort()
    for i in range(len(name)):
        if i%2==0:
            tmp.append(name[i])
    tmpr = list(tmp)
    tmpr.reverse()
    if odd==1:
        tmp.append(charodd)
    tmp = tmp + tmpr
    print("".join(tmp))