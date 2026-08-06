arr = []
cnt3 = 0
cnt5 = 0

for i in range(10):
    arr.append(int(input()))

for n in arr:
    if n%3==0:
        cnt3+=1
    if n%5==0:
        cnt5+=1

print(cnt3, cnt5)
