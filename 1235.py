import sys
num = int(input())
li = []
itmp=0
for _ in range(num):
    li.append(str(sys.stdin.readline()).strip())
for i in range(len(li[0])):
    litmp=[]
    for j in range(num):
        litmp.append(li[j][len(li[0])-1-i:])
    liset = set(litmp)
    if len(litmp)==len(liset):
        itmp=i+1
        break
print(itmp)