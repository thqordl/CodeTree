n = int(input())
numbers = map(int, input().split())
res = []

for num in numbers:
    if num%2==0:
        res.append(num)

res.reverse()
for i in res:
    print(i, end=' ')