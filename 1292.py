a,b= map(int, input().split())
c = []
for i in range(1,46):
    c += i*[i]
print(sum(c[a-1:b]))