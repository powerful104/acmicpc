import sys
num = int(input())
list=[]
for _ in range(num):
    n = int(sys.stdin.readline())
    list.append(n)
list.sort()
for i in range(num):
    print(list[i])