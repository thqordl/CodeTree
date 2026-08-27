arr=list(map(int,input().split()))
res=[0]*10

for i in arr:
    if i==0:
        break
    res[i//10]+=1

for i in range(1,10):
    print(f'{i} - {res[i]}')