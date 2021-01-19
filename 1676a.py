#1676번 오버플로우 신경안쓴 알고리즘
num = int(input())
fact=1
for i in range(num):
    fact*=i+1
fact=list(str(fact))
fact.reverse()
ans=0
for i in fact:
    if i!="0":
        break
    ans+=1
print(ans)