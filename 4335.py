se=set(range(0,11))
while True:
    num = int(input())
    if num==0:
        break
    s=str(input())
    if s=="too high":
        se-=set(range(num,11))
    elif s=="too low":
        se-=set(range(1,num+1))
    elif s=="right on":
        if num in se:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        se=set(range(0,11))