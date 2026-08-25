n = int(input())
arr = list(map(int, input().split()))

def change(arr):
    for i in range(n):
        if arr[i]%2==0:
            arr[i]= int(arr[i]/2)

change(arr)
for a in arr:
    print(a, end=' ')