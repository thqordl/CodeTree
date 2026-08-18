n = int(input())
res=''
for i in range(2, n):
    if n%i==0:
        res='C'
if res=='C':
    print('C')
else:
    print('N')