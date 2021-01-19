num = int(input())
fn = 0
fn1 = 1
ans = fn1
for _ in range(num-1):
    ans=fn+fn1
    fn=fn1
    fn1=ans
print(ans)