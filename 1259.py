while 1:
    check=0
    name = str(int(input()))
    if name=="0":
        break
    for i in range(len(name)):
        if name[i] != name[len(name)-1-i]:
            check=1
    if check==1:
        print("no")
    else:
        print("yes")