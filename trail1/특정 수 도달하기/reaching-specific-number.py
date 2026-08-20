arr = list(map(int, input().split()))
hap, cnt=0,0
for i in range(10):
    if arr[i]>=250:
        break
    else:
        hap+=arr[i]
        cnt+=1

print(f'{hap} {hap/cnt:.1f}')