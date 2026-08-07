n = int(input())
arr = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i%2==0:
            arr[j][i]=j+1
        else:
            arr[j][i]=n-j
    
for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()