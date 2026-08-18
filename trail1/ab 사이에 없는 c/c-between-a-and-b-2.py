a,b,c = map(int, input().split())
res='YES'
for i in range(a, b+1):
    if i%c==0:
        res='NO'
print(res)