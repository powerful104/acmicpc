#1676번 오버플로우 신경쓴 알고리즘
def ins(n):
    ans=0
    while n%5==0:
        n=n//5
        ans+=1
    return ans

num = int(input())
ans=0
for i in range(num):
    ans+=ins(i+1)
print(ans)