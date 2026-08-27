n = int(input())
arr = list(map(int, input().split()))

def abs(n, arr):
    for i in range(n):
        if arr[i]<0:
            print(-arr[i], end=' ')
        else:
            print(arr[i], end=' ')
    
abs(n,arr)