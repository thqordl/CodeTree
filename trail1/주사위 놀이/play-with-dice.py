arr=list(map(int,input().split()))
res=[0]*7
for i in arr:
    res[i]+=1
for i in range(1,7):
    print(f'{i} - {res[i]}')