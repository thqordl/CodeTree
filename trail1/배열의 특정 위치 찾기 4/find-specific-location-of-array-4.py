nums = list(map(int,input().split()))
cnt=0
hap=0
for i in range(10):
    if nums[i]==0:
        break
    if nums[i]%2==0:
        cnt+=1
        hap+=nums[i]
print(cnt, hap)