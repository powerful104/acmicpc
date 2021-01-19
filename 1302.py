import sys
num = int(input())
list={}
li=[]
max=1
for _ in range(num):
    book = str(sys.stdin.readline())
    if book in list:
        list[book]+=1
        if list[book]>max:
            max=list[book]
    else:
        list[book]=1
for i in list.keys():
    if list[i]==max:
        li.append(i)
li.sort()
print(li[0])