a = [list(map(int, input().split())) for i in range(3)]
n = input()
b = [list(map(int, input().split())) for i in range(3)]

for i in range(3):
    for j in range(3):
        print(a[i][j]*b[i][j], end=' ')
    print()