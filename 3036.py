import math as m
num = int(input())
li = list(map(int, input().split()))
for i in range(1,len(li)):
    print(str(li[0]//m.gcd(li[0],li[i]))+"/"+str(li[i]//m.gcd(li[0],li[i])))