import sys
num = int(input())
li=[]
lix=set([])
liy=set([])
ans=0
for i in range(num):
    a = tuple(map(int, sys.stdin.readline().split()))
    li.append(a)
li = sorted(li, key=lambda x: x[0])
for i in range(num-1):
    for j in range(i+1,num):
        if li[i][0]==li[j][0]:
            if not li[i][0] in liy:
                liy.add(li[i][0])
                ans +=1
            break
        else:
            break
li = sorted(li, key=lambda x: x[1])
for i in range(num-1):
    for j in range(i+1,num):
        if li[i][1]==li[j][1]:
            if not li[i][1] in lix:
                lix.add(li[i][1])
                ans += 1
            break
        else:
            break
print(ans)