start, end = map(int, input().split())
total = 0

for i in range(start, end+1):
    cnt = 0
    for j in range(i):
        if i%(j+1)==0:
            cnt+=1
    if cnt == 3:
        total+=1
print(total)