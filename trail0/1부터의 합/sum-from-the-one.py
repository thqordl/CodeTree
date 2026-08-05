n = int(input())
hap = 0
x = 0

for i in range(1, 101):
    if hap<n:
        hap += i
        continue
    x = i
    break
if x == 0:
    print(100)
else:
    print(x-1)