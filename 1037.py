num = int(input())
n = list(map(int, input().split()))
n.sort()
if num%2==1:
    ans=n[num//2]**2
else:
    ans=n[0]*n[num-1]
print(ans)