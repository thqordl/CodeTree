per=[0]*4
for i in range(3):
    cold, tem = input().split()
    if int(tem)>=37:
        if cold=='Y':
            per[0]+=1
        else:
            per[1]+=1
    else:
        if cold=='Y':
            per[2]+=1
        else:
            per[3]+=1

for i in per:
    print(i, end=' ')
if per[0]>=2:
    print('E')