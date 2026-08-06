for i in range(4):
    sum = 0
    a = list(map(int, input().split()))
    for j in range(4):
        sum+=a[j]
    print(sum)