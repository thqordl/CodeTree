nums=list(map(int,input().split()))
cnt=0
for i in range(10):
    if nums[i]==0:
        break
    cnt+=1
for i in range(cnt-1, -1,-1):
    print(nums[i], end=' ')