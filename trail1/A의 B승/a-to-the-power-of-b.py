a,b = map(int, input().split())
res=1
for i in range(b):
    res *=a
print(res)