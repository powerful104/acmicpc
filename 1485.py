import math as m
import sys
num = int(input())
for _ in range(num):
    sq=[]
    length=[]
    vec=[]
    ny=[]
    for _ in range(4):
        x, y = map(int, sys.stdin.readline().split())
        sq.append((x,y))
    for i in range(3):
        for j in range(i+1,4):
            length.append(m.sqrt((sq[i][0]-sq[j][0])**2+(sq[i][1]-sq[j][1])**2))
            vec.append((sq[i][0]-sq[j][0],sq[i][1]-sq[j][1]))
    for i in range(5):
        for j in range(i+1,6):
            ny.append(vec[i][0]*vec[j][0]+vec[i][1]*vec[j][1])
    length.sort()
    ny.sort()

    if length[0]==length[1]==length[2]==length[3] and ny.count(0)>=4:
        print(1)
    else:
        print(0)