a,b,c = map(int,input().split())
res=''
for i in range(a, b+1):
    if i%c==0:
        res='Y'
if res=='Y':
    print('YES')
else:
    print('NO')