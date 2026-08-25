n=int(input())
for i in range(n):
    arr=input().split()
    a,b=int(arr[0]),int(arr[1])

    xab=1
    for j in range(a,b+1):
        xab*=j
    print(xab)