arr = list(map(int, input().split()))
hap,avg,cnt=0,0,0
for i in range(1,10,2):
    hap+=arr[i]
for j in range(2,10,3):
    avg+=arr[j]
    cnt+=1
print(f'{hap} {avg/cnt:.1f}')