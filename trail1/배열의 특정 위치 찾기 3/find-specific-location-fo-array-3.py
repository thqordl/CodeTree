arr = list(map(int,input().split()))
rrr = []
for a in arr:
    if a==0:
        break
    rrr.append(a)
print(rrr[-1]+rrr[-2]+rrr[-3])