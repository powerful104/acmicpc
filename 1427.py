num = str(input())
l=[]
for i in range(len(num)):
    l.append(int(num[i]))
l.sort()
l.reverse()
for i in range(len(num)):
    print(l[i],end="")