n = int(input())
sum=0
k=0
for i in range(1,101):
    if sum>=n:
        break
    sum+=i
    k=i
print(k)