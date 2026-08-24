n, m = map(int, input().split())

def minx(n,m):
    for i in range(max(n,m), m*n+1):
        if i%n==0 and i%m==0:
            print(i)
            break
minx(n,m)