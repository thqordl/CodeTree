score=list(map(int,input().split()))
stu=[0]*11
for i in score:
    if i==0:
        break
    stu[i//10]+=1

for i in range(10,0,-1):
    print(f'{i*10} - {stu[i]}')