a,b= map(int, input().split())
seta = set(list(map(int, input().split())))
setb = set(list(map(int, input().split())))
print(len((seta-setb)|(setb-seta)))