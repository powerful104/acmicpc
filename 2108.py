from collections import Counter
import sys
num = int(input())
li=[]
for i in range(num):
    li.append(int(sys.stdin.readline()))
print(round(sum(li)/num))
li.sort()
print(li[num//2])

c = Counter(li)
order = c.most_common()
maximum = order[0][1]

modes = []
for n in order:
    if n[1] == maximum:
        modes.append(n[0])
modes.sort()
if len(modes)!=1:
    print(modes[1])
else:
    print(modes[0])
print(li[num-1]-li[0])