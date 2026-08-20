nums = list(map(int,input().split()))
cnt=0
for i in range(10):
    if nums[i]==0:
        break
    cnt+=1
print(sum(nums[:cnt]), f'{(sum(nums[:cnt])/(cnt)):.1f}')
