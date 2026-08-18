n = int(input())
sum, cnt = 0,0
for i in range(n):
    a = int(input())
    sum+=a
    cnt+=1
print(f'{sum} {sum/cnt:.1f}')