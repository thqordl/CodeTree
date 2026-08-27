n=int(input())
  
arr=[i for i in range(n,10*n+1,n)]
cnt=0
for i in arr:
    if cnt==2:
        break
    print(i, end=' ')
    if i%5==0:
        cnt+=1