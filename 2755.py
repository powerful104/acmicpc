num = int(input())
suma=0
sumb=0
for _ in range(num):
    a, b, c = map(str, input().split())
    score=0
    if c[0]=="A":
        score+=4.0
    elif c[0] == "B":
        score+=3.0
    elif c[0] == "C":
        score+=2.0
    elif c[0] == "D":
        score+=1.0

    if c[0]!="F":
        if c[1]=="+":
            score+=0.3
        elif c[1]=="-":
            score-=0.3
    suma+=float(b)*score
    sumb+=float(b)

if int(suma/sumb*1000)%10==5:
    print("{:.2f}".format(round(suma/sumb,2)+0.01))
else:
    print("{:.2f}".format(round(suma/sumb,2)))