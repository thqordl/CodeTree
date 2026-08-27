a,b = map(int,input().split())
per=[0]*10
while a>1:
    per[a%b]+=1
    a//=b
print(sum(i*i for i in per))