n = int(input())
for i in range(n):
    for j in range(n):
        print((n+1)*(i+1)-(i+1)*(j+1), end=' ')
    print()